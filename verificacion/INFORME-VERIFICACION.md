# Informe de verificación contra fuentes oficiales

**Fecha:** 9 de octubre de 2026. **Quién lo hizo:** Claude Code en la computadora del usuario, con el kit de `verificacion/` (Playwright y Chromium) y búsquedas web.
**Documentos revisados:** `Markdown/` (00 a 18 y CLAUDE.md). Los textos extraídos están en `verificacion/textos/`, con su registro en `textos/_manifest.json`.

## 0. Resumen

| Resultado | Puntos |
|---|---|
| Coincide, sin cambios | V4 (niveles Dos y Cuatro), V3 (escala y catálogo), V5 (SINCO y SCIAN), V8 (Acuerdo del DOF), V12 (Unión Europea) |
| Corregido | V1 (situaciones emergentes), V2 (campos del formato), V6 (delimitación con el EC1705, ahora con el texto), V9 (definiciones de la ley de datos), V10 (LFT y DC-3), V11 (acreditación y comité), enlaces rotos |
| Quedó por confirmar | Texto de EC1827 a EC1829, EC1657, EC1440 y EC1410 (sus PDF ya no están publicados); clave de área temática de la DC-3 en la fuente oficial; vigencia de los manuales del CONOCER de 2015 y 2016; EC restringidos; evaluación a distancia; revisión de un abogado |

**Hallazgos que cambian decisiones**

1. **El EC1705 es de nivel Tres, no Dos**, y su Elemento 3 de 3 no tiene productos ni conocimientos propios (solo dos desempeños y una actitud). El traslape con el EC-A es parcial en la intención y no en los criterios (V6).
2. **Los PDF de estándares de 2024 a 2026 ya no están en conocer.gob.mx.** La página de publicaciones los enlaza, pero la ruta `/contenido/publicaciones_dof/...` devuelve 404 y redirige al inicio. Se obtuvieron del Archivo de Internet (Wayback). Los de EC1827 a EC1829 no están ni ahí; el DOF los enlaza a esa misma ruta rota.
3. **La ley de datos de 2025 cambió términos:** no incluye "afiliación sindical" en la lista de datos sensibles, no define "vulneración" ni "remisión" (esas definiciones están en la Ley General para sujetos obligados) y tuvo una reforma el 14 de noviembre de 2025 (V9).
4. **La página de publicaciones del CONOCER está desactualizada** (modificada el 1 de junio de 2026; su última entrada es el EC1826). No sirve para confirmar qué se publicó después del 7 de agosto (V7).

## 1. Fuentes descargadas

Estado al final de la corrida. "Wayback" indica que el PDF se obtuvo del Archivo de Internet porque el sitio oficial devuelve 404.

