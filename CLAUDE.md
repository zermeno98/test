# Proyecto: Estándares de Competencia CONOCER en Inteligencia Artificial

Contexto para continuar el proyecto desde Claude Code local. Escrito al cierre de la sesión en la nube del 9 de octubre de 2026. Todo el trabajo se hace en español de México.

## 1. Quién es el usuario y qué busca

- Es socio de una empresa con fines de lucro que desarrolla Estándares de Competencia (EC) con el CONOCER (Consejo Nacional de Normalización y Certificación de Competencias Laborales, sectorizado en la SEP). Sus socios son expertos en estándares de otras áreas, no en IA.
- Activos de la empresa: buena relación con la directora del CONOCER y un **centro evaluador que ya opera** y ha implementado otros estándares.
- Objetivo: estándares de IA que generen demanda obligatoria o casi obligatoria y que se moneticen rápido: cursos de alineación, evaluación y certificación, y consultoría.
- Analogía que usa el usuario: tras la explosión de la pipa de gas en Iztapalapa (septiembre de 2025) se emitieron las NOM-EM-006-ASEA-2025 y NOM-EM-007-ASEA-2025, que exigen capacitación de choferes acreditada con un estándar de competencia. No hubo reforma legal: la obligación vino de una NOM de emergencia emitida por una dependencia con facultades.

## 2. Decisiones estratégicas tomadas

