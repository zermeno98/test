"""Convierte los documentos Markdown del proyecto a PDF para imprimir (tamaño carta).

Uso:
    python md_a_pdf.py ENTRADA.md SALIDA.pdf [--estandar] [--confidencial TEXTO] [--diagramas]
                       [--titulo-pie TEXTO]

    --estandar      encabezado del formato F21-COOPYD-01 con número de página (documentos 02 y 03)
    --confidencial  banda de confidencialidad en el encabezado
    --diagramas     inserta los diagramas de diagramas/generador en la exposición de motivos
"""
import argparse
import re
import sys
from html import escape
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / 'diagramas' / 'generador'))


from md_a_docx import preprocesar  # noqa: E402  (misma preparación que el Word)


CSS = """
@page { size: Letter; }
:root { --ink:#2d3142; --muted:#4f5d75; --soft:#7a8399; --rule:rgba(45,49,66,.16); --paper:#f5f5f5; }
* { box-sizing: border-box; }
html { font-size: 10pt; }
body { font-family:'Geist',Arial,sans-serif; color:var(--ink); line-height:1.5; margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1 { font-family:'Instrument Serif','Noto Serif',serif; font-weight:400; font-size:25pt; line-height:1.12; letter-spacing:-.02em; margin:0 0 8pt; }
h2 { font-family:'Instrument Serif','Noto Serif',serif; font-weight:400; font-size:17pt; letter-spacing:-.01em; line-height:1.15; margin:20pt 0 7pt; break-after:avoid; }
h3 { font-size:11pt; font-weight:600; margin:14pt 0 5pt; break-after:avoid; }
h4 { font-size:10pt; font-weight:600; margin:10pt 0 4pt; break-after:avoid; }
p { margin:0 0 7pt; }
strong { font-weight:600; }
ul, ol { margin:0 0 8pt; padding-left:16pt; } li { margin:0 0 2.5pt; } li > ul, li > ol { margin:2pt 0 2pt; }
a { color:#2e5aa8; text-decoration:none; overflow-wrap:anywhere; word-break:break-all; }
code { font-family:'Geist Mono',Consolas,monospace; font-size:8.5pt; background:#f0f0f0; padding:0 2px; border-radius:2px; overflow-wrap:anywhere; }
blockquote { margin:6pt 0 10pt; padding:6pt 10pt; border-left:2.5pt solid #bfc0c0; background:#f7f7f7; }
blockquote p:last-child { margin-bottom:0; }
hr { border:0; border-top:1px solid var(--rule); margin:14pt 0; }
table { width:100%; border-collapse:collapse; margin:5pt 0 11pt; font-size:8.2pt; line-height:1.38; }
thead th { text-align:left; font-weight:600; font-size:7.8pt; background:var(--paper); border-top:1px solid var(--ink); border-bottom:1px solid var(--rule); padding:4pt 5pt; }
thead { display: table-header-group; }
tbody td { vertical-align:top; padding:4pt 5pt; border-bottom:1px solid var(--rule); overflow-wrap:break-word; }
th { overflow-wrap:break-word; }
.nw { white-space:nowrap; }
tr { break-inside:avoid; }
table:has(th:nth-child(6)) { font-size:7.4pt; }
table:has(th:nth-child(6)) td, table:has(th:nth-child(6)) th { padding:3pt 3.5pt; }
table:has(th:nth-child(8)) { font-size:6.9pt; }
table:not(:has(tbody tr:nth-child(5))) { break-inside:avoid; }
figure { margin:8pt 0 12pt; break-inside:avoid; }
figure svg { display:block; width:100%; height:auto; border:1px solid var(--rule); border-radius:8px; }
figcaption { font-size:8pt; color:var(--muted); margin-top:5pt; }
h2 + p, h2 + table, h3 + p, h3 + table, h3 + ul, h3 + ol { break-before:avoid; }
p:has(+ figure) { break-after:avoid; }
.estandar h2 { font-family:'Geist',Arial,sans-serif; font-weight:600; font-size:13pt; letter-spacing:0; border-bottom:1px solid var(--ink); padding-bottom:3pt; }
.estandar h3 { font-size:10.5pt; }
"""

ENC_ESTANDAR = """<div style="width:100%;padding:0 0.7in;font-family:Arial,sans-serif;font-size:7.5pt;color:#2d3142;">
<table style="width:100%;border-collapse:collapse;"><tr>
<td style="border:0.6pt solid #2d3142;padding:3pt 6pt;font-weight:bold;font-size:9pt;width:42%;">ESTÁNDAR DE COMPETENCIA</td>
<td style="border:0.6pt solid #2d3142;padding:3pt 6pt;line-height:1.35;">Formato de Estándar de Competencia F21-COOPYD-01<br>Versión: borrador 1.0 para validación<br>Página <span class="pageNumber"></span> de <span class="totalPages"></span></td>
</tr></table></div>"""


def encabezado_simple(texto, confidencial):
    color = '#b03a2e' if confidencial else '#7a8399'
    peso = 'bold' if confidencial else 'normal'
    return (f'<div style="width:100%;padding:0 0.7in;font-family:Arial,sans-serif;font-size:7pt;color:{color};'
            f'font-weight:{peso};">{escape(texto)}</div>')


