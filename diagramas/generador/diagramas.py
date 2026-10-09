"""Genera los tres diagramas de la exposición de motivos con las reglas de la skill diagram-design.

Salida: fragmentos SVG (para el PDF) y archivos HTML autónomos.
Estilo: el predeterminado de la skill (papel #f5f5f5, tinta #2d3142, un acento #eb6c36).
"""
from html import escape
from pathlib import Path

INK, MUTED, SOFT, ACC = "#2d3142", "#4f5d75", "#7a8399", "#eb6c36"
PAPER = "#f5f5f5"
ACC_T = "rgba(235,108,54,0.08)"
RULE = "rgba(45,49,66,0.10)"
RULE2 = "rgba(45,49,66,0.22)"
SANS = "'Geist', system-ui, sans-serif"
MONO = "'Geist Mono', ui-monospace, monospace"

MARKERS = f"""
  <defs>
    <marker id="{{s}}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{MUTED}"/></marker>
    <marker id="{{s}}-arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{ACC}"/></marker>
    <marker id="{{s}}-arrow-link" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#2e5aa8"/></marker>
  </defs>"""


def t(x, y, s, size=12, weight=400, fill=INK, family=SANS, anchor="start", ls=None, style=None):
    extra = f' letter-spacing="{ls}"' if ls else ""
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{family}" text-anchor="{anchor}"{extra}{st}>{escape(s)}</text>')


def eyebrow(x, y, s, fill=MUTED, size=8, anchor="start"):
    return t(x, y, s, size=size, weight=500, fill=fill, family=MONO, anchor=anchor, ls="0.18em")


def box(x, y, w, h, kind="white"):
    """Máscara opaca de papel y caja con el tratamiento del tipo de nodo."""
    fills = {
        "white": ("#ffffff", INK, "", 1),
        "store": ("rgba(45,49,66,0.05)", MUTED, "", 1),
        "optional": ("rgba(45,49,66,0.02)", "rgba(45,49,66,0.38)", ' stroke-dasharray="4,3"', 1),
        "focal": (ACC_T, ACC, "", 1),
        "note": (ACC_T, ACC, ' stroke-dasharray="4,3"', 1),
    }
    fill, stroke, dash, sw = fills[kind]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{PAPER}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')


def node(x, y, w, h, name, lines, kind="white", name_fill=INK):
    out = [box(x, y, w, h, kind), t(x + 12, y + 24, name, 12, 600, name_fill)]
    for i, ln in enumerate(lines):
        out.append(t(x + 12, y + 42 + 13 * i, ln, 10, 400, MUTED))
    return "".join(out)


def label(cx, y_line, s, fill=MUTED, above=True):
    """Etiqueta de flecha con máscara opaca y 6 px de aire sobre el trazo."""
    w = int(len(s) * 6.4 + 12) // 4 * 4 + 4
    top = y_line - 6 - 12
    return (f'<rect x="{cx - w // 2}" y="{top}" width="{w}" height="12" rx="2" fill="{PAPER}"/>'
            + t(cx, top + 9, s, 8, 400, fill, MONO, "middle", "0.06em"))


def legend(slug, y, items, x0=24, width=720):
    """Franja horizontal inferior. items: (tipo, texto) con tipo en box/arrow."""
    out = [f'<line x1="{x0}" y1="{y}" x2="{width - x0}" y2="{y}" stroke="{RULE}" stroke-width="0.8"/>',
           eyebrow(x0, y + 18, "LEYENDA")]
    x = x0
    yy = y + 32
    for kind, text in items:
        if kind in ("white", "store", "optional", "focal", "note"):
            fills = {"white": ("#ffffff", INK, ""), "store": ("rgba(45,49,66,0.05)", MUTED, ""),
                     "optional": ("rgba(45,49,66,0.02)", "rgba(45,49,66,0.38)", ' stroke-dasharray="3,2"'),
                     "focal": (ACC_T, ACC, ""), "note": (ACC_T, ACC, ' stroke-dasharray="3,2"')}[kind]
            out.append(f'<rect x="{x}" y="{yy - 8}" width="16" height="10" rx="2" fill="{fills[0]}" stroke="{fills[1]}" stroke-width="1"{fills[2]}/>')
            out.append(t(x + 22, yy, text, 9, 400, MUTED))
            x += 22 + int(len(text) * 5.0) + 28
        else:
            stroke, dash, marker = {"arrow": (MUTED, "", "arrow"), "dash": (MUTED, ' stroke-dasharray="4,3"', "arrow"),
                                    "accent": (ACC, "", "arrow-accent")}[kind]
            out.append(f'<line x1="{x}" y1="{yy - 3}" x2="{x + 24}" y2="{yy - 3}" stroke="{stroke}" stroke-width="1.2"{dash} marker-end="url(#{slug}-{marker})"/>')
            out.append(t(x + 32, yy, text, 9, 400, MUTED))
            x += 32 + int(len(text) * 5.0) + 28
    return "".join(out)


