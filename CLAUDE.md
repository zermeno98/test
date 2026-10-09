# Proyecto: Estándares de Competencia CONOCER en Inteligencia Artificial

Contexto para continuar el proyecto desde Claude Code local. Escrito al cierre de la sesión en la nube del 9 de octubre de 2026. Todo el trabajo se hace en español de México.

## 1. Quién es el usuario y qué busca

- Es socio de una empresa con fines de lucro que desarrolla Estándares de Competencia (EC) con el CONOCER (Consejo Nacional de Normalización y Certificación de Competencias Laborales, sectorizado en la SEP). Sus socios son expertos en estándares de otras áreas, no en IA.
- Activos de la empresa: buena relación con la directora del CONOCER y un **centro evaluador que ya opera** y ha implementado otros estándares.
- Objetivo: estándares de IA **"con dientes"** (que generen demanda obligatoria o casi obligatoria) y que se moneticen rápido: cursos de alineación, evaluación y certificación, y consultoría.
- Analogía que usa el usuario: tras la explosión de la pipa de gas en Iztapalapa (septiembre de 2025) se emitieron las NOM-EM-006-ASEA-2025 y NOM-EM-007-ASEA-2025, que exigen capacitación de choferes acreditada con un estándar de competencia. No hubo reforma legal: el "diente" fue una NOM de emergencia emitida por una dependencia con facultades.

## 2. Decisiones estratégicas tomadas

1. **No depender de reformas legales.** Los "dientes" vienen de instrumentos que ya existen: NOM (Ley de Infraestructura de la Calidad), lineamientos de dependencias, requisitos en contratos, requisitos de egreso de universidades y obligaciones vigentes de las empresas.
2. **Mercados:**
   - Universidades: requisito de egreso. Subsistemas que dependen de la SEP (TecNM, universidades tecnológicas y politécnicas, DGETI, CONALEP) y privadas con RVOE. El EGEL del CENEVAL **no** es obligatorio a nivel nacional.
   - Empresas: la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF 20 de marzo de 2025) exige medidas de seguridad (art. 18) e informar vulneraciones (art. 19); la LFT obliga a capacitar (art. 153-A, constancias DC-3). Empleados que pegan datos en ChatGPT = riesgo legal actual.
   - Gobierno y sus proveedores.
3. **Familia de dos estándares:**
   - **EC-A (volumen):** *Protección de la información y verificación de resultados en el uso de herramientas de inteligencia artificial generativa.* Nivel Dos. 3 elementos: preparar la información, verificar los productos, atender incidentes (incluye deepfakes y suplantación). Evaluación: caso simulado de 2 h 30 min.
   - **EC-B (alto valor):** *Gestión de riesgos y controles en el uso de sistemas de inteligencia artificial en la organización.* Nivel Cuatro. 4 elementos: inventario, evaluación de riesgos, política y controles, supervisión e incidentes. Evaluación: caso práctico de 5 h. Alineado con NIST AI RMF e ISO/IEC 42001.
   - El EC-B (Elemento 3, programa de capacitación) genera demanda del EC-A.
4. **Descartados:** un estándar para docentes (ya existe el EC1691) y depender de la "Ley Antimemes", que al 9 de octubre de 2026 **no es ley**: Diputados la aprobó con cambios el 7 de octubre y regresa al Senado. Su tema (contenido sintético, imagen y voz) quedó incorporado en el EC-A.
5. **Unión Europea:** el artículo 4 de la Ley de IA (alfabetización en IA, vigente desde febrero de 2025) se flexibilizó en julio de 2026 con el Reglamento (UE) 2026/1744: mantiene la obligación de tomar medidas, sin exigir un nivel específico. No exagerarlo en materiales de venta.

## 3. Estándares de IA que ya existen en el RENEC (sin traslape con la familia)

EC1657 (IA generativa en cadena de suministro), EC1691 (materiales educativos con IA), EC1705 (uso básico de IA generativa para crear contenido digital; el más cercano, complementario), ECM0358 (Fundamentos de IA generativa por Microsoft, estándar de marca), EC1827, EC1828 y EC1829 (Acuerdo SE/III-26/05,R: aprobado el 3 de julio de 2026, DOF del 7 de agosto de 2026). Pendiente: revisar el Elemento 3 del EC1705 y lo publicado después del 7 de agosto de 2026.

## 4. Archivos

| Archivo | Contenido |
|---|---|
| `estandares-ia/00-indice-familia-estandares.md` | Índice, estado y lista de pendientes |
| `estandares-ia/01-mapa-funcional.md` | Mapa funcional, correspondencia NIST/ISO y revisión del RENEC |
| `estandares-ia/02-EC-A-borrador.md` | EC-A completo, versión 1.0, formato F21-COOPYD-01 |
| `estandares-ia/03-EC-B-borrador.md` | EC-B completo, versión 1.0, formato F21-COOPYD-01 |
| `estandares-ia/04-exposicion-de-motivos.md` | Exposición de motivos para lectores que no conocen el CONOCER |
| `estandares-ia/05-IEC-EC-A-guia-evaluador.md` | Instrumento de evaluación del EC-A, guía del evaluador (confidencial): plan, guiones, guía de observación, lista de cotejo, claves, juicio y cédula |
| `estandares-ia/06-IEC-EC-A-materiales-candidato.md` | Instrumento de evaluación del EC-A, materiales del candidato: caso ficticio, anexos A1 a A7 y cuestionario de 24 reactivos |
| `estandares-ia/07-IEC-EC-B-guia-evaluador.md` | Instrumento de evaluación del EC-B, guía del evaluador (confidencial): plan, guiones de las cuatro simulaciones, guía de observación, lista de cotejo, claves, juicio y cédula |
| `estandares-ia/08-IEC-EC-B-materiales-candidato.md` | Instrumento de evaluación del EC-B, materiales del candidato: caso ficticio, anexos B1 a B7 y cuestionario de 28 reactivos |

