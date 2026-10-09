# Evaluación de riesgo legal del proyecto

**Fecha:** 9 de octubre de 2026.
**Objeto:** los riesgos legales de la empresa como **desarrolladora** de los estándares, **centro de evaluación**, **capacitadora** y **consultora**, con los documentos 02 a 18 tal como están hoy.
**Base:** la revisión de congruencia jurídica (`verificacion/REVISION-JURIDICA.md`) y los textos oficiales de `verificacion/textos/`. Los identificadores entre paréntesis (T1, 15-3, etc.) remiten a esa revisión.
**Naturaleza:** priorización para decidir qué atender primero. No es un dictamen jurídico.

---

## 1. Método

**Probabilidad**, en los próximos 12 meses, si no se hace nada:

| Valor | Criterio |
|---|---|
| 1 Baja | Requiere una combinación poco común de hechos |
| 2 Media | Puede ocurrir con la operación prevista (piloto, convenios, cursos) |
| 3 Alta | Ocurrirá con la operación prevista, o ya está en los documentos que se usarán |

**Impacto:**

| Valor | Criterio |
|---|---|
| 1 Menor | Corrección de documentos o retrabajo interno |
| 2 Moderado | Multa baja, reclamo de un cliente o de una persona, retraso de un convenio o del piloto |
| 3 Grave | Multa alta, nulidad de un acto, inhabilitación o suspensión, pérdida de una acreditación, de un mercado o daño serio a la relación con el CONOCER |

**Nivel** = probabilidad × impacto. **Alto:** 6 a 9. **Medio:** 3 o 4. **Bajo:** 1 o 2.

Las multas se expresan en veces la Unidad de Medida y Actualización (UMA); no se convirtieron a pesos porque el valor de 2026 no se verificó en fuente oficial.

---

## 2. Mapa de calor

| Probabilidad \ Impacto | 1 Menor | 2 Moderado | 3 Grave |
|---|---|---|---|
| **3 Alta** | — | R08, R09 | **R01** |
| **2 Media** | R13, R19 | R06, R10, R16, R18 | **R02, R03, R04, R05, R07** |
| **1 Baja** | — | R12, R17, R20, R21 | R11, R14, R15 |

**Riesgos altos:** R01 a R05, R07, R08 y R09. **Medios:** R06, R10, R11, R14, R15, R16 y R18. **Bajos:** R12, R13, R17, R19, R20 y R21.

---

## 3. Registro de riesgos

