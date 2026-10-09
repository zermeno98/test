"""Exporta todos los documentos Markdown a Word (Word/) y a PDF (PDF/), y valida los Word.

Uso (desde la raíz del proyecto, con el entorno de verificacion/.venv):
    python exportar/exportar_todo.py [--solo 02 15 ...] [--sin-pdf] [--sin-word]
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# En la carpeta local los Markdown están en Markdown/; en GitHub, en estandares-ia/ (y CLAUDE.md en la raíz)
MD = RAIZ / 'Markdown' if (RAIZ / 'Markdown').exists() else RAIZ / 'estandares-ia'
WORD, PDF = RAIZ / 'Word', RAIZ / 'PDF'
PY = sys.executable
PLANTILLA_BASE = WORD / '15-convenio-tipo-universidades.docx'

CONF_EVAL = 'CONFIDENCIAL · Contiene claves de evaluación · Uso exclusivo del evaluador'
CONF_INSTR = 'Incluye el cuestionario final del curso, CONFIDENCIAL para instructores'

# clave, archivo md, título para el pie, opciones
DOCUMENTOS = [
    ('00', '00-indice-familia-estandares', 'Índice y estado del proyecto', {}),
    ('01', '01-mapa-funcional', 'Mapa funcional', {}),
    ('02', '02-EC-A-borrador', 'EC-A · Borrador 1.0 para validación', {'estandar': True}),
    ('03', '03-EC-B-borrador', 'EC-B · Borrador 1.0 para validación', {'estandar': True}),
    ('04', '04-exposicion-de-motivos', 'Exposición de motivos', {'diagramas': True}),
    ('05', '05-IEC-EC-A-guia-evaluador', 'IEC EC-A · Guía del evaluador', {'confidencial': CONF_EVAL}),
    ('06', '06-IEC-EC-A-materiales-candidato', 'IEC EC-A · Materiales del candidato', {}),
    ('07', '07-IEC-EC-B-guia-evaluador', 'IEC EC-B · Guía del evaluador', {'confidencial': CONF_EVAL}),
    ('08', '08-IEC-EC-B-materiales-candidato', 'IEC EC-B · Materiales del candidato', {}),
    ('09', '09-curso-alineacion-EC-A', 'Curso de alineación EC-A', {'confidencial': CONF_INSTR}),
    ('10', '10-guia-estudio-EC-A', 'Guía de estudio EC-A', {}),
    ('11', '11-curso-alineacion-EC-B', 'Curso de alineación EC-B', {'confidencial': CONF_INSTR}),
    ('12', '12-guia-estudio-EC-B', 'Guía de estudio EC-B', {}),
    ('13', '13-diagnostico-uso-IA', 'Diagnóstico de uso de IA', {}),
    ('14', '14-plantilla-politica-uso-IA', 'Plantilla de política de uso de IA', {}),
    ('15', '15-convenio-tipo-universidades', 'Convenio tipo con instituciones educativas', {}),
    ('16', '16-plan-prueba-piloto', 'Plan de la prueba piloto', {}),
    ('17', '17-gobernanza-comite-grupo-tecnico', 'Gobernanza: comité y grupo técnico', {}),
    ('18', '18-decision-EC-o-ECM', 'Decisión EC o ECM', {}),
    ('19', '19-avisos-de-privacidad', 'Avisos de privacidad', {}),
    ('20', '20-contratos-tipo', 'Contratos tipo', {}),
    ('21', '21-resumen-ejecutivo-socios', 'Resumen ejecutivo para los socios', {}),
    ('CLAUDE', 'CLAUDE', 'Contexto del proyecto', {'word': 'CLAUDE-contexto-del-proyecto'}),
]


def limpiar_plantilla(origen, destino):
    """Guarda el Word original como plantilla, sin su texto: conserva estilos, numeración y encabezado."""
    import docx
    from docx.oxml.ns import qn
    d = docx.Document(str(origen))
    body = d.element.body
    for child in list(body):
        if child.tag != qn('w:sectPr'):
            body.remove(child)
    d.save(str(destino))


def correr(args):
    r = subprocess.run([PY] + [str(x) for x in args], capture_output=True, text=True, encoding='utf-8',
                       env={**__import__('os').environ, 'PYTHONIOENCODING': 'utf-8'})
    if r.returncode != 0:
        raise SystemExit(f'ERROR en {args[0]}:\n{r.stdout}\n{r.stderr}')
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--solo', nargs='*')
    ap.add_argument('--sin-pdf', action='store_true')
    ap.add_argument('--sin-word', action='store_true')
    a = ap.parse_args()
    PDF.mkdir(exist_ok=True)
    fuente_plantillas = RAIZ / 'exportar' / 'plantillas'
    fuente_plantillas.mkdir(exist_ok=True)
    for clave, nombre, pie, op in DOCUMENTOS:
        if a.solo and clave not in a.solo:
            continue
        md = MD / f'{nombre}.md'
        if not md.exists() and (RAIZ / f'{nombre}.md').exists():
            md = RAIZ / f'{nombre}.md'
        nombre_word = op.get('word', nombre)
        docx_out = WORD / f'{nombre_word}.docx'
        # plantilla: el Word original de cada documento (copia de seguridad la primera vez)
        plantilla = fuente_plantillas / f'{nombre_word}.docx'
        if not plantilla.exists():
            origen = docx_out if docx_out.exists() else PLANTILLA_BASE
            limpiar_plantilla(origen, plantilla)
        if not a.sin_word:
            args = [RAIZ / 'exportar' / 'md_a_docx.py', md, plantilla, docx_out, '--titulo-pie', pie]
            if op.get('estandar'):
                args.append('--estandar')
            if op.get('confidencial'):
                args += ['--confidencial', op['confidencial']]
            if op.get('diagramas'):
                args += ['--diagramas', RAIZ / 'diagramas']
            for linea in correr(args).splitlines():
                if 'aviso' in linea.lower():
                    print(f'{clave:>6} Word  {linea.strip()}')
            chk = [RAIZ / 'exportar' / 'comprobar_texto.py', md, docx_out] + (['--estandar'] if op.get('estandar') else []) + (['--diagramas'] if op.get('diagramas') else [])
            res = correr(chk)
            print(f'{clave:>6} Word  {res}')
        if not a.sin_pdf:
            pdf_out = PDF / f'{nombre_word}.pdf'
            args = [RAIZ / 'exportar' / 'md_a_pdf.py', md, pdf_out, '--titulo-pie', f'{pie} · Octubre de 2026']
            if op.get('estandar'):
                args.append('--estandar')
            if op.get('confidencial'):
                args += ['--confidencial', op['confidencial']]
            if op.get('diagramas'):
                args.append('--diagramas')
            for linea in correr(args).splitlines():
                if 'aviso' in linea.lower():
                    print(f'{clave:>6} PDF   {linea.strip()}')
            print(f'{clave:>6} PDF   {pdf_out.name}')


if __name__ == '__main__':
    main()