1. **No depender de reformas legales.** La obligación de certificarse viene de instrumentos que ya existen: NOM (Ley de Infraestructura de la Calidad), lineamientos de dependencias, requisitos en contratos, requisitos de egreso de universidades y obligaciones vigentes de las empresas.
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
| `estandares-ia/00-indice-familia-estandares.md` | Índice, estado, lista de pendientes y documentos por elaborar |
| `estandares-ia/01-mapa-funcional.md` | Mapa funcional, correspondencia NIST/ISO y revisión del RENEC |
| `estandares-ia/02-EC-A-borrador.md` | EC-A completo, versión 1.0, formato F21-COOPYD-01 |
| `estandares-ia/03-EC-B-borrador.md` | EC-B completo, versión 1.0, formato F21-COOPYD-01 |
| `estandares-ia/04-exposicion-de-motivos.md` | Exposición de motivos para lectores que no conocen el CONOCER |
| `estandares-ia/05-IEC-EC-A-guia-evaluador.md` | Instrumento de evaluación del EC-A, guía del evaluador (confidencial): plan, guiones, guía de observación, lista de cotejo, claves, juicio y cédula |
| `estandares-ia/06-IEC-EC-A-materiales-candidato.md` | Instrumento de evaluación del EC-A, materiales del candidato: caso ficticio, anexos A1 a A7 y cuestionario de 24 reactivos |
| `estandares-ia/07-IEC-EC-B-guia-evaluador.md` | Instrumento de evaluación del EC-B, guía del evaluador (confidencial): plan, guiones de las cuatro simulaciones, guía de observación, lista de cotejo, claves, juicio y cédula |
| `estandares-ia/08-IEC-EC-B-materiales-candidato.md` | Instrumento de evaluación del EC-B, materiales del candidato: caso ficticio, anexos B1 a B7 y cuestionario de 28 reactivos |
| `estandares-ia/09-curso-alineacion-EC-A.md` | Curso de alineación del EC-A (8 horas): carta descriptiva, guía del instructor, evaluación con cuestionario final de 15 reactivos (confidencial para instructores), datos para la DC-3, correspondencia con cada criterio del EC y reglas de integridad de la evaluación |
| `estandares-ia/10-guia-estudio-EC-A.md` | Guía de estudio del EC-A, que también es el cuaderno del participante del curso: contenidos, caso de práctica (Universidad Tecnológica Ficticia del Sur, distinto del caso del IEC), 10 ejercicios, autodiagnóstico, 15 preguntas de práctica y respuestas |
| `estandares-ia/11-curso-alineacion-EC-B.md` | Curso de alineación del EC-B (20 horas en cinco sesiones): carta descriptiva, guía del instructor, simulaciones en tríos con tarjetas de rol, evaluación con cuestionario final de 20 reactivos (confidencial para instructores), datos para la DC-3, correspondencia con cada criterio del EC y reglas de integridad |
| `estandares-ia/12-guia-estudio-EC-B.md` | Guía de estudio del EC-B y cuaderno del participante: contenidos, caso de práctica (Transportes Ficticios del Pacífico, distinto del caso del IEC), 16 ejercicios que integran un expediente, cuatro tarjetas de rol, autodiagnóstico, 20 preguntas de práctica y respuestas |
| `estandares-ia/13-diagnostico-uso-IA.md` | Diagnóstico empresarial de uso de IA (servicio de consultoría): modalidades exprés, estándar y ampliada; fases; insumos; autodiagnóstico de 20 preguntas con semáforo; cuestionario, guía de entrevista y lista de proveedores; índice de madurez; formato del informe con hoja de ruta de 90 días; confidencialidad; mensajes comerciales permitidos y no permitidos |
| `estandares-ia/14-plantilla-politica-uso-IA.md` | Plantilla de política de uso de IA con los diez contenidos del Producto 1 del Elemento 3 del EC-B, seis anexos (registro de sistemas autorizados, clasificación, solicitud de autorización, reporte de incidente, lista de proveedores, carta de conocimiento) y notas de adaptación |
| `estandares-ia/15-convenio-tipo-universidades.md` | Convenio específico de colaboración con instituciones educativas (alineación, evaluación y certificación), con anexos de programa de trabajo, condiciones económicas sin cifras, requisitos de sede y flujo de datos personales; notas para la empresa |
| `estandares-ia/16-plan-prueba-piloto.md` | Plan de la prueba piloto: universidades y empresas participantes, grupo con curso y sin curso, doble calificación, indicadores con criterios de decisión (tiempo, dificultad y discriminación de reactivos, acuerdo entre evaluadores, umbrales), calendario de 10 semanas, ética y consentimiento informado |
| `estandares-ia/17-gobernanza-comite-grupo-tecnico.md` | Ruta para el Comité de Gestión por Competencias (nuevo o adhesión), composición propuesta, contenido de la propuesta de integración, términos de referencia y cuatro sesiones del grupo técnico, minuta de validación, carta de confidencialidad y preguntas para el CONOCER |
| `estandares-ia/18-decision-EC-o-ECM.md` | Análisis EC frente a ECM (y EC de uso restringido, por confirmar), cómo capturar valor con un EC público, preguntas para el CONOCER y recomendación preliminar: EC público |

Copias en Google Drive (carpeta "Estándares de Competencia en IA - CONOCER"): https://drive.google.com/drive/folders/1UVEkFJ_GA7fd-w1_kA7MqKXrHWS-O3OP

Exposición de motivos con diagramas (documento de Claude): https://claude.ai/code/artifact/71df6896-f000-44f3-bf53-ef54f1417a0c

Rama de trabajo en GitHub: `claude/ai-standards-mexico-monetize-8v1qbe` del repositorio `zermeno98/test`.

## 5. Pendientes, en orden de prioridad