| ID | Papel | Riesgo y escenario | Fundamento y consecuencia | P | I | Nivel | Controles que ya existen | Tratamiento y acciones | Residual |
|---|---|---|---|---|---|---|---|---|---|
| **R01** | Centro de evaluación, capacitadora y consultora | **Tratar datos sin aviso de privacidad.** En la piloto se recaban nombre, CURP, contacto, evidencias y resultados de candidatos y participantes, y datos de entrevistados del diagnóstico. El consentimiento del piloto remite a un aviso que no existe (T1) | LFPDPPP arts. 14, 15, 16 y 29. Infracción del art. 58, V ("Omitir en el aviso de privacidad… elementos"), con multa de 100 a 160,000 UMA (art. 59, II); hasta el doble si hay datos sensibles | 3 | 3 | **9** | Minimización (piloto, 6.4); consentimiento escrito (piloto, anexo 1) | **Reducir.** Redactar el aviso integral y el simplificado (candidatos, participantes, clientes y entrevistados); designar el departamento de datos (art. 29); fijar plazos de conservación de evidencias. **Antes de iniciar la piloto** | Bajo |
| **R02** | Centro de evaluación | **Transferir datos al CONOCER y a la ECE sin cláusula en el aviso** al gestionar certificados. El convenio presenta las "reglas del CONOCER" como fundamento (15-5) | LFPDPPP art. 35 (cláusula de aceptación de la transferencia) y art. 36, IV y VII. Infracciones del art. 58, X y XII, con multa de 200 a 320,000 UMA (art. 59, III) | 2 | 3 | **6** | Registro directo con la empresa (convenio, NOVENA.2) | **Reducir.** Incluir en el aviso la cláusula de transferencias y su fundamento; corregir el anexo D del convenio. **Antes de la primera evaluación con certificado** | Bajo |
| **R03** | Consultora | **La plantilla de política lleva al cliente a tratar datos sensibles sin consentimiento.** La plantilla los admite con autorización interna (14-2). Si el cliente la aplica y lo sancionan, puede reclamar a la empresa | LFPDPPP art. 8 ("consentimiento expreso y por escrito"); art. 58, XIII (infracción del cliente). Responsabilidad contractual de la consultora frente al cliente | 2 | 3 | **6** | Advertencia de "no constituye asesoría jurídica" y recomendación de revisión jurídica (plantilla, encabezado) | **Reducir.** Corregir 14-1 a 14-4 y T7 antes de entregar la plantilla a cualquier cliente | Bajo |
| **R04** | Capacitadora y centro de evaluación | **Convenio con una institución pública que paga los servicios.** Se elige la opción "LA INSTITUCIÓN paga" de la cláusula QUINTA. El acto puede considerarse una evasión de la normatividad de adquisiciones: la institución no paga, el convenio se anula o se finca responsabilidad (T2) | LAASSP art. 1: las dependencias y entidades "se abstendrán de… celebrar actos o cualquier tipo de contratos, que evadan lo previsto en este ordenamiento". Para la empresa: cobro incierto y posible inhabilitación si se le vincula a una falta (LGRA arts. 65 y 81, II) | 2 | 3 | **6** | Nota preliminar del convenio que advierte la normatividad de adquisiciones | **Evitar.** En instituciones públicas, firmar convenios solo con el esquema "cada participante paga"; si la institución paga, seguir el procedimiento de contratación aplicable. **Antes de firmar el primer convenio público** | Bajo |
| **R05** | Capacitadora y centro de evaluación | **Requisito de egreso de pago en una institución pública.** Una universidad pública establece la certificación como requisito obligatorio para egresar y el estudiante paga a la empresa. Pueden seguir quejas, impugnaciones y la revocación del requisito, con daño al canal universitario (T3) | CPEUM art. 3, IV ("Toda la educación que el Estado imparta será gratuita"); LGES art. 6, VIII (eliminar cobros por "cuotas escolares ordinarias") | 2 | 3 | **6** | El convenio reconoce que la institución decide (SEGUNDA, último párrafo; nota 2) | **Reducir.** Ofrecerlo como opción voluntaria de titulación o con costo cubierto por la institución; obtener dictamen por subsistema. **Antes de proponer el requisito a cualquier institución pública** | Medio (depende del dictamen) |
| **R06** | Capacitadora y centro de evaluación | **Uso de instalaciones públicas para un servicio que cobra la empresa**, sin autorización ni contraprestación (15-3) | LGRA art. 71 (uso indebido de recursos públicos por particulares); sanciones del art. 81, II (personas morales: multa de 1,000 a 1,500,000 UMA, inhabilitación de 3 meses a 10 años, suspensión de actividades de 3 meses a 3 años) | 2 | 2 | 4 | Ninguno específico | **Reducir.** Pactar el uso de instalaciones conforme a las disposiciones de la institución (autorización o contraprestación) | Bajo |
| **R07** | Desarrolladora | **Percepción de influencia indebida por la relación con la titular del CONOCER.** La estrategia se apoya en esa relación, y la empresa es a la vez desarrolladora y primer centro evaluador. Un competidor o un órgano de control puede cuestionar la aprobación o la acreditación | LGRA art. 58 (la persona servidora pública debe solicitar ser excusada si tiene conflicto de interés); art. 68 (tráfico de influencias de particulares); arts. 65 y 81 (faltas graves y sus sanciones) | 2 | 3 | **6** | Cláusula de integridad del convenio (DÉCIMA OCTAVA); carta de conflicto de interés del grupo técnico (17, 3.4) | **Reducir.** Tratar con el CONOCER solo por canales formales (oficio y minuta); que el CGC, no la empresa, presente los estándares; no ofrecer beneficios; documentar las interacciones (17-3) | Bajo |
| **R08** | Capacitadora | **Expedir DC-3 sin registro como agente capacitador o a personas sin patrón.** Los cursos 09 y 11 la ofrecen a "quien aprueba el curso", incluidos estudiantes (T6). Las constancias carecerían de validez, con reclamos de clientes y de participantes | LFT art. 153-A ("deberán estar autorizados y registrados por la Secretaría del Trabajo y Previsión Social"); Acuerdo STPS 2013, arts. 24 y 25 | 3 | 2 | **6** | Los cursos marcan el registro "por tramitar o confirmar" | **Reducir.** Tramitar el registro; expedir DC-3 solo a personas trabajadoras dentro del plan de su patrón; constancia de participación para los demás; ninguna constancia con logotipos que sugieran aval de la STPS. **Antes del primer curso con DC-3** | Bajo |
| **R09** | Desarrolladora y capacitadora | **Titularidad débil de los materiales**, que el documento 18 presenta como la principal protección comercial. No hay cesiones de empleados, consultores ni del grupo técnico, y parte del texto se elaboró con apoyo de IA (T9) | LFDA art. 84 (sin pacto, derechos divididos por partes iguales con el empleado; sin contrato escrito, son del empleado); art. 30 (transmisión "onerosa y temporal" y por escrito, o nula); art. 12 ("Autor es la persona física…") | 3 | 2 | **6** | Licencia limitada en el convenio (DÉCIMA PRIMERA); confidencialidad del grupo técnico | **Reducir.** Firmar cesiones escritas y onerosas; documentar la autoría y la revisión humana; registrar las obras ante INDAUTOR y las marcas ante el IMPI; proteger instrumentos y claves como secreto industrial (LFPPI art. 163) | Bajo |
| **R10** | Centro de evaluación | **Filtración de instrumentos o claves de evaluación**, que invalida versiones del examen y abre reclamos | LFPPI art. 163 (la protección como secreto industrial requiere "medios o sistemas suficientes para preservar su confidencialidad") | 2 | 2 | 4 | Documentos 05 y 07 marcados como confidenciales; carta de confidencialidad (17); separación de instructores y evaluadores | **Reducir.** Acceso por necesidad, registro de accesos, cláusulas con evaluadores, versiones paralelas (pendiente del índice) | Bajo |
| **R11** | Centro de evaluación | **Pérdida o suspensión de la autorización** por evaluar a personas a quienes el mismo personal capacitó | M-DGAOSU-02, página 103: "revisar que el personal que capacita, no evalúe en el mismo proceso de la misma candidata o candidato" (vigencia por confirmar) | 1 | 3 | 3 | Convenio, SÉPTIMA.2; reglas de integridad de 09 y 11 | **Aceptar con monitoreo.** Registrar por persona quién la capacitó y quién la evaluó | Bajo |
| **R12** | Capacitadora y consultora | **Publicidad engañosa**: afirmar obligatoriedad, empleo o cumplimiento garantizado | LFPC art. 32: la publicidad "deberán ser veraces, comprobables, claros y exentos de… descripciones que induzcan o puedan inducir a error" | 1 | 2 | 2 | Mensajes permitidos y prohibidos (09, 11, 13 y 15) | **Aceptar con monitoreo.** Revisar la publicidad antes de publicarla; agregar términos y condiciones, cancelaciones y reembolsos para personas que pagan | Bajo |
| **R13** | Centro de evaluación | **Impugnación de un juicio de competencia** por reactivos con base jurídica incierta (por ejemplo, "remisión") o desactualizada | LFPDPPP 2025 sin la figura; RLFPDPPP art. 2, IX (vigencia por confirmar) (T5) | 2 | 1 | 2 | Análisis de reactivos previsto en la piloto (16, sección 4) | **Reducir.** Reformular el reactivo 8 del documento 08 y revisar las claves con el abogado | Bajo |
| **R14** | Consultora | **El cliente discrimina** al seguir la salvedad "si la finalidad lo justifica" de la plantilla o de la guía del EC-B (T8) | LFT art. 133, I; LFPED; LFPDPPP art. 8 | 1 | 3 | 3 | Intervención humana y evaluación de impacto (14, sección 9) | **Reducir.** Limitar la salvedad a obligaciones legales o acciones afirmativas documentadas | Bajo |
| **R15** | Capacitadora y consultora | **Subcontratación prohibida o falta de registro de servicios especializados** cuando el personal de la empresa presta servicios en las instalaciones del cliente o de la institución, dentro de la actividad de esta (15-10) | LFT art. 12 (prohibición), art. 13 (servicios especializados con registro) y art. 14 (responsabilidad solidaria) | 1 | 3 | 3 | Cláusula de relación laboral del convenio (DÉCIMA TERCERA) | **Transferir y reducir.** Dictamen laboral; en su caso, registro de servicios especializados (art. 15) y contratos que precisen el servicio y el personal | Por confirmar |
| **R16** | Consultora | **Reclamación por recomendaciones del diagnóstico o por datos del cliente**, sin contrato de servicios ni límite de responsabilidad (13-4) | CCF: responsabilidad contractual y daño moral (art. 1916). Si la consultora usa datos del cliente para fines propios, asume el carácter de responsable (RLFPDPPP art. 53, I) | 2 | 2 | 4 | Exclusión de opinión jurídica (13, sección 1); contrato de encargo previsto (13, sección 10) | **Reducir.** Contrato de servicios profesionales con alcance, entregables, límite de responsabilidad y encargo de datos | Bajo |
| **R17** | Desarrolladora | **Responsabilidad por el contenido de los estándares** ante quejas por un criterio contrario a la ley | Acuerdo SE/III-26/05,R: el contenido "es responsabilidad exclusiva de la Institución" | 1 | 2 | 2 | Verificación del 9 de octubre de 2026 y esta revisión jurídica | **Reducir.** Dictamen de un abogado antes de presentar los estándares; minutas del grupo técnico | Bajo |
| **R18** | Capacitadora y centro de evaluación | **Menores de edad** (bachillerato) sin el consentimiento de su madre, padre o tutor (09-3, 15-7) | LGPDPPSO arts. 7 y 14 (instituciones públicas); legislación civil aplicable | 2 | 2 | 4 | Ninguno | **Reducir.** Prever el consentimiento del representante en el aviso y el convenio; confirmar con el CONOCER la edad mínima para certificarse | Bajo |
| **R19** | Desarrolladora y capacitadora | **Materiales desactualizados**: los documentos 04 y 10 no reflejan la reforma a la LFDA de mayo de 2026 (T4) | LFDA art. 87 (DOF 14-05-2026) | 2 | 1 | 2 | Revisión de la ley prevista cada dos años en los estándares | **Reducir.** Corregir 04 y 10; revisar la normatividad cada semestre | Bajo |
| **R20** | Centro de evaluación | **Grabación de evaluaciones a distancia** sin aviso específico (05-2, 16-3) | LFPDPPP arts. 14, 15 y 18 | 1 | 2 | 2 | Sujeta a autorización del CONOCER | **Reducir.** Aviso específico y aceptación previa; plazo de conservación | Bajo |
| **R21** | Consultora | **Monitoreo desproporcionado del personal del cliente** a partir de la plantilla (registros técnicos sin límite) (14-4) | CPEUM art. 16; LFT art. 330-I; LFPDPPP art. 12 | 1 | 2 | 2 | El diagnóstico usa registros agregados, sin contenido ni identificación (13, sección 5) | **Reducir.** Corregir el punto 10.3 de la plantilla | Bajo |