def pie(titulo):
    return ('<div style="width:100%;padding:0 0.7in;font-family:Arial,sans-serif;font-size:7pt;color:#7a8399;'
            'display:flex;justify-content:space-between;">'
            f'<span>{escape(titulo)}</span><span>Página <span class="pageNumber"></span> de '
            '<span class="totalPages"></span></span></div>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada')
    ap.add_argument('salida')
    ap.add_argument('--estandar', action='store_true')
    ap.add_argument('--confidencial')
    ap.add_argument('--diagramas', action='store_true')
    ap.add_argument('--titulo-pie', default='Borrador 1.0 · Octubre de 2026')
    a = ap.parse_args()

    texto = Path(a.entrada).read_text(encoding='utf-8')
    if a.estandar:
        texto = texto.split('\n---\n', 1)[1]  # título y versión van en el encabezado F21
    if a.diagramas:
        import diagramas as D
        from md_a_docx import sustituir_figuras  # mismos reemplazos que el Word
        texto = sustituir_figuras(texto)
    # URLs sueltas como enlaces, para que se puedan cortar sin angostar otras columnas
    texto = re.sub(r'(?<![(<\[`])\bhttps?://[^\s)>\]|`]+[^\s)>\]|`.,;:]', lambda m: f'<{m.group(0)}>', texto)
    html = markdown.markdown(preprocesar(texto), extensions=['tables', 'sane_lists'])
    # en las celdas, las palabras cortas con guion (folios como Q3-0311) no se parten
    def _sin_corte(m):
        celda = re.sub(r'(?<![\w/.-])(\w{1,6}(?:-\w{1,8}){1,3})(?![\w/.-])',
                       lambda x: f'<span class="nw">{x.group(1)}</span>' if len(x.group(1)) <= 14 else x.group(1),
                       m.group(2))
        return m.group(1) + celda + m.group(3)
    html = re.sub(r'(<td>)(.*?)(</td>)', lambda m: m.group(1) + re.sub(r'>([^<]*)<', lambda n: '>' + _sin_corte(re.match(r'()(.*)()', n.group(1), re.S)) + '<', '>' + m.group(2) + '<')[1:-1] + m.group(3), html, flags=re.S)
    if a.diagramas:
        figs = {'FIGURA1': (D.figura1, 'Figura 1. Un estándar se crea una vez y certifica a muchas personas. Seis pasos en dos etapas.'),
                'FIGURA2': (D.figura2, 'Figura 2. Dos estándares: uno para quien usa la IA y otro para quien responde por ella. Familia de dos estándares y siete elementos.'),
                'FIGURA3': (D.figura3, 'Figura 3. Ruta de implementación: cuatro fases y tres puntos de control.')}
        for clave, (fn, pie_fig) in figs.items():
            svg = fn().replace(' data-w="720"', '')
            assert f'<p>{clave}</p>' in html, clave
            html = html.replace(f'<p>{clave}</p>', f'<figure>{svg}<figcaption>{pie_fig}</figcaption></figure>')

    clase = 'estandar' if a.estandar else ''
    doc = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{escape(Path(a.entrada).stem)}</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body class="{clase}">{html}</body></html>"""

    salida = Path(a.salida)
    tmp = salida.with_suffix('.tmp.html')
    tmp.write_text(doc, encoding='utf-8')
    if a.estandar:
        enc, margen_sup = ENC_ESTANDAR, '1.15in'
    elif a.confidencial:
        enc, margen_sup = encabezado_simple(a.confidencial, True), '0.8in'
    else:
        enc, margen_sup = encabezado_simple('Estándares de Competencia en Inteligencia Artificial · CONOCER', False), '0.8in'
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        pg.goto(tmp.resolve().as_uri(), wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(800)
        # comprobación: nada debe exceder el ancho imprimible (8.5 - 1.4 pulgadas = 681 px);
        # si algo lo excede, Chromium reduce toda la página y la letra sale pequeña
        pg.emulate_media(media='print')
        pg.set_viewport_size({'width': 681, 'height': 1000})
        anchos = pg.evaluate("""() => {
            const W = document.documentElement.clientWidth, malos = [];
            document.querySelectorAll('body *').forEach(e => {
                const r = e.getBoundingClientRect();
                if (r.right > W + 2 && !e.closest('figure')) malos.push(e.tagName + ': ' + (e.textContent || '').trim().slice(0, 60));
            });
            return [document.documentElement.scrollWidth, W, malos.slice(0, 5)];
        }""")
        if anchos[0] > anchos[1] + 2:
            print(f'AVISO {salida.name}: contenido de {anchos[0]} px en {anchos[1]} px; {anchos[2]}')
        partidas = pg.evaluate("""() => {
            const cv = document.createElement('canvas').getContext('2d'), malas = [];
            document.querySelectorAll('td, th').forEach(c => {
                const cs = getComputedStyle(c);
                const util = c.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
                const recorre = (nodo, font) => {
                    nodo.childNodes.forEach(n => {
                        if (n.nodeType === 3) {
                            cv.font = font;
                            n.textContent.split(/\s+/).forEach(w => {
                                if (w && cv.measureText(w).width > util + 1 && !n.parentElement.closest('a, code'))
                                    malas.push(w);
                            });
                        } else if (n.nodeType === 1) {
                            const s = getComputedStyle(n);
                            recorre(n, `${s.fontWeight} ${s.fontSize} ${s.fontFamily}`);
                        }
                    });
                };
                recorre(c, `${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`);
            });
            return malas;
        }""")
        if partidas:
            print(f'AVISO {salida.name}: {len(partidas)} palabras no caben en su columna: {partidas[:8]}')
        pg.pdf(path=str(salida), format='Letter', print_background=True, display_header_footer=True,
               header_template=enc, footer_template=pie(a.titulo_pie),
               margin={'top': margen_sup, 'bottom': '0.8in', 'left': '0.7in', 'right': '0.7in'})
        b.close()
    if not __import__("os").environ.get("CONSERVAR_HTML"): tmp.unlink()
    print('ok', salida)


if __name__ == '__main__':
    main()