| Id | URL de donde se obtuvo | Estado |
|---|---|---|
| EC1705 | conocer.gob.mx/wp-content/uploads/2025/11/EC1705.pdf | ok, 8 páginas |
| EC1804, EC1780, EC1781 | Wayback de www.conocer.gob.mx/contenido/publicaciones_dof/2026/... | ok (11, 12 y 14 páginas) |
| ECM0358 | Wayback de .../2024/segunda/ECM0358.pdf | ok, 1 página |
| EC1691, EC0554_01, EC0553_01, EC1131_01 | conocer.gob.mx/wp-content/uploads/2025/11/ | ok |
| EC0076, EC1171, EC0301, EC0217_01 | sitios de universidades, ILCE e Infoem (formato anterior N-FO-02) | ok |
| EC1827, EC1828, EC1829 | ruta del DOF (rota); Wayback | **error: no disponibles** |
| EC1657, EC1440, EC1410, EC1730 | rutas antiguas del CONOCER, Wayback y sitios externos | **error: no disponibles** |
| CONOCER_PUBLICACIONES_DOF | conocer.gob.mx/contenidos/publicaciones_dof/ | ok (la tabla se extrajo del HTML: `CONOCER_PUBLICACIONES_DOF_tabla.txt`) |
| CONOCER_INICIO | conocer.gob.mx | ok |
| CONOCER_TRANSPARENCIA_55 (manual M-DGAOSU-02, rev. 3.3, octubre de 2016) y _61 (manual COVACEC, versión 6.0, 2015) | Wayback | ok |
| CONOCER_ABC_CGC | www.conocer.gob.mx/contenido/comites/... | **error** |
| DOF_ACUERDO_SE_III_26_05R | dof.gob.mx/nota_detalle.php?codigo=5795750 (edición matutina del 7 de agosto de 2026) | ok. `DOF_2026_08_07` (índice del día) mostró la edición vespertina y quedó sustituida por esta nota |
| LFPDPPP, LFPDPPP_DOF_2025, LGPDPPSO, LFT, LFDA | diputados.gob.mx | ok. LFPDPPP y LGPDPPSO: última reforma DOF 14-11-2025; LFT: DOF 14-05-2026 |
| LEY_INFRAESTRUCTURA_CALIDAD | diputados.gob.mx/LeyesBiblio/pdf/LICal.pdf | **error** (no se usó en ninguna verificación) |
| INEGI_SCIAN, INEGI_SINCO | inegi.org.mx/app/... | ok. La estructura completa SCIAN México 2023 se descargó aparte: `INEGI_SCIAN_ESTRUCTURA_2023` |
| EU_REGLAMENTO_IA | eur-lex (CELEX:32024R1689) | ok |
| EU_REGLAMENTO_2026_1744 | eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ:L_202601744 | ok (se agregó como fuente) |
| STPS_DC3 | Acuerdo de la STPS en el DOF del 14 de junio de 2013 (nota 5302582) | ok (se agregó como `STPS_ACUERDO_2013`) |
| CONOCER_REGLAS_SNC | no se encontró el texto de las Reglas Generales | **por confirmar**; se usaron los dos manuales del CONOCER, que las citan |

**Cambios al kit:** se quitó `www.` de las URL del CONOCER; se agregaron como alternativa las URL de Wayback; el tiempo de espera por intento bajó de 90 a 40 segundos; se agregó `cryptography` a `requirements.txt` (el PDF del INEGI está cifrado); se corrigió la URL del EC1131.01; se agregaron cuatro fuentes.

## 2. Verificaciones

### V1. Frases fijas del formato

| Punto | Fuente | Texto oficial | Resultado | Archivo |
|---|---|---|---|---|
| "La persona es competente cuando demuestra los siguientes:" (desempeños) | EC1705 p. 5; EC1804 p. 6 | "La persona es competente cuando demuestra los siguientes:" | Coincide | — |
| "obtiene los siguientes" (productos) | EC1780 p. 6; EC1781 | "La persona es competente cuando obtiene los siguientes:" | Coincide | — |
| "obtiene el siguiente" (un solo producto) | Ninguno de los estándares descargados | No apareció | **Por confirmar**; se conserva por analogía con "demuestra el siguiente" | 02 (nota 2) |
| "posee los siguientes" con columna NIVEL | EC1705 p. 5 | "La persona es competente cuando posee los siguientes: CONOCIMIENTOS NIVEL" | Coincide | — |
| Situaciones emergentes | EC1781 p. 13; EC1171 p. 6 | "La persona es competente cuando demuestra las siguientes: RESPUESTAS ANTE SITUACIONES EMERGENTES / Situación emergente / Respuestas esperadas" | **Corregido.** El borrador decía "demuestra la siguiente", "RESPUESTA ANTE" y repetía "Situación emergente:" dentro del texto | 02 (2 bloques), 03 (1 bloque) |
| Actitudes: "demuestra las siguientes" | EC1705 p. 7; EC1804; EC0554_01 | "La persona es competente cuando demuestra las siguientes: ACTITUDES/HÁBITOS/VALORES" | Coincide | — |
| Singular "demuestra el siguiente" | EC1131_01 p. 5 | "La persona es competente cuando demuestra el siguiente: DESEMPEÑO" | Coincide con la regla de singular usada en el EC-A | — |
| GLOSARIO | EC1705 p. 5; EC1804; EC1780 | Encabezado "GLOSARIO" al final de cada elemento | Coincide | — |

### V2. Datos Generales y orden de campos