P: probabilidad. I: impacto. Residual: nivel esperado después de aplicar las acciones.

---

## 4. Plan de tratamiento por momento del proyecto

| Momento | Riesgos | Acciones | Quién |
|---|---|---|---|
| **Antes de iniciar la prueba piloto** (semanas 1 y 2 del plan del documento 16) | R01, R02, R18, R20 | Aviso de privacidad integral y simplificado; departamento de datos; cláusula de transferencias; consentimiento de representantes de menores; reglas para grabaciones | Socio responsable del proyecto y abogado |
| **Antes de entregar la plantilla o el diagnóstico a un cliente** | R03, R14, R16, R21 | Corregir la plantilla de política (14-1 a 14-5); contrato de servicios profesionales y de encargo de datos | Consultor líder y abogado |
| **Antes del primer curso con DC-3** | R08 | Registro como agente capacitador externo ante la STPS; reglas de expedición | Coordinación de capacitación |
| **Antes de firmar convenios con instituciones públicas** | R04, R05, R06, R07 | Dictamen por tipo de institución; convenio solo con pago directo del participante; requisito de egreso voluntario o sin costo; uso de instalaciones pactado; canales formales con el CONOCER | Socio responsable y abogado |
| **Antes de presentar los estándares al CONOCER** | R07, R09, R13, R17, R19 | Cesiones de derechos; registro de obras y marcas; corrección de reactivos y de los documentos 04 y 10; dictamen sobre el contenido | Desarrolladora y abogado |
| **Antes de la operación comercial** | R10, R11, R12, R15 | Control de acceso a instrumentos; registro de quién capacita y quién evalúa; términos y condiciones; dictamen laboral sobre servicios especializados | Centro de evaluación y abogado |