def svg(slug, w, h, title, desc, body):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="{slug}-title {slug}-desc" data-w="{w}">'
            f'<title id="{slug}-title">{escape(title)}</title><desc id="{slug}-desc">{escape(desc)}</desc>'
            + MARKERS.replace("{s}", slug) +
            f'<rect width="100%" height="100%" fill="{PAPER}"/>' + body + "</svg>")


# ---------------------------------------------------------------- Figura 1: swimlane
def figura1():
    s = "estandar-ciclo"
    W = 720
    nx = [160, 344, 528]          # columnas (ancho 160, separación 24)
    nw, nh = 160, 80
    y1, y2 = 40, 192              # y de los nodos de cada carril
    top, div, bot = 24, 144, 312  # líneas de carril
    b = []
    # carriles
    b += [f'<line x1="24" y1="{top}" x2="696" y2="{top}" stroke="{RULE2}" stroke-width="1"/>',
          f'<line x1="24" y1="{div}" x2="696" y2="{div}" stroke="{RULE}" stroke-width="1"/>',
          f'<line x1="24" y1="{bot}" x2="696" y2="{bot}" stroke="{RULE2}" stroke-width="1"/>',
          f'<line x1="144" y1="{top}" x2="144" y2="{bot}" stroke="{RULE2}" stroke-width="1"/>']
    b += [eyebrow(36, 76, "SE CREA"), eyebrow(36, 90, "UNA VEZ"),
          eyebrow(36, 228, "SE CERTIFICA"), eyebrow(36, 242, "A CADA PERSONA")]
    # flechas (antes que las cajas)
    m1 = y1 + nh // 2
    m2 = y2 + nh // 2
    for a, c in ((0, 1), (1, 2)):
        b.append(f'<line x1="{nx[a] + nw}" y1="{m1}" x2="{nx[c]}" y2="{m1}" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    b.append(f'<line x1="{nx[0] + nw}" y1="{m2}" x2="{nx[1]}" y2="{m2}" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    b.append(f'<line x1="{nx[1] + nw}" y1="{m2}" x2="{nx[2]}" y2="{m2}" stroke="{ACC}" stroke-width="1.4" marker-end="url(#{s}-arrow-accent)"/>')
    # traspaso: DOF y RENEC -> Evaluación (codo con r=8)
    px, ex = nx[2] + 96, nx[1] + 80
    ybus = 168
    b.append(f'<path d="M{px},{y1 + nh} V{ybus - 8} Q{px},{ybus} {px - 8},{ybus} H{ex + 8} Q{ex},{ybus} {ex},{ybus + 8} V{y2}" '
             f'fill="none" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    b.append(label((px + ex) // 2, ybus, "REFERENCIA"))
    # reintento (discontinuo): Evaluación -> Preparación
    bx, ax = nx[1] + 80, nx[0] + 80
    yl = y2 + nh + 24
    b.append(f'<path d="M{bx},{y2 + nh} V{yl - 8} Q{bx},{yl} {bx - 8},{yl} H{ax + 8} Q{ax},{yl} {ax},{yl - 8} V{y2 + nh}" '
             f'fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#{s}-arrow)"/>')
    b.append(label((bx + ax) // 2, yl, "REEVALUACIÓN"))
    # nodos
    b.append(node(nx[0], y1, nw, nh, "Comité de Gestión", ["Empleadores, trabajadores", "e instituciones redactan", "el estándar"]))
    b.append(node(nx[1], y1, nw, nh, "Comité Técnico", ["Revisa el estándar", "y lo aprueba"]))
    b.append(node(nx[2], y1, nw, nh, "DOF y RENEC", ["Publicación oficial y", "consulta pública", "y gratuita"], "store"))
    b.append(node(nx[0], y2, nw, nh, "Preparación", ["Curso de alineación,", "opcional"], "optional"))
    b.append(node(nx[1], y2, nw, nh, "Evaluación", ["Un centro acreditado", "observa a la persona", "y revisa sus evidencias"]))
    b.append(node(nx[2], y2, nw, nh, "Certificado oficial", ["Si demuestra la", "competencia; vale en", "todo el país"], "focal"))
    b.append(legend(s, bot + 16, [("white", "Paso"), ("optional", "Paso opcional"), ("store", "Registro público"),
                                  ("focal", "Resultado"), ("arrow", "Flujo"), ("dash", "Reintento si aún no es competente")]))
    return svg(s, W, 372, "Un estándar se crea una vez y certifica a muchas personas",
               "Dos carriles: el Comité de Gestión redacta el estándar, el Comité Técnico lo aprueba y se publica en el DOF y el RENEC; "
               "con esa referencia, un centro acreditado evalúa a cada persona y le otorga el certificado oficial.", "".join(b))


# ---------------------------------------------------------------- Figura 2: árbol
def figura2():
    s = "familia-estandares"
    W = 720
    cy = 128                      # y de las tarjetas
    cw = 320
    ax_, bx_ = 24, 376
    b = []
    # conectores desde la raíz (puntos de salida distintos)
    b.append(f'<path d="M336,80 V96 Q336,104 328,104 H{ax_ + cw // 2 + 8} Q{ax_ + cw // 2},104 {ax_ + cw // 2},112 V{cy}" fill="none" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    b.append(f'<path d="M384,80 V96 Q384,104 392,104 H{bx_ + cw // 2 - 8} Q{bx_ + cw // 2},104 {bx_ + cw // 2},112 V{cy}" fill="none" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    # vínculo EC-B (elemento 3) -> EC-A (nota)
    y3 = cy + 64 + 2 * 52 + 26
    yn = cy + 64 + 3 * 52 + 4 + 26
    b.append(f'<path d="M{bx_},{y3} H{bx_ - 8} Q{bx_ - 16},{y3} {bx_ - 16},{y3 + 8} V{yn - 8} Q{bx_ - 16},{yn} {bx_ - 24},{yn} H{ax_ + cw - 12}" '
             f'fill="none" stroke="{ACC}" stroke-width="1.4" marker-end="url(#{s}-arrow-accent)"/>')
    b.append(f'<circle cx="{bx_}" cy="{y3}" r="3" fill="{ACC}"/>')
    # raíz
    b.append(box(200, 24, 320, 56, "white"))
    b.append(eyebrow(360, 42, "PROPÓSITO PRINCIPAL", anchor="middle", size=7.5))
    b.append(t(360, 58, "Usar y gestionar la IA en las organizaciones de forma", 10, 400, MUTED, anchor="middle"))
    b.append(t(360, 71, "segura, responsable y conforme a la normatividad", 10, 400, MUTED, anchor="middle"))
    # tarjetas
    cards = [
        (ax_, "EC-A · Usuario de IA", "Para toda persona que usa IA · nivel 2", [
            ("Preparar la información", ["Herramienta autorizada, información", "clasificada y datos personales retirados"]),
            ("Verificar los productos", ["Datos contrastados con fuentes, derechos", "de terceros y uso de IA declarado"]),
            ("Atender incidentes", ["Solicitudes sospechosas confirmadas por", "otro canal e incidentes reportados"])]),
        (bx_, "EC-B · Responsable de la IA", "Para quien responde por la IA · nivel 4", [
            ("Integrar el inventario", ["Cada sistema de IA con su proveedor,", "uso, área responsable y datos que procesa"]),
            ("Evaluar los riesgos", ["Matriz de riesgos y evaluación de impacto", "de los usos que afectan a las personas"]),
            ("Establecer política y controles", ["Política de uso, revisión de proveedores,", "plan de controles y capacitación"]),
            ("Supervisar y atender incidentes", ["Verificación de controles, registro de", "incidentes e informe a la dirección"])]),
    ]
    for x, ttl, sub, rows in cards:
        h = 64 + 4 * 52 + 12
        b.append(box(x, cy, cw, h, "white"))
        b.append(t(x + 12, cy + 26, ttl, 12, 600))
        b.append(t(x + 12, cy + 42, sub, 10, 400, MUTED))
        b.append(f'<line x1="{x + 12}" y1="{cy + 56}" x2="{x + cw - 12}" y2="{cy + 56}" stroke="{RULE2}" stroke-width="0.8"/>')
        for i, (nm, ds) in enumerate(rows):
            top = cy + 64 + 52 * i
            if i:
                b.append(f'<line x1="{x + 12}" y1="{top}" x2="{x + cw - 12}" y2="{top}" stroke="{RULE}" stroke-width="0.8"/>')
            b.append(f'<rect x="{x + 12}" y="{top + 10}" width="16" height="16" rx="2" fill="transparent" stroke="rgba(45,49,66,0.40)" stroke-width="0.8"/>')
            b.append(t(x + 20, top + 22, str(i + 1), 9, 500, MUTED, MONO, "middle"))
            b.append(t(x + 38, top + 22, nm, 12, 600))
            for j, ln in enumerate(ds):
                b.append(t(x + 38, top + 36 + 12 * j, ln, 10, 400, MUTED))
    # nota de conexión dentro de la tarjeta EC-A (4.º espacio)
    ny = cy + 64 + 3 * 52 + 4
    b.append(box(ax_ + 12, ny, cw - 24, 52, "note"))
    b.append(eyebrow(ax_ + 24, ny + 17, "CÓMO SE CONECTAN", fill=ACC, size=7.5))
    b.append(t(ax_ + 24, ny + 32, "El EC-B define la capacitación del personal;", 10, 400, MUTED))
    b.append(t(ax_ + 24, ny + 45, "el EC-A acredita que el personal la aplica", 10, 400, MUTED))
    bottom = cy + 64 + 4 * 52 + 12
    b.append(legend(s, bottom + 16, [("white", "Estándar y elementos"), ("note", "Vínculo entre estándares"),
                                     ("arrow", "Se desglosa en")]))
    return svg(s, W, bottom + 16 + 48, "Dos estándares: uno para quien usa la IA y otro para quien responde por ella",
               "El propósito principal se desglosa en el EC-A, con tres elementos para el usuario de IA, y el EC-B, con cuatro para el responsable; "
               "el programa de capacitación del EC-B se acredita en el personal mediante el EC-A.", "".join(b))


# ---------------------------------------------------------------- Figura 3: fases
def figura3():
    s = "ruta-fases"
    W = 720
    xs = [24, 200, 376, 552]
    cw, ch, y = 144, 176, 24
    fases = [
        ("1", "Preparación", ["Comité de Gestión por", "Competencias integrado;", "el grupo técnico valida", "mapa y borradores"], "PUNTO DE CONTROL", "Borradores validados"),
        ("2", "Prueba piloto", ["Instrumentos probados", "con empresas y", "universidades; revisión", "jurídica"], "PUNTO DE CONTROL", "Piloto aprobado"),
        ("3", "Aprobación", ["El Comité Técnico del", "CONOCER aprueba; se", "publica en el DOF y se", "inscribe en el RENEC"], "PUNTO DE CONTROL", "Publicado en el DOF"),
        ("4", "Operación", ["Evaluación acreditada en", "centros y entidades;", "primeras personas", "certificadas"], "REVISIÓN SUGERIDA", "Cada 2 años"),
    ]
    b = []
    mid = y + 88
    for i in range(3):
        b.append(f'<line x1="{xs[i] + cw}" y1="{mid}" x2="{xs[i + 1]}" y2="{mid}" stroke="{MUTED}" stroke-width="1.2" marker-end="url(#{s}-arrow)"/>')
    for i, (n, nm, ds, ey, tx) in enumerate(fases):
        x = xs[i]
        kind = "focal" if i == 0 else "white"
        b.append(box(x, y, cw, ch, kind))
        stroke = ACC if i == 0 else "rgba(45,49,66,0.40)"
        b.append(f'<rect x="{x + 12}" y="{y + 12}" width="44" height="14" rx="2" fill="transparent" stroke="{stroke}" stroke-width="0.8"/>')
        b.append(t(x + 34, y + 22, f"FASE {n}", 7.5, 500, ACC if i == 0 else MUTED, MONO, "middle", "0.12em"))
        if i == 0:
            b.append(eyebrow(x + cw - 12, y + 22, "SE SOLICITA", fill=ACC, size=7.5, anchor="end"))
        b.append(t(x + 12, y + 50, nm, 12, 600))
        for j, ln in enumerate(ds):
            b.append(t(x + 12, y + 68 + 13 * j, ln, 10, 400, MUTED))
        b.append(f'<line x1="{x + 12}" y1="{y + 120}" x2="{x + cw - 12}" y2="{y + 120}" stroke="{RULE2}" stroke-width="0.8"/>')
        b.append(eyebrow(x + 12, y + 138, ey, size=7))
        b.append(t(x + 12, y + 156, tx, 11, 600))
    bottom = y + ch + 20
    b.append(legend(s, bottom, [("focal", "Paso que se solicita"), ("white", "Fase"), ("arrow", "Siguiente fase")]))
    return svg(s, W, bottom + 48, "Cuatro fases llevan los borradores a los primeros certificados",
               "Ruta de implementación en cuatro fases: preparación, prueba piloto, aprobación y operación; "
               "cada una cierra con un punto de control y la última con revisión sugerida cada dos años.", "".join(b))


FIGURAS = {"01-estandar-ciclo": figura1, "02-familia-estandares": figura2, "03-ruta-fases": figura3}

PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{ --color-paper:#f5f5f5; --color-ink:#2d3142; --color-muted:#4f5d75;
      --font-sans:'Geist',system-ui,sans-serif; --font-serif:'Instrument Serif',serif; --font-mono:'Geist Mono',ui-monospace,monospace; }}
    body {{ font-family:var(--font-sans); background:var(--color-paper); color:var(--color-ink); min-height:100vh;
      display:flex; align-items:center; justify-content:center; padding:3rem 2rem; }}
    .frame {{ max-width:1200px; width:100%; }}
    .diagram-container {{ width:100%; overflow-x:auto; }}
    .eyebrow {{ font-family:var(--font-mono); font-size:.66rem; font-weight:500; letter-spacing:.18em; text-transform:uppercase; color:var(--color-muted); margin-bottom:.5rem; }}
    h1 {{ font-family:var(--font-serif); font-size:clamp(1.5rem,2.4vw + .75rem,2rem); font-weight:400; letter-spacing:-.02em; line-height:1.15; margin-bottom:1.5rem; }}
    svg {{ width:100%; min-width:{w}px; display:block; }}
    @media print {{ .diagram-container {{ overflow-x:visible; }} svg {{ min-width:0; }} }}
  </style>
</head>
<body>
  <div class="frame">
    <p class="eyebrow">{eyebrow} · Exposición de motivos</p>
    <h1>{title}</h1>
    <div class="diagram-container">
{svg}
    </div>
  </div>
</body>
</html>
"""

EYEBROWS = {"01-estandar-ciclo": "Carriles", "02-familia-estandares": "Jerarquía", "03-ruta-fases": "Proceso"}

if __name__ == "__main__":
    import re
    import sys
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for nombre, fn in FIGURAS.items():
        s = fn()
        title = re.search(r"<title[^>]*>(.*?)</title>", s).group(1)
        w = re.search(r'data-w="(\d+)"', s).group(1)
        (out / f"{nombre}.svgfrag").write_text(s, encoding="utf-8")
        (out / f"{nombre}.html").write_text(PAGE.format(title=title, svg=s, w=w, eyebrow=EYEBROWS[nombre]), encoding="utf-8")
        print(nombre, len(s))