Copias en Google Drive (carpeta "Estándares de Competencia en IA - CONOCER"): https://drive.google.com/drive/folders/1UVEkFJ_GA7fd-w1_kA7MqKXrHWS-O3OP

Exposición de motivos con diagramas (documento de Claude): https://claude.ai/code/artifact/71df6896-f000-44f3-bf53-ef54f1417a0c

Rama de trabajo en GitHub: `claude/ai-standards-mexico-monetize-8v1qbe` del repositorio `zermeno98/test`.

## 5. Pendientes, en orden de prioridad

1. ~~Instrumento de Evaluación de Competencia (IEC) del EC-A~~ **Hecho como borrador 1.0** (archivos 05 y 06). Pendiente: prueba piloto, segunda versión paralela del caso y validar con el CONOCER el umbral del cuestionario (20 de 24) y la condición crítica.
2. ~~IEC del EC-B~~ **Hecho como borrador 1.0** (archivos 07 y 08). Pendiente: prueba piloto (medir si alcanzan 4 horas para doce productos), segunda versión paralela del caso y validar con el CONOCER el umbral del cuestionario (23 de 28) y la condición crítica.
   **Siguiente:** curso de alineación y guía de estudio del EC-A, que se derivan del IEC; después, los del EC-B.
3. Verificar en las fuentes oficiales (la sesión en la nube **no pudo** abrir conocer.gob.mx ni dof.gob.mx; tu máquina local sí puede):
   - La plantilla vigente F21-COOPYD-01 y sus frases fijas: "obtiene los siguientes" para productos, "demuestra la siguiente" para situaciones emergentes, "demuestra las siguientes" para actitudes.
   - El texto oficial de los niveles Dos y Cuatro del Sistema Nacional de Competencias.
   - La escala de niveles de conocimiento y el catálogo de actitudes que usa el CONOCER.
   - SINCO y SCIAN para estándares transversales.
   - El Elemento 3 del EC1705.
4. Revisión jurídica de las definiciones de la LFPDPPP 2025 (dato personal, dato sensible, vulneración) y de los artículos citados.
5. Gobernanza: Comité de Gestión por Competencias, grupo técnico y prueba piloto con universidades y empresas.
6. Decidir el registro como EC o como ECM (Estándar de Competencia de Marca) y qué control da cada opción sobre quién evalúa.
7. Pasar los estándares a la plantilla oficial en Word cuando el CONOCER la proporcione.
8. Paquete comercial: cursos de alineación (con constancia DC-3), diagnóstico empresarial de uso de IA, plantilla de política de uso de IA, convenio tipo con universidades. Los evaluadores necesitan certificación en EC0076.

## 6. Reglas de redacción de los estándares (CONOCER)

- Título del EC: sustantivo de acción ("Protección de…", "Gestión de…").
- Título de elemento: verbo en infinitivo + objeto + condición.
- Desempeños: verbo en presente, tercera persona, y condiciones en gerundio en viñetas; "y" antes del último inciso, y "e" si este empieza con "i" o "hi".
- Productos: "El [producto] elaborado:" seguido de "Contiene…", "Especifica…", "Incluye…".
- Conocimientos: introducidos con "La persona es competente cuando posee los siguientes:", en tabla con su nivel (Conocimiento, Comprensión o Aplicación).
- Duración: "X en gabinete y Y en campo, totalizando Z".
- Sin adjetivos subjetivos ("adecuado", "confiable"): criterios medibles ("al menos una fuente verificable distinta de la herramienta").
- Evaluación siempre con datos ficticios. Neutralidad tecnológica: ninguna marca obligatoria.
- No presentar como hecho lo que no se ha verificado: marcarlo "por confirmar". No prometer al usuario que un certificado es "obligatorio por ley".
- Las cifras de precios o ingresos que se han dado al usuario son hipotéticas.

## 7. Cómo arrancar

```
git clone https://github.com/zermeno98/test.git
cd test
git checkout claude/ai-standards-mexico-monetize-8v1qbe
claude
```

Primer mensaje sugerido para Claude local: "Lee CLAUDE.md y los archivos de estandares-ia/. Verifica en conocer.gob.mx la plantilla F21-COOPYD-01 y el EC1705, ajusta los borradores y después diseña el curso de alineación y la guía de estudio del EC-A a partir de su instrumento de evaluación (archivos 05 y 06)."