---

## 5. Lectura para los socios

1. **El riesgo más probable no viene de la IA, sino de los datos personales del propio negocio.** Sin aviso de privacidad, la piloto y la operación del centro de evaluación incumplen la ley desde el primer registro (R01 y R02). Corregirlo cuesta poco y elimina el riesgo más alto.
2. **El canal universitario público necesita un diseño jurídico propio.** El pago lo debe hacer la persona, no la institución (salvo contratación formal). El requisito de egreso debe ser voluntario o sin costo para el estudiante, y el uso de las instalaciones debe estar autorizado (R04 a R06).
3. **La relación con el CONOCER es un activo que debe manejarse con formalidad.** Llevarla por canales oficiales protege a la empresa y a la servidora pública (R07).
4. **La protección comercial que plantea el documento 18 depende de la titularidad de los materiales**, y hoy no está asegurada (R09).
5. **Los riesgos de la consultoría se trasladan al cliente y regresan como reclamación.** Por eso la plantilla de política debe corregirse antes de entregarse (R03).

---

## 6. Supuestos y límites

- La probabilidad y el impacto son juicios de priorización, no estimaciones actuariales.
- Se tomó como vigente el texto de las leyes descargadas el 9 de octubre de 2026. Siguen por confirmar: la aplicación del reglamento de 2011 de la ley de datos, la vigencia de los manuales del CONOCER de 2015 y 2016 y el texto de las Reglas Generales del Sistema Nacional de Competencias.
- No se evaluaron riesgos fiscales, de competencia económica ni de normatividad estatal (leyes de datos y de adquisiciones de cada entidad, y normatividad de universidades autónomas), que dependen de cada institución y cliente.
- Los temas que requieren dictamen de un abogado mexicano están en la sección 6 de `REVISION-JURIDICA.md`.

---

## 7. Estado del tratamiento (9 de octubre de 2026)

Ya se aplicaron en los documentos las acciones que dependían de su redacción:

- R01 y R02: avisos de privacidad, documento 19.
- R03, R14 y R21: plantilla de política, documento 14.
- R04 a R06: convenio, documento 15.
- R07: canales formales, documento 17.
- R08: reglas de la DC-3, documentos 09, 11, 14 y 15.
- R09: modelo de cesión y notas de titularidad, documentos 17, 18 y 20.
- R12 y R16: contrato de servicios y términos para participantes, documento 20.
- R13: reactivo 8 del documento 08.
- R18: menores de edad, documentos 09, 15, 16 y 19.
- R19: reforma de la LFDA, documentos 04, 10 y 14.
- R20: grabaciones, documentos 05, 07, 16 y 19.

Las acciones que requieren actos de la empresa siguen pendientes y conservan su nivel hasta que se realicen:

- Publicar los avisos y designar el departamento de datos personales.
- Registrarse ante la STPS como agente capacitador externo.
- Firmar las cesiones y registrar obras y marcas.
- Obtener el dictamen del abogado.
- Aplicar los controles de acceso a los instrumentos de evaluación.