Formato publicado: F21-COOPYD-01, **versión 08** (EC1705, EC1780, EC1781, EC1804, EC1691 y EC1131.01). EC0553_01, EC0554_01 y EC1171 traen la versión 7.0.

| Punto | Fuente | Texto oficial | Resultado | Archivo |
|---|---|---|---|---|
| Orden: código y título; propósito; descripción general; nivel; comité; fechas; periodo de revisión; SINCO; SCIAN; texto del RENEC; organizaciones; aspectos de la evaluación; referencias | EC1781 pp. 1 a 3; EC1804 pp. 1 a 4 | Mismo orden | Coincide | — |
| Campo de empresas | EC1705 p. 2; EC1804 p. 2; EC1781 p. 2 | "Organizaciones participantes en el desarrollo del Estándar de Competencia" (el formato anterior decía "Empresas e Instituciones participantes en el desarrollo del EC") | **Corregido** | 02, 03 |
| "Relación con otros estándares de competencia" / "Estándares relacionados" | Ausente en los seis estándares de la versión 08; solo aparece en EC0301 y EC1171 (formato anterior) | — | **Corregido:** se retiró el apartado del cuerpo; la relación con el EC1705 y con el EC-A quedó en las notas | 02, 03 |
| "Tiempo de Vigencia del Certificado de competencia en este EC" | EC1781 p. 1 ("3 años"); ausente en EC1705, EC1780 y EC1804 | Campo presente solo en EC1781 | Coincide (campo nuevo de 2026, se conserva) | — |
| Detalles de la práctica, Apoyos/Requerimientos, Duración estimada | EC1781 pp. 2 y 3 | Mismos tres rubros | Coincide | — |
| Perfil y encabezado de elemento | EC1705 pp. 4 y 5 | "Referencia Código Título" | Coincide | — |
| Campos nuevos en 2026 | EC1781 | Solo "Tiempo de Vigencia del Certificado" | Señalado arriba | — |

### V3. Escala de niveles y catálogo de actitudes

| Punto | Fuente | Resultado |
|---|---|---|
| Palabras de la columna NIVEL | EC0076, EC0301, EC0553_01, EC0554_01, EC1171, EC1691, EC1705, EC1780, EC1781, EC1804 | Se usan **Conocimiento, Comprensión y Aplicación**. No aparecieron otras. Coincide con los borradores |
| Actitudes | EC1705 y EC1781 (Responsabilidad, Orden); EC1691 p. 7 (Perseverancia); EC1780 p. 9 (Iniciativa, Tolerancia); EC0554_01 (Amabilidad, Cooperación, Tolerancia) | Las seis usadas (Responsabilidad, Orden, Perseverancia, Iniciativa, Amabilidad, Tolerancia) están en estándares publicados. Coincide |

### V4. Niveles Dos y Cuatro

| Punto | Fuente | Texto oficial | Resultado |
|---|---|---|---|
| Nivel Dos | EC0554_01 p. 1; EC1804 p. 1 | "Desempeña actividades programadas que, en su mayoría, son rutinarias y predecibles. Depende de las instrucciones de un superior. Se coordina con compañeros de trabajo del mismo nivel jerárquico." | Coincide palabra por palabra (el EC1780 dice "de su mismo nivel") |
| Nivel Cuatro | ECM0358 p. 1 | "Desempeña diversas actividades tanto programadas, poco rutinarias como impredecibles que suponen la aplicación de técnicas y principios básicos. Recibe lineamientos generales de un superior. Requiere emitir orientaciones generales e instrucciones específicas a personas y equipos de trabajo subordinados. Es responsable de los resultados de las actividades de sus subordinados y del suyo propio." | Coincide palabra por palabra |
| Nivel Cuatro en EC0076, EC1410, EC1440 | EC0076 es de formato anterior y no trae el texto; EC1410 y EC1440 no se pudieron descargar | — | No comparado (queda el ECM0358 como respaldo) |

### V5. Clasificación