1. ~~Instrumento de Evaluación de Competencia (IEC) del EC-A~~ **Hecho como borrador 1.0** (archivos 05 y 06). Pendiente: prueba piloto, segunda versión paralela del caso y validar con el CONOCER el umbral del cuestionario (20 de 24) y la condición crítica.
2. ~~IEC del EC-B~~ **Hecho como borrador 1.0** (archivos 07 y 08). Pendiente: prueba piloto (medir si alcanzan 4 horas para doce productos), segunda versión paralela del caso y validar con el CONOCER el umbral del cuestionario (23 de 28) y la condición crítica.
   - ~~Curso de alineación y guía de estudio del EC-A~~ **Hechos como borrador 1.0** (archivos 09 y 10). No usan el caso ni los reactivos del IEC. Pendiente: confirmar la clave de área temática de la DC-3, el registro como agente capacitador externo ante la STPS y si el CONOCER exige que quien alinea no evalúe a las mismas personas.
   - ~~Curso de alineación y guía de estudio del EC-B~~ **Hechos como borrador 1.0** (archivos 11 y 12). Pendiente: medir en la piloto si 20 horas alcanzan.
   - ~~Diagnóstico empresarial y plantilla de política~~ **Hechos como borrador 1.0** (archivos 13 y 14). Sin precios: se definen aparte.
   - ~~Convenio tipo con universidades~~ **Hecho como borrador 1.0** (archivo 15), para revisión jurídica.
   - Revisión general del 9 de octubre de 2026 aplicada a los documentos 00 a 18. En el EC-A el cuestionario se aplica al final de la situación simulada, para que no adelante los errores sembrados.
   - **Siguiente:** segunda versión paralela de los casos de evaluación del EC-A y del EC-B (necesaria para la piloto y la operación), y después los demás documentos de la sección "Documentos por elaborar" del índice (00). El usuario pidió terminar los documentos, en especial los estándares; no hace falta preparar la reunión con el CONOCER.
3. Verificar en las fuentes oficiales (la sesión en la nube **no pudo** abrir conocer.gob.mx ni dof.gob.mx; tu máquina local sí puede). Ya verificado con fragmentos de estándares publicados (EC0076, EC0301, EC0554.01, EC1061, EC1410, EC1440, EC1171): frases de desempeños, productos y conocimientos; redacción de actitudes; textos de los niveles Dos y Cuatro; SINCO 9999. Falta:
   - Las frases "demuestra la siguiente" (situaciones emergentes) y "demuestra las siguientes" (actitudes).
   - La escala completa de niveles de conocimiento y el catálogo de actitudes (si incluye Perseverancia y Tolerancia).
   - Los códigos y nombres del SCIAN propuestos (561110 para el EC-A y 541610 para el EC-B).
   - El texto completo del Elemento 3 del EC1705 ("Aplicar principios de uso responsable y seguro de la inteligencia artificial generativa"), para compararlo criterio por criterio con el EC-A.
4. Revisión jurídica de las definiciones de la LFPDPPP 2025 (dato personal, dato sensible, vulneración) y de los artículos citados.
5. Gobernanza: Comité de Gestión por Competencias, grupo técnico y prueba piloto con universidades y empresas. Documentos listos: plan de la piloto (16) y ruta del comité y términos de referencia del grupo técnico (17). Falta ejecutarlos.
6. Decidir el registro como EC o como ECM (Estándar de Competencia de Marca) y qué control da cada opción sobre quién evalúa. Análisis en el archivo 18: recomendación preliminar EC público; confirmar con el CONOCER si existe el EC de uso restringido y quién puede acreditarse.
7. Pasar los estándares a la plantilla oficial en Word cuando el CONOCER la proporcione.
8. Paquete comercial: ~~cursos de alineación~~ (archivos 09 y 11), ~~diagnóstico empresarial~~ (13), ~~plantilla de política~~ (14) y ~~convenio tipo con universidades~~ (15) hechos como borrador 1.0. Los evaluadores necesitan certificación en EC0076.

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
- No usar en los documentos la expresión "con dientes" ni "dientes": es un término interno de los socios. Decir "que dependencias, universidades y empresas lo exijan" o "demanda obligatoria o casi obligatoria".

## 7. Cómo arrancar

```
git clone https://github.com/zermeno98/test.git
cd test
git checkout claude/ai-standards-mexico-monetize-8v1qbe
claude
```

Primer mensaje sugerido para Claude local: "Lee CLAUDE.md y los archivos de estandares-ia/. Verifica en conocer.gob.mx la plantilla F21-COOPYD-01 y el EC1705, ajusta los borradores y después elabora la segunda versión paralela de los casos de evaluación del EC-A y del EC-B."
