# Verificación contra fuentes oficiales

Desde la sesión en la nube no se pudo abrir conocer.gob.mx ni dof.gob.mx. Esta carpeta permite hacer la verificación desde tu computadora:

- `descargar_fuentes.py` abre cada fuente con un navegador real (Playwright), guarda el PDF o la página y extrae su texto.
- `fuentes.json` es la lista de fuentes (estándares publicados, DOF, leyes, SCIAN y Ley de IA europea).
- Este archivo dice qué hay que verificar y cómo aplicar los cambios.

---

## Parte 1. Para ti: cómo arrancar (10 minutos)

Necesitas Python 3.10 o posterior y Git. En Visual Studio Code:

1. Abre la carpeta del repositorio. Si aún no lo tienes:
   ```
   git clone https://github.com/zermeno98/test.git
   cd test
   git checkout claude/ai-standards-mexico-monetize-8v1qbe
   ```
   Si ya lo tienes: `git pull origin claude/ai-standards-mexico-monetize-8v1qbe`.
2. Abre la terminal (menú Terminal → Nueva terminal) y escribe `claude`.
3. Pega este mensaje:

   > Lee CLAUDE.md y verificacion/INSTRUCCIONES.md (Parte 2). Ejecuta el script de descarga, haz todas las verificaciones V1 a V12, corrige los documentos, escribe el informe y sube los cambios a la rama.

Claude instalará lo necesario, correrá el script y te avisará si un sitio necesita que intervengas (por ejemplo, un captcha).

**Si prefieres correr el script tú mismo** (Windows, PowerShell):
```
cd verificacion
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
python descargar_fuentes.py
```
En Mac o Linux, la activación es `source .venv/bin/activate`. Agrega `--ver` para ver el navegador mientras trabaja.

---

## Parte 2. Para Claude en la computadora del usuario

### Contexto y reglas

- Lee primero `CLAUDE.md`. Todo en español de México.
- No uses la palabra "dientes" en ningún documento.
- No presentes como verificado lo que no lo esté: si una fuente no se encuentra, deja "por confirmar".
- No escribas que un certificado es "obligatorio por ley".
- Trabaja en la rama `claude/ai-standards-mexico-monetize-8v1qbe`. No abras un pull request.

### Paso 1. Descargar las fuentes

1. Desde `verificacion/`, crea el entorno e instala (comandos de la Parte 1) y ejecuta `python descargar_fuentes.py`.
2. Revisa `textos/_manifest.json`:
   - **error**: busca la URL vigente (búsqueda web o navegando con `--ver`), agrégala en `alternativas` de `fuentes.json` y vuelve a correr con `--solo ID`.
   - **buscar**: localiza la fuente, agrégala a `fuentes.json` con su URL y tipo, y descárgala con `--solo ID`.
   - **aviso de PDF escaneado**: lee el PDF directamente o deja el punto como "por confirmar".
3. Si un sitio pide captcha o bloquea el navegador sin ventana, corre con `--ver` y pide al usuario que lo resuelva.
4. Para una fuente extra: `python descargar_fuentes.py --url URL --id NOMBRE` (agrega `--tipo pagina` si no es PDF).

### Paso 2. Verificaciones

Para cada punto, cita el texto oficial literal (breve), compáralo con el borrador y corrige cuando no coincida.