| Punto | Fuente | Texto oficial | Resultado |
|---|---|---|---|
| SINCO 9999 | EC1781 p. 2; EC1171 p. 2 | "9999 Ocupaciones no especificadas" / "Sin referente" | Coincide |
| SCIAN 561110 | SCIAN México 2023 (INEGI, estructura2023.pdf) | "56 Servicios de apoyo a los negocios y manejo de residuos, y servicios de remediación; 561 Servicios de apoyo a los negocios; 5611 y 56111 Servicios de administración de negocios; 561110 Servicios de administración de negocios" | Coincide. El EC1804 usa los nombres de 2018 ("y desechos") |
| SCIAN 541610 | Misma | "54; 541; 5416 Servicios de consultoría administrativa, científica y técnica; 54161 y 541610 Servicios de consultoría en administración" | Coincide |
| Precedentes | EC1705 p. 2 | Sector 61, clase 611710 | Coincide con la nota. EC1657: PDF no disponible, queda "por confirmar" |
| Códigos asignados a EC1827 a EC1829 | — | PDF no disponibles | No verificado |

Archivos: 02 (nota 3) y 03 (nota 4) actualizados.

### V6. Elemento 3 de 3 del EC1705 frente al EC-A

Fuente: EC1705 p. 8 (código del elemento E5338; el estándar es de **nivel Tres**).

| EC1705, Elemento 3 | Cita | EC-A | Relación |
|---|---|---|---|
| Desempeño 1 | "Revisando las políticas de privacidad de las herramientas de inteligencia artificial… Evitando ingresar información que comprometa la privacidad del usuario cuando las políticas de privacidad no son claras" | Elemento 1, Desempeños 1 a 4 (verificar la herramienta y la política de la organización, clasificar, depurar, ingresar) | Parcial. El EC1705 se basa en las políticas del proveedor y no pide clasificar, depurar ni registrar |
| Desempeño 2 | "Identificando la información relevante como fechas/cifras/nombres/referencias… consultando fuentes alternas y bibliografía especializada" | Elemento 2, Desempeño 1 (contrastar cada dato con al menos una fuente verificable distinta de la herramienta) | Parcial. El EC-A exige registro de verificación, revisión de derechos de terceros y declaración de uso |
| Actitud: Responsabilidad | "…procurando la integridad de la información y veracidad del contenido" | Elemento 2, actitud Responsabilidad | Afín |
| Productos y conocimientos | El Elemento 3 **no tiene** | El EC-A tiene registro de clasificación, información depurada, producto verificado, registro de verificación y reporte de incidente | Sin traslape |
| Incidentes y suplantaciones | El EC1705 no los cubre | Elemento 3 del EC-A | Sin traslape |

**Delimitación propuesta:** el EC-A se distingue por el procedimiento con registros, por cubrir incidentes y suplantaciones y por el nivel (Dos frente a Tres). Escrita en la nota 1 del 02, en el mapa funcional (01) y en el índice (00). Nota: el nivel Tres del EC1705 es mayor que el Dos del EC-A; conviene explicarlo al CONOCER.

### V7. Estándares publicados después del 7 de agosto de 2026

| Punto | Fuente | Resultado |
|---|---|---|
| DOF del 8 de agosto al 9 de octubre de 2026 (ediciones matutina y vespertina, 6 días a la semana) | Índice del DOF consultado día por día | Ningún acuerdo del CONOCER ni de estándares de competencia. Las coincidencias de "datos personales" fueron acuerdos de otros organismos sin relación |
| Página de publicaciones del CONOCER | `CONOCER_PUBLICACIONES_DOF_tabla.txt` (160 estándares) | Última entrada: EC1826; la página se modificó el 1 de junio de 2026. No sirve para este punto |
| Estándares relacionados con ciberseguridad ya publicados | Misma tabla | **EC1771** "Gestión de prácticas seguras y cultura de ciberseguridad en el entorno laboral" y **EC1801** "Gestión de la calidad en servicios de tecnologías de la información y ciberseguridad". No estaban en los documentos. Su texto no se pudo consultar. También EC1701 "Prestación de servicios de asistencia virtual ejecutiva" (público similar al del EC-A) |

Archivos: 01 (dos filas nuevas y conclusión), 00 y CLAUDE.md.

### V8. Acuerdo SE/III-26/05,R

