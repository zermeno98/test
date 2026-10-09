"""Descarga las fuentes oficiales para verificar los Estándares de Competencia de IA.

Abre cada fuente con un navegador real (Playwright + Chromium), guarda el PDF o la
página y extrae su texto para que Claude pueda leerlo y compararlo con los borradores.

Uso (desde la carpeta verificacion/):
    python descargar_fuentes.py                      # todas las fuentes de fuentes.json
    python descargar_fuentes.py --solo EC1705 LFPDPPP # solo esas fuentes (por id)
    python descargar_fuentes.py --ver                 # muestra el navegador mientras trabaja
    python descargar_fuentes.py --url https://... --id MI_FUENTE   # una fuente adicional
    python descargar_fuentes.py --ignorar-certificados  # si un sitio de gobierno tiene
                                                          # el certificado vencido

Resultados:
    descargas/<id>.pdf o descargas/<id>.html   archivos originales (no se suben a GitHub)
    textos/<id>.txt                             texto extraído, con marcas de página
    textos/<id>.enlaces.json                    enlaces encontrados en las páginas
    textos/_manifest.json                       qué se descargó, de dónde, tamaño y huella
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

BASE = Path(__file__).resolve().parent
DESCARGAS = BASE / "descargas"
TEXTOS = BASE / "textos"
TIEMPO = 40_000  # milisegundos por intento


def es_pdf(datos: bytes) -> bool:
    return datos[:5] == b"%PDF-"


def texto_pdf(ruta: Path) -> tuple[str, int]:
    lector = PdfReader(str(ruta))
    partes = []
    for i, pagina in enumerate(lector.pages, start=1):
        try:
            contenido = pagina.extract_text() or ""
        except Exception as e:  # una página dañada no detiene las demás
            contenido = f"[No se pudo extraer el texto de esta página: {e}]"
        partes.append(f"\n=== Página {i} ===\n{contenido}")
    return "".join(partes), len(lector.pages)


def bajar_pdf(contexto, pagina, url: str, destino: Path) -> None:
    """Intenta primero una petición directa y, si no llega un PDF, abre la URL en el navegador."""
    try:
        resp = contexto.request.get(url, timeout=TIEMPO)
        datos = resp.body()
        if resp.ok and es_pdf(datos):
            destino.write_bytes(datos)
            return
        motivo = f"respuesta {resp.status}" + ("" if es_pdf(datos) else ", no es PDF")
    except PlaywrightError as e:
        motivo = str(e).splitlines()[0]
    # Segundo intento: navegación, que provoca la descarga del PDF.
    try:
        with pagina.expect_download(timeout=TIEMPO) as info:
            try:
                pagina.goto(url, timeout=TIEMPO)
            except PlaywrightError:
                pass  # al iniciar una descarga, goto se interrumpe; es normal
        info.value.save_as(destino)
        if es_pdf(destino.read_bytes()[:5]):
            return
        destino.unlink(missing_ok=True)
        raise RuntimeError("la descarga no es un PDF")
    except PlaywrightError as e:
        raise RuntimeError(f"{motivo}; navegador: {str(e).splitlines()[0]}") from None


def bajar_pagina(pagina, fuente: dict, url: str, destino: Path) -> tuple[str, list]:
    pagina.goto(url, timeout=TIEMPO, wait_until="domcontentloaded")
    try:
        pagina.wait_for_load_state("networkidle", timeout=20_000)
    except PlaywrightError:
        pass  # algunas páginas nunca dejan de cargar recursos
    destino.write_text(pagina.content(), encoding="utf-8")
    texto = pagina.inner_text("body")
    enlaces = pagina.eval_on_selector_all(
        "a[href]", "els => els.map(e => ({texto: (e.innerText || '').trim(), url: e.href}))"
    )
    patrones = [re.compile(p, re.IGNORECASE) for p in fuente.get("filtrar_enlaces", [])]
    if patrones:
        enlaces = [e for e in enlaces if any(p.search(e["texto"]) or p.search(e["url"]) for p in patrones)]
    return texto, enlaces


def procesar(contexto, pagina, fuente: dict) -> dict:
    fid = fuente["id"]
    tipo = fuente.get("tipo", "pdf")
    registro = {"id": fid, "tipo": tipo, "para": fuente.get("para", ""), "estado": "error"}
    if tipo == "buscar":
        registro.update(estado="buscar", nota="Sin URL fija: Claude debe localizarla (ver INSTRUCCIONES.md).")
        return registro
    urls = [fuente["url"]] + fuente.get("alternativas", [])
    errores = []
    for url in urls:
        try:
            if tipo == "pdf":
                destino = DESCARGAS / f"{fid}.pdf"
                bajar_pdf(contexto, pagina, url, destino)
                texto, paginas = texto_pdf(destino)
                registro["paginas"] = paginas
            else:
                destino = DESCARGAS / f"{fid}.html"
                texto, enlaces = bajar_pagina(pagina, fuente, url, destino)
                (TEXTOS / f"{fid}.enlaces.json").write_text(
                    json.dumps(enlaces, ensure_ascii=False, indent=1), encoding="utf-8"
                )
                registro["enlaces"] = len(enlaces)
            (TEXTOS / f"{fid}.txt").write_text(f"Fuente: {url}\n{texto}", encoding="utf-8")
            datos = destino.read_bytes()
            registro.update(
                estado="ok",
                url=url,
                bytes=len(datos),
                sha256=hashlib.sha256(datos).hexdigest(),
                caracteres_de_texto=len(texto),
            )
            if tipo == "pdf" and len(texto.strip()) < 20 * registro.get("paginas", 1):
                registro["aviso"] = "Casi sin texto: puede ser un PDF escaneado; revisarlo a mano."
            return registro
        except Exception as e:
            errores.append(f"{url}: {e}")
    registro["errores"] = errores
    return registro


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fuentes", default=str(BASE / "fuentes.json"), help="archivo con la lista de fuentes")
    ap.add_argument("--solo", nargs="*", help="ids de las fuentes a descargar")
    ap.add_argument("--url", help="URL de una fuente adicional")
    ap.add_argument("--id", help="id para la fuente adicional de --url")
    ap.add_argument("--tipo", default="pdf", choices=["pdf", "pagina"], help="tipo de la fuente de --url")
    ap.add_argument("--ver", action="store_true", help="mostrar el navegador")
    ap.add_argument("--ignorar-certificados", action="store_true", help="aceptar certificados HTTPS vencidos")
    ap.add_argument("--navegador", help="ruta a un ejecutable de Chromium o Chrome, si no se usa el de Playwright")
    args = ap.parse_args()

    fuentes = json.loads(Path(args.fuentes).read_text(encoding="utf-8"))["fuentes"]
    if args.url:
        fuentes = [{"id": args.id or "FUENTE_EXTRA", "tipo": args.tipo, "url": args.url, "para": "Fuente adicional"}]
    elif args.solo:
        pedidas = {s.upper() for s in args.solo}
        fuentes = [f for f in fuentes if f["id"].upper() in pedidas]
        if not fuentes:
            print("Ningún id coincide con fuentes.json.")
            return 1

    DESCARGAS.mkdir(exist_ok=True)
    TEXTOS.mkdir(exist_ok=True)
    manifest_ruta = TEXTOS / "_manifest.json"
    manifest = json.loads(manifest_ruta.read_text(encoding="utf-8")) if manifest_ruta.exists() else {}

    with sync_playwright() as p:
        opciones = {"headless": not args.ver}
        if args.navegador:
            opciones["executable_path"] = args.navegador
        navegador = p.chromium.launch(**opciones)
        contexto = navegador.new_context(
            locale="es-MX",
            accept_downloads=True,
            ignore_https_errors=args.ignorar_certificados,
        )
        pagina = contexto.new_page()
        for i, fuente in enumerate(fuentes, start=1):
            print(f"[{i}/{len(fuentes)}] {fuente['id']} ... ", end="", flush=True)
            registro = procesar(contexto, pagina, fuente)
            registro["fecha"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            manifest[fuente["id"]] = registro
            manifest_ruta.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
            print(registro["estado"] + (f" ({registro['aviso']})" if "aviso" in registro else ""))
            for err in registro.get("errores", []):
                print(f"      {err}")
        navegador.close()

    fallas = [k for k, v in manifest.items() if v["estado"] == "error"]
    print(f"\nListo. Correctas: {sum(v['estado'] == 'ok' for v in manifest.values())}. "
          f"Con error: {len(fallas)}. Por localizar: {sum(v['estado'] == 'buscar' for v in manifest.values())}.")
    if fallas:
        print("Con error: " + ", ".join(fallas))
    print(f"Textos en: {TEXTOS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