| # | Qué verificar | Fuentes | Dónde está en el proyecto |
|---|---|---|---|
| V1 | Frases fijas del formato F21-COOPYD-01: "La persona es competente cuando demuestra los siguientes:" (desempeños), "obtiene los siguientes" y "obtiene el siguiente" (productos), "posee los siguientes" (conocimientos, con columna NIVEL), "demuestra la siguiente" (RESPUESTA ANTE SITUACIONES EMERGENTES, con SITUACIÓN EMERGENTE y RESPUESTAS ESPERADAS), "demuestra las siguientes" (ACTITUDES/HÁBITOS/VALORES) y GLOSARIO | EC1804, EC1780, EC1781, EC1827, EC1705, EC0554_01 | `estandares-ia/02-EC-A-borrador.md` y `03-EC-B-borrador.md` (Elementos); nota 2 del 02 y nota 5 del 03 |
| V2 | Campos de Datos Generales y su orden exacto: Propósito, Descripción general, Nivel, Comité, fechas de aprobación y publicación, Periodo sugerido de revisión/actualización, Tiempo de vigencia del certificado, SINCO (Grupo unitario, Ocupaciones asociadas, Ocupaciones no contenidas), SCIAN (Sector a Clase), nombre del campo de empresas participantes, Relación con otros estándares, Aspectos relevantes de la evaluación (Detalles de la práctica, Apoyos/Requerimientos, Duración estimada), Referencias de Información; tabla del Perfil y encabezado de cada elemento (Referencia, Código, Título). Señala cualquier campo nuevo en los estándares de 2026 | Mismos que V1 | Sección I y II del 02 y del 03 |
| V3 | Escala de niveles de conocimiento que usan los estándares (todas las palabras distintas de la columna NIVEL) y catálogo de actitudes (todas las actitudes distintas, por ejemplo Responsabilidad, Orden, Iniciativa, Perseverancia, Tolerancia, Amabilidad, Cooperación) | Todos los EC descargados | Tablas de conocimientos y actitudes del 02 y del 03; si una actitud no aparece en ningún estándar publicado, propón el reemplazo más cercano |
| V4 | Texto literal de los niveles Dos y Cuatro del Sistema Nacional de Competencias | EC0554_01, EC1804, EC1780 (Dos); EC0076, EC1410, EC1440 (Cuatro) | 02 (Nivel en el Sistema Nacional de Competencias: Dos) y 03 (Cuatro) |
| V5 | Clasificación: uso de SINCO 9999 en estándares transversales; nombres y códigos SCIAN vigentes de 561110 (propuesto para el EC-A) y 541610 (EC-B); cómo clasificaron el EC1705, el EC1657 y los EC1827 a EC1829 | EC1171, EC1705, EC1657, EC1827, INEGI_SCIAN, INEGI_SINCO | Tablas SINCO y SCIAN del 02 y 03; nota 3 del 02 y nota 4 del 03 |
| V6 | Elemento 3 de 3 del EC1705 ("Aplicar principios de uso responsable y seguro de la inteligencia artificial generativa"): copia sus desempeños, productos y conocimientos y compáralos criterio por criterio con el EC-A. Si hay traslape, propón cómo delimitar | EC1705 | `01-mapa-funcional.md` (fila EC1705 y conclusión) y nota 1 del 02 |
| V7 | Estándares publicados después del 7 de agosto de 2026 relacionados con IA, datos personales o seguridad de la información; si alguno se traslapa con el EC-A o el EC-B, descríbelo | CONOCER_PUBLICACIONES_DOF, DOF | Tabla del RENEC en 01 y en 04; lista de estándares en CLAUDE.md sección 3 |
| V8 | Acuerdo SE/III-26/05,R (DOF del 7 de agosto de 2026): fecha de aprobación, lista de estándares aprobados y si dice que el contenido es responsabilidad de quien lo desarrolla | DOF_2026_08_07 | Nota 6 del 03; 01 (filas EC1827 a EC1829); 04 (plazo de aprobación a publicación) |
| V9 | Ley Federal de Protección de Datos Personales en Posesión de los Particulares vigente: definiciones de dato personal, dato personal sensible (lista completa), responsable, encargado, remisión, transferencia y vulneración (si la define); lista de principios; artículos de medidas de seguridad y de vulneraciones (número y texto); fecha de la última reforma. Para instituciones públicas, nombre exacto de la Ley General | LFPDPPP, LFPDPPP_DOF_2025, LGPDPPSO | Glosarios del 02 (Elemento 1) y del 03; definiciones del 14; Unidad 2.1 del 12; preguntas sobre principios, remisión y vulneraciones del 08 y del cuestionario final del 11; cláusula NOVENA del 15; referencias de 02 y 03; CLAUDE.md sección 2 |
| V10 | Ley Federal del Trabajo: artículo 153-A y los que regulan la constancia de habilidades laborales y la comisión mixta (incluido a partir de cuántos trabajadores); criterios y formatos vigentes de la STPS para la DC-3 y clave de área temática que corresponde a estos cursos | LFT, STPS_DC3 | Datos para la DC-3 del 09 y del 11; sección 3.5 del 12; apartado 12.3 del 14; preguntas 21 y 22 del 08 |
| V11 | Reglas vigentes del Sistema Nacional de Competencias: quién acredita a Entidades de Certificación y Evaluación, Organismos Certificadores, Centros de Evaluación y Evaluadores Independientes; diferencias EC y ECM; existencia de estándares de uso restringido; evaluación a distancia; nombre vigente del comité que valida comités y estándares | CONOCER_REGLAS_SNC, CONOCER_INICIO, CONOCER_TRANSPARENCIA_55 y 61, CONOCER_ABC_CGC | 04 (cómo funciona el sistema), 15 (declaración II.2), 17 y 18 |
| V12 | Ley de IA de la Unión Europea: texto del artículo 4 y modificación por el Reglamento (UE) 2026/1744 (fecha y qué cambió) | EU_REGLAMENTO_IA, EU_REGLAMENTO_2026_1744 | 01 (referente adicional), 04 (tabla de referentes), CLAUDE.md sección 2 punto 5 |

### Paso 3. Corregir los documentos

- Aplica las correcciones en los archivos de `estandares-ia/` sin cambiar lo que no se relaciona con la verificación.
- Si un cambio en un estándar (02 o 03) afecta un criterio, revisa también su instrumento de evaluación (05 a 08), su curso (09 u 11) y su guía (10 o 12) para que sigan coincidiendo.
- Actualiza las notas "Fórmulas del formato" y "Clasificación" del 02 y del 03 con lo ya verificado y lo que siga "por confirmar".
- Actualiza `00-indice-familia-estandares.md` (casilla de verificación) y `CLAUDE.md` (pendiente 3).

### Paso 4. Informe

Crea `verificacion/INFORME-VERIFICACION.md` con:

1. Fecha y fuentes descargadas (id, URL, estado).
2. Una tabla por verificación: #, punto, fuente (archivo y página), texto oficial (cita breve), resultado (coincide / corregido / no encontrado), archivo modificado.
3. Lo que quedó "por confirmar" y por qué.

### Paso 5. Subir

1. Sube `verificacion/textos/` (textos extraídos y manifiesto), el informe y los documentos corregidos. Los PDF de `descargas/` no se suben (están en `.gitignore`).
2. Haz commit con un mensaje que resuma las correcciones y `git push -u origin claude/ai-standards-mexico-monetize-8v1qbe`.
3. Dile al usuario en pocas líneas qué coincidió, qué se corrigió y qué sigue pendiente.