Fuente: DOF 07/08/2026, edición matutina, nota 5795750.

| Punto | Texto oficial | Resultado |
|---|---|---|
| Fecha de aprobación | "…celebrada el 03 de julio de 2026, se aprobó el siguiente" | Coincide (CLAUDE.md, 01 y 04) |
| Estándares aprobados | 8: EC1827 "Desarrollo de productos y servicios con IA en MiPyME", EC1828 "Implementación de estrategias con Marketing, utilizando IA para la Alta Dirección en PyME's", EC1829 "Producción de videos digitales con herramientas de inteligencia artificial generativa", y ECM0400 a ECM0404 (estándares de marca sobre niñez y familia) | Coincide. Los tres de IA son EC; los otros cinco son ECM |
| Responsabilidad del contenido | "…cuyo contenido y apego a la normatividad vigente es responsabilidad exclusiva de la Institución" | Coincide con la nota 6 del 03, que ahora cita el texto |
| Plazo de aprobación a publicación | 3 de julio a 7 de agosto = 35 días | Coincide con "cinco semanas" (04) |
| Enlaces de los EC | Apuntan a `www.conocer.gob.mx/contenido/publicaciones_dof/2026/tercera_se/...`, ruta que da 404 | Los enlaces del documento 04 ahora apuntan a la nota del DOF |

### V9. Ley Federal de Protección de Datos Personales en Posesión de los Particulares

Fuente: texto vigente de diputados.gob.mx (nueva ley DOF 20-03-2025, **última reforma DOF 14-11-2025**) y Ley General (LGPDPPSO) con la misma fecha de reforma.

| Punto | Texto oficial | Resultado | Archivo |
|---|---|---|---|
| Dato personal (art. 2, V) | "Cualquier información concerniente a una persona identificada o identificable. Se considera que una persona es identificable cuando su identidad pueda determinarse directa o indirectamente a través de cualquier información" | **Corregido** (el borrador omitía la segunda oración) | 02 |
| Dato personal sensible (art. 2, VI) | "…esfera más íntima de la persona titular, o cuya utilización indebida pueda dar origen a discriminación o conlleve un riesgo grave para esta. De manera enunciativa más no limitativa… origen racial o étnico, estado de salud presente o futuro, información genética, creencias religiosas, filosóficas y morales, opiniones políticas y preferencia sexual" | **Corregido.** La lista **no incluye afiliación sindical**, que los borradores citaban | 02, 06, 10, 14 (coincidía) |
| Responsable, encargado | "Sujetos regulados…"; "Persona encargada: persona física o jurídica que sola o conjuntamente con otras trate datos personales por cuenta del responsable" | Término correcto: "persona encargada" | 12 |
| Remisión | La ley para particulares **no la define**. La Ley General (art. 3, XXIV) la define como "toda comunicación de datos personales realizada exclusivamente entre el responsable y la persona encargada" | **Corregido:** el conocimiento 1 del Elemento 2 de 4 ya no cita "remisiones"; en la guía 12 se aclaró el origen del término. Las preguntas que usan "remisión" (08, 12) y los textos de 11, 13 y 17 se conservan: **por confirmar** con un especialista si el reglamento anterior sigue aplicándose | 03, 12 |
| Transferencia | "Toda comunicación de datos personales dentro o fuera del territorio mexicano, realizada a persona distinta de la titular, del responsable o de la persona encargada del tratamiento" | Coincide | — |
| Vulneración | La ley para particulares no la define. La Ley General (art. 32) enumera: pérdida o destrucción; robo, extravío o copia; uso, acceso o tratamiento; daño, alteración o modificación no autorizados | **Corregido:** el glosario del 03 sigue esa lista, con nota de origen | 03, 12 |
| Principios (art. 5) | "licitud, finalidad, lealtad, consentimiento, calidad, proporcionalidad, información y responsabilidad" | Coincide (los ocho) | — |
| Medidas de seguridad (art. 18) | "…medidas de seguridad administrativas, técnicas y físicas…" | Coincide | — |
| Vulneraciones (art. 19) | "Las vulneraciones de seguridad… que afecten de forma significativa los derechos patrimoniales o morales de las personas titulares le serán informadas de forma inmediata por el responsable…" | Coincide. La ley **no fija un plazo en horas** | 03 (nota 6) |
| Autoridad | "Secretaría Anticorrupción y Buen Gobierno" | Coincide con 04 y 15 | — |
| Ley General para instituciones públicas | "Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados" (nueva ley DOF 20-03-2025) | Nombre exacto confirmado | — |

