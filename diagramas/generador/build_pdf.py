"""Construye el PDF de la exposición de motivos con los diagramas rediseñados.

Uso: python build_pdf.py <04-exposicion-de-motivos.md> <carpeta_con_svgfrag> <salida.pdf> [salida.html]
"""
import re
import sys
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

md_path, frag_dir, pdf_out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
html_out = Path(sys.argv[4]) if len(sys.argv) > 4 else None

texto = md_path.read_text(encoding="utf-8")

# --- títulos y versión
m = re.match(r"# (.+)\n\n(.+)\n", texto)
titulo, version = m.group(1), m.group(2)
texto = texto[m.end():]

# --- sustituir el texto de los tres esquemas por marcadores de figura
def sustituir(patron, marcador, texto):
    nuevo, n = re.subn(patron, marcador, texto, flags=re.S)
    assert n == 1, (marcador, n)
    return nuevo

texto = sustituir(r"\*\*Así nace un estándar\*\*.*?vuelve a evaluarse\.\n", "\n\nFIGURA1\n", texto)
texto = sustituir(r"\| EC-A · Usuario de IA \| EC-B · Responsable de la IA \|\n.*?incidentes e informe a la dirección \|\n", "\nFIGURA2\n", texto)
texto = sustituir(r"\| Fase \| Qué incluye \| Punto de control \|\n.*?revisión cada 2 años \| \|\n", "\nFIGURA3\n", texto)

html = markdown.markdown(texto, extensions=["tables", "sane_lists"])

FIGS = {
    "FIGURA1": ("01-estandar-ciclo", "Figura 1. Un estándar se crea una vez y certifica a muchas personas. Seis pasos en dos etapas."),
    "FIGURA2": ("02-familia-estandares", "Figura 2. Dos estándares: uno para quien usa la IA y otro para quien responde por ella. Familia de dos estándares y siete elementos."),
    "FIGURA3": ("03-ruta-fases", "Figura 3. Ruta de implementación: cuatro fases y tres puntos de control."),
}
for clave, (archivo, pie) in FIGS.items():
    svg = (frag_dir / f"{archivo}.svgfrag").read_text(encoding="utf-8")
    svg = svg.replace(' data-w="720"', "")
    assert f"<p>{clave}</p>" in html, clave
    html = html.replace(f"<p>{clave}</p>", f'<figure>{svg}<figcaption>{pie}</figcaption></figure>')

CSS = """
@page { size: Letter; margin: 0.8in 0.7in 0.85in 0.7in; }
:root { --ink:#2d3142; --muted:#4f5d75; --soft:#7a8399; --rule:rgba(45,49,66,.16); --paper:#f5f5f5; --acc:#eb6c36; }
* { box-sizing: border-box; }
html { font-size: 10pt; }
body { font-family:'Geist',system-ui,sans-serif; color:var(--ink); line-height:1.55; margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.cabecera { border-bottom:1px solid var(--rule); padding-bottom:14pt; margin-bottom:18pt; }
.cabecera .eyebrow { font-family:'Geist Mono',monospace; font-size:7.5pt; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); margin:0 0 8pt; }
h1 { font-family:'Instrument Serif','Noto Serif',serif; font-weight:400; font-size:27pt; line-height:1.12; letter-spacing:-.02em; margin:0 0 8pt; }
.version { font-size:9pt; color:var(--muted); margin:0; }
h2 { font-family:'Instrument Serif','Noto Serif',serif; font-weight:400; font-size:19pt; letter-spacing:-.015em; line-height:1.15; margin:24pt 0 8pt; break-after:avoid; }
p { margin:0 0 8pt; }
strong { font-weight:600; }
ul, ol { margin:0 0 9pt; padding-left:15pt; } li { margin:0 0 3pt; }
a { color:#2e5aa8; text-decoration:none; border-bottom:.5pt solid rgba(46,90,168,.4); overflow-wrap:anywhere; }
table { width:100%; border-collapse:collapse; margin:6pt 0 12pt; font-size:8.3pt; line-height:1.4; }
table:not(:has(tbody tr:nth-child(5))) { break-inside:avoid; }
thead th { text-align:left; font-weight:600; font-size:7.8pt; background:var(--paper); color:var(--ink); border-top:1px solid var(--ink); border-bottom:1px solid var(--rule); padding:5pt 6pt; }
tbody td { vertical-align:top; padding:5pt 6pt; border-bottom:1px solid var(--rule); }
tr { break-inside:avoid; }
tbody tr td:first-child { font-weight:500; }
figure { margin:8pt 0 12pt; break-inside:avoid; }
figure svg { display:block; width:100%; height:auto; border:1px solid var(--rule); border-radius:8px; }
figcaption { font-size:8pt; color:var(--muted); margin-top:5pt; }
h2 + p, h2 + table { break-before:avoid; }
p:has(+ figure) { break-after:avoid; }
"""

doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><title>{titulo}</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="cabecera"><p class="eyebrow">CONOCER · Estándares de Competencia · Exposición de motivos</p><h1>{titulo}</h1><p class="version">{version}</p></div>
{html}
</body></html>"""

if html_out:
    html_out.write_text(doc, encoding="utf-8")

tmp = pdf_out.with_suffix(".tmp.html")
tmp.write_text(doc, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page()
    pg.goto(tmp.resolve().as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(1200)
    plantilla_cab = '<div style="width:100%;font-family:Geist,Arial,sans-serif;font-size:7pt;color:#7a8399;padding:0 0.7in;">Exposición de motivos · Estándares de Competencia en Inteligencia Artificial</div>'
    plantilla_pie = '<div style="width:100%;font-family:Geist,Arial,sans-serif;font-size:7pt;color:#7a8399;padding:0 0.7in;display:flex;justify-content:space-between;"><span>Borrador 1.0 · Octubre de 2026</span><span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>'
    pg.pdf(path=str(pdf_out), format="Letter", print_background=True, display_header_footer=True,
           header_template=plantilla_cab, footer_template=plantilla_pie,
           margin={"top": "0.8in", "bottom": "0.85in", "left": "0.7in", "right": "0.7in"})
    b.close()
tmp.unlink()
print("PDF", pdf_out)