### V10. Ley Federal del Trabajo y DC-3

Fuente: LFT (última reforma DOF **14-05-2026**) y Acuerdo de la STPS, DOF 14-06-2013.

| Punto | Texto oficial | Resultado | Archivo |
|---|---|---|---|
| Art. 153-A | Los patrones deben proporcionar capacitación y adiestramiento; las instituciones, escuelas, organismos e instructores independientes "deberán estar autorizados y registrados por la Secretaría del Trabajo y Previsión Social" | Coincide. Se agregó el requisito de registro | 12 |
| Comisión mixta | Art. 153-E: "En las empresas que tengan más de 50 trabajadores se constituirán Comisiones Mixtas de Capacitación, Adiestramiento y Productividad" | Coincide con la pregunta 15 del 11; se agregó el artículo | 12 |
| Constancia | Art. 153-T: la entidad instructora expide las constancias, "autentificadas por la Comisión Mixta"; art. 153-V: "La constancia de competencias o de habilidades laborales es el documento con el cual el trabajador acreditará haber llevado y aprobado un curso de capacitación" | Coincide | 12 |
| Certificado de competencia en lugar del curso | Art. 153-U: quien tiene los conocimientos puede acreditarlos "mediante el correspondiente certificado de competencia laboral" o con examen de suficiencia | Dato nuevo, útil para la venta; se agregó | 12 |
| Formato DC-3 | Acuerdo 2013, art. 24 (la constancia deberá contener): nombre del curso, duración en horas, periodo, área temática (según catálogo), agente capacitador o empresa, instructor, representantes de la Comisión Mixta | Coincide con la tabla de los cursos | 09, 11 |
| Clave de área temática 8000 | El acuerdo remite el catálogo al sistema de la STPS y al reverso del formato; no está en el acuerdo. Copias del formato de terceros (Scribd, StudyLib) muestran "8000 Uso de tecnologías de la información y comunicación" | **Por confirmar** en la fuente oficial | 09, 11 |

### V11. Reglas del Sistema Nacional de Competencias

Fuentes: manual M-DGAOSU-02 (rev. 3.3, octubre de 2016) y manual N-OPCV-MT-01 (versión 6.0, 2015). **No se encontró el texto de las Reglas Generales vigentes**, y ambos manuales son anteriores a 2026; su vigencia queda por confirmar.

| Punto | Texto oficial | Resultado | Archivo |
|---|---|---|---|
| Quién acredita a las ECE y OC | Punto 4.5.1: la acreditación de un EC procede cuando la ECE/OC "sea solución de certificación aprobada por el CONOCER" | Coincide | 18 |
| Centros de Evaluación y Evaluadores Independientes | 4.6.1: la autorización "deberá realizarse por medio del sistema informático del CONOCER" si el prestador tiene acreditado un EC inscrito en el RENEC y evaluadores certificados en el EC de evaluación y en el EC (doble certificación); 4.6.3: al autorizar a una ECE se autoriza a sus CE, EI y sedes | **Corregido:** los CE y EI se autorizan por el sistema del CONOCER a solicitud de la ECE; el borrador decía "acreditados por ellos" | 04, 15, 18 |
| EC frente a ECM | 4.1.2: las ECE/OC pueden operar los "Estándares de Competencia Cerrados (ECC) o también conocidos como Estándares de Competencia de Marca (ECM)" cuando el propietario de la marca los determine como solución de certificación y así conste en un convenio con el CONOCER; 4.2.2 y 4.6.2 | **Corregido** la fila "Quién evalúa" del ECM, que estaba "no confirmado". El control sobre quién evalúa es del propietario de la marca | 18 |
| EC de uso restringido | 4.7.3: "los EC y los EC restringidos" | Se confirma la existencia del término, sin definición. Condiciones por confirmar | 18 |
| Evaluación a distancia | Los manuales no la regulan (solo mencionan una etapa "virtual" de transferencia del conocimiento) | No encontrado; se conserva la consulta al CONOCER | 04, 18 |
| Nombre del comité que valida | "Comité de Validación de los Comités de Gestión por Competencias y de los Estándares de Competencia (COVACEC)" | **Corregido** con el nombre completo | 17 |
| Certificado de un ECM | ECM0358: "Vigencia del Certificado: Indefinida"; nivel Cuatro | Dato nuevo, útil para el análisis EC o ECM | — |

### V12. Unión Europea

Fuente: Reglamento (UE) 2026/1744, DOUE L, 24.7.2026 (eur-lex).

| Punto | Texto oficial | Resultado |
|---|---|---|
| Fecha y entrada en vigor | "de 8 de julio de 2026"; "entrará en vigor a los tres días de su publicación" (publicado el 24 de julio de 2026, vigente desde el 27) | Coincide con "julio de 2026" |
| Qué cambió | El artículo 1, punto 5, sustituye el artículo 4. Nuevo texto: "Los proveedores y responsables del despliegue de sistemas de IA adoptarán medidas para apoyar la promoción de la alfabetización en materia de IA de su personal… Esta obligación no exige que los proveedores o los responsables del despliegue garanticen un nivel específico de alfabetización en materia de IA de ninguna persona en particular." Antes: "garantizar" un nivel suficiente (considerando 8 del reglamento modificatorio) | Coincide con CLAUDE.md, 01 y 04. Se agregaron las referencias exactas en 02, 03 y 04 y se sustituyó el enlace secundario por el de EUR-Lex |

## 3. Archivos modificados

| Archivo | Cambios |
|---|---|
| `Markdown/02-EC-A-borrador.md` | V1, V2, V5, V6, V9; notas 1 a 4; referencias; registro de cambios |
| `Markdown/03-EC-B-borrador.md` | V1, V2, V5, V9; conocimiento sobre remisiones; glosario; notas 4 a 6; referencias; registro de cambios |
| `Markdown/00`, `01`, `04`, `CLAUDE.md` | Casillas del índice, delimitación y enlaces, pendiente 3 |
| `Markdown/06`, `10`, `12` | Se retiró la afiliación sindical; definición literal; aclaraciones sobre remisión y vulneración; artículos de la LFT |
| `Markdown/09`, `11` | Texto sobre la DC-3 |
| `Markdown/15`, `17`, `18` | Autorización de los Centros de Evaluación, nombre del COVACEC, filas del análisis EC o ECM |
| `verificacion/` | `fuentes.json`, `descargar_fuentes.py`, `requirements.txt`, textos extraídos |

**No se modificaron** los archivos de `Word/` ni el PDF `04-Exposicion-de-motivos-con-diagramas.pdf`: siguen con el texto anterior. Hay que regenerarlos desde los Markdown.

## 4. Por confirmar

| Tema | Por qué |
|---|---|
| Texto de EC1827, EC1828, EC1829, EC1657, EC1440, EC1410, EC1730 | Los PDF ya no están publicados en conocer.gob.mx ni en Wayback. Pedirlos al CONOCER |
| Estándares posteriores al 7 de agosto de 2026 | El DOF no muestra nuevos acuerdos; la página del CONOCER no se actualiza desde junio |
| EC1771, EC1801 y EC1701 | Se detectaron solo por título |
| Frase "obtiene el siguiente" | No apareció en ningún estándar descargado |
| Clave 8000 de la DC-3 | Solo en copias de terceros |
| Vigencia de los manuales de 2015 y 2016; texto de las Reglas Generales; EC restringidos; evaluación a distancia | Preguntar al CONOCER |
| Reglamento anterior de la ley de datos y el término "remisión" | Revisión de un abogado |
| Plantilla vigente | Confirmar que sigue la versión 08 del F21-COOPYD-01 |
| Revisión jurídica de todo el material | Ninguna de estas verificaciones sustituye la opinión de un especialista |
