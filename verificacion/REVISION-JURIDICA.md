# Revisión de congruencia jurídica de los documentos 02 a 18

**Fecha:** 9 de octubre de 2026.
**Alcance:** documentos 02 a 18 de `estandares-ia/`, revisados contra el derecho mexicano vigente. No se editó ningún documento.
**Naturaleza:** revisión técnica de congruencia con textos oficiales. **No es un dictamen jurídico** ni sustituye la opinión de un abogado mexicano (sección 6).

**Método.** Para cada documento se verificó:

1. Que las definiciones, principios, figuras y artículos citados coincidan con el texto vigente.
2. Que el tratamiento de datos tenga fundamento y aviso de privacidad.
3. Que nada exija algo contrario a la ley.
4. Que nada prometa una obligatoriedad legal inexistente.
5. Los riesgos para la empresa en sus cuatro papeles.

Se aplicaron los enfoques de revisión de contratos, evaluación de riesgo legal, brechas regulatorias, encargo de datos personales, políticas y proveedores de IA. Los skills con esos nombres no estaban instalados en la sesión, así que se siguieron sus criterios de forma manual.

**Gravedad:**

- **Alta:** contraviene la ley, puede anular un acto o exponer a sanción; corregir antes de usar el documento.
- **Media:** impreciso o incompleto frente a la ley; puede inducir a error o dejar un hueco de cumplimiento.
- **Baja:** precisión, actualización o buena práctica.

---

## 1. Fuentes oficiales consultadas

Textos en `verificacion/textos/`, descargados de la Cámara de Diputados, el DOF, el CONOCER (manuales vía Wayback) y EUR-Lex.

| Abreviatura | Ordenamiento | Versión revisada | Archivo |
|---|---|---|---|
| LFPDPPP | Ley Federal de Protección de Datos Personales en Posesión de los Particulares | Nueva ley DOF 20-03-2025; última reforma DOF 14-11-2025 | `LFPDPPP.txt` |
| RLFPDPPP | Reglamento de la LFPDPPP | DOF 21-12-2011. La Cámara de Diputados lo publica como "texto vigente", aunque reglamenta la ley de 2010, abrogada. **Su aplicación a la ley de 2025 está por confirmar** | `REG_LFPDPPP.txt` |
| LGPDPPSO | Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados | Nueva ley DOF 20-03-2025; última reforma DOF 14-11-2025 | `LGPDPPSO.txt` |
| LFT | Ley Federal del Trabajo | Última reforma DOF 14-05-2026 | `LFT.txt` |
| Acuerdo STPS 2013 | Acuerdo por el que se dan a conocer los criterios administrativos, requisitos y formatos en materia de capacitación (DC-3, DC-4) | DOF 14-06-2013 | `STPS_ACUERDO_2013.txt` |
| LFDA | Ley Federal del Derecho de Autor | Última reforma DOF 14-05-2026 (reforma en materia de IA, imagen y voz) | `LFDA.txt` |
| LFPPI | Ley Federal de Protección a la Propiedad Industrial | Última reforma DOF 03-04-2026 | `LFPPI.txt` |
| CCF | Código Civil Federal | Última reforma DOF 14-11-2025 | `CCF.txt` |
| LICal | Ley de Infraestructura de la Calidad | DOF 01-07-2020 | `LEY_INFRAESTRUCTURA_CALIDAD.txt` |
| LAASSP | Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público | Nueva ley DOF 16-04-2025 | `LAASSP.txt` |
| LGES | Ley General de Educación Superior | DOF 20-04-2021 | `LGES.txt` |
| LGE | Ley General de Educación | Última reforma DOF 15-01-2026 | `LGE.txt` |
| LFPC | Ley Federal de Protección al Consumidor | Última reforma DOF 12-12-2025 | `LFPC.txt` |
| LFPED | Ley Federal para Prevenir y Eliminar la Discriminación | Última reforma DOF 14-11-2025 | `LFPED.txt` |
| LGRA | Ley General de Responsabilidades Administrativas | Última reforma DOF 15-12-2025 | `LGRA.txt` |
| CPEUM | Constitución Política de los Estados Unidos Mexicanos | Última reforma DOF 07-10-2026 | `CPEUM.txt` |
| M-DGAOSU-02 | Manual del CONOCER para la operación de ECE/OC y prestadores | Revisión 3.3, octubre de 2016 (vigencia por confirmar) | `CONOCER_TRANSPARENCIA_55.txt` |
| Acuerdo SE/III-26/05,R | Acuerdo del Comité Técnico del CONOCER | DOF 07-08-2026 | `DOF_ACUERDO_SE_III_26_05R.txt` |
| Reglamento (UE) 2026/1744 | Ómnibus digital sobre IA | DOUE 24-07-2026 | `EU_REGLAMENTO_2026_1744_ES.txt` |

**No se localizaron en texto oficial:**

- Las Reglas Generales y Criterios para la Integración y Operación del Sistema Nacional de Competencias (DOF 27-11-2009), citadas por el propio CONOCER.
- El catálogo oficial de áreas temáticas de la DC-3.
- Los lineamientos del aviso de privacidad para la ley de 2025.

---

## 2. Resumen

**Lo que está bien:**

- **Obligatoriedad.** Ningún documento promete que la certificación sea obligatoria por ley. Hay cláusulas y guías expresas que lo prohíben: 09 (5), 11 (4), 13 (sección 12) y 15 (DÉCIMA SEGUNDA).
- **Figuras y artículos.** Los principios (art. 5), las medidas de seguridad (art. 18) y el deber de informar vulneraciones (art. 19 LFPDPPP), así como los artículos 153-A, 153-E, 153-T, 153-U y 153-V de la LFT, coinciden con el texto vigente.
- **Separación entre capacitación y evaluación.** La cláusula SÉPTIMA del convenio coincide con la regla del CONOCER: "revisar que el personal que capacita, no evalúe en el mismo proceso de la misma candidata o candidato" (M-DGAOSU-02, página 103).

**Hallazgos principales** (detalle en las secciones 3 y 4):

| # | Hallazgo | Documentos | Gravedad |
|---|---|---|---|
| T1 | No existe un aviso de privacidad para candidatos, participantes, entrevistados y clientes, y los documentos se apoyan en él como si existiera | 05 a 13, 15, 16, 17 | Alta |
| T2 | El convenio permite que una institución pública pague los servicios mediante un convenio de colaboración, lo que puede evadir la normatividad de adquisiciones | 15 | Alta |
| T3 | El modelo de "requisito de egreso" de pago en instituciones públicas puede chocar con el principio de gratuidad | 15, 17, CLAUDE.md | Alta |
| T4 | El artículo 87 de la LFDA se reformó (DOF 14-05-2026). Hoy protege la imagen y la voz de artistas intérpretes y ejecutantes, incluidos los resultados de IA. Los documentos dicen que la LFDA "protege el retrato de las personas" en general | 04, 10 | Media |
| T5 | "Remisión" y la lista de vulneraciones vienen del reglamento de 2011 (y de la LGPDPPSO). La ley de 2025 para particulares no los define. Hay reactivos de examen que dependen de ese término | 03, 08, 11, 12, 13, 17 | Media |
| T6 | La constancia DC-3 es para trabajadores dentro del plan de capacitación de su patrón. Los documentos la ofrecen a "quien aprueba el curso", incluidos estudiantes | 09, 11, 15 | Media |
| T7 | Ningún documento establece que el tratamiento de datos de proveedores de IA debe formalizarse como encargo (contrato) o como transferencia (con aviso y, en su caso, consentimiento) | 03, 13, 14 | Media |
| T8 | La política y la guía del EC-B permiten usar variables discriminatorias "si la finalidad lo justifica" | 12, 14 | Media |
| T9 | La titularidad de los materiales de la empresa no está asegurada. Se presume una división 50/50 de derechos con empleados sin pacto escrito, la transmisión de derechos debe ser escrita y onerosa, y la autoría humana es requisito frente a materiales elaborados con apoyo de IA | 15, 17, 18 | Media |

---

## 3. Verificación de figuras y artículos citados

| Figura o artículo | Texto vigente (cita breve) | Cómo lo usan los documentos | Resultado |
|---|---|---|---|
| Dato personal (LFPDPPP art. 2, V) | "Cualquier información concerniente a una persona identificada o identificable. Se considera que una persona es identificable cuando su identidad pueda determinarse directa o indirectamente…" | 02 (literal desde el 9-10-2026); 14 (solo la primera oración) | Coincide en 02; incompleto en 14 |
| Dato personal sensible (art. 2, VI) | "…origen racial o étnico, estado de salud presente o futuro, información genética, creencias religiosas, filosóficas y morales, opiniones políticas y preferencia sexual". No incluye afiliación sindical (la LGPDPPSO, art. 3, X, tampoco) | 02, 06, 10 (corregidos); 14 (redacción anterior, lista incompleta) | Corregir 14 |
| Responsable (art. 2, XIV y XVI) | "Sujetos regulados…": "Personas físicas o morales de carácter privado que llevan a cabo el tratamiento de datos personales" | 12, 14, 15 | Coincide |
| Persona encargada (art. 2, XII) | "Persona física o jurídica que sola o conjuntamente con otras trate datos personales por cuenta del responsable" | 12 y 13 dicen "encargado" o "encargada" | Coincide en sustancia; usar "persona encargada" |
| Remisión | La LFPDPPP 2025 no la define. RLFPDPPP art. 2, IX: "La comunicación de datos personales entre el responsable y el encargado…". LGPDPPSO art. 3, XXIV: "…exclusivamente entre el responsable y la persona encargada…" | 03 (corregido), 08 (reactivo 8), 11 (2.1), 12 (nota agregada), 13 (9.4), 17 (perfil) | Por confirmar: depende de la aplicación del reglamento de 2011 |
| Transferencia (art. 2, XX) | "Toda comunicación de datos personales… realizada a persona distinta de la titular, del responsable o de la persona encargada" | 12, 14 (anexo 5), 15 (anexo D) | Coincide |
| Vulneración | La LFPDPPP 2025 no la define. RLFPDPPP art. 63 y LGPDPPSO art. 32: pérdida o destrucción; robo, extravío o copia; uso, acceso o tratamiento; daño, alteración o modificación no autorizados | 03 (glosario), 07, 12 | Coincide con el reglamento y la ley general; fundamento por confirmar para particulares |
| Principios (art. 5) | "licitud, finalidad, lealtad, consentimiento, calidad, proporcionalidad, información y responsabilidad" | 03, 10, 12, 06 (reactivo 4), 08 (reactivo 7) | Coincide |
| Medidas de seguridad (art. 18) | "…administrativas, técnicas y físicas que permitan proteger los datos personales contra daño, pérdida, alteración, destrucción o el uso, acceso o tratamiento no autorizado" | 04, 06 (reactivo 3), 10, 13 | Coincide |
| Aviso de vulneraciones (art. 19) | "…que afecten de forma significativa los derechos patrimoniales o morales de las personas titulares le serán informadas de forma inmediata por el responsable…" | 03, 04, 08 (reactivo 25), 12 | Coincide. No hay plazo en horas |
| Decisiones automatizadas (art. 26, II) | Derecho de oposición cuando un tratamiento automatizado "le produzca efectos jurídicos no deseados… y estén destinados a evaluar, sin intervención humana…" | No se cita; es el fundamento de la intervención humana de 03, 12 y 14 | Citar como fundamento |
| Encargado (RLFPDPPP arts. 49 a 51; LGPDPPSO arts. 52 a 58) | RLFPDPPP art. 51: "La relación entre el responsable y el encargado deberá estar establecida mediante cláusulas contractuales u otro instrumento jurídico…" | 13 (sección 10) | Coincide; fundamento por confirmar para particulares |
| LFT art. 153-A | Obligación de capacitar. Los agentes externos "deberán estar autorizados y registrados por la Secretaría del Trabajo y Previsión Social" | 04, 08, 11, 12, 14, 15 | Coincide |
| LFT art. 153-E | "En las empresas que tengan más de 50 trabajadores se constituirán Comisiones Mixtas…" | 11 (reactivo 15), 12 | Coincide |
| LFT arts. 153-T y 153-V | La entidad instructora expide las constancias, "autentificadas por la Comisión Mixta"; la constancia acredita "haber llevado y aprobado un curso de capacitación" | 08 (reactivo 22), 09, 11, 12 | Coincide; alcance por precisar (T6) |
| LFDA art. 87 (reforma DOF 14-05-2026) | "La imagen, incluida la voz, de las personas artistas intérpretes o ejecutantes… sólo puede ser usada o publicada, con su consentimiento expreso… La protección… abarca los resultados generados por sistemas de inteligencia artificial…" | 04 y 10: "protege el retrato de las personas" | Desactualizado (T4) |
| CCF art. 1916 | Daño moral: "afectación… en sus sentimientos, afectos, creencias, decoro, honor, reputación, vida privada, configuración y aspecto físicos…" | No se cita | Fundamento general para la imagen de cualquier persona |
| Reglamento (UE) 2026/1744 | El art. 4 se sustituye: "adoptarán medidas para apoyar la promoción de la alfabetización…"; "no exige… un nivel específico" | 02, 03, 04, 13 | Coincide |
| Acuerdo SE/III-26/05,R | "…cuyo contenido y apego a la normatividad vigente es responsabilidad exclusiva de la Institución" | 03 (nota 6) | Coincide |

---

## 4. Hallazgos por documento

Formato de cada tabla: ubicación · texto actual · problema · fundamento (ley, artículo y cita literal breve) · gravedad · redacción propuesta.

### 4.0 Hallazgos transversales

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| T1 | 15 (NOVENA.2 y anexo D), 16 (anexo 1, punto 5), 13 (sección 10), 05 a 12 (evaluaciones y cursos) | "…les da a conocer su aviso de privacidad"; "conforme al aviso de privacidad de [empresa], que recibí" | No hay un aviso de privacidad de la empresa. Hacen falta tres: (a) candidatos a evaluación, (b) participantes de cursos (incluidos datos para la DC-3) y (c) clientes y entrevistados del diagnóstico. Falta también la designación de la persona o el departamento de datos | LFPDPPP art. 15: el aviso "deberá contener, al menos…" identidad, datos (sensibles), finalidades, opciones para limitar, medios ARCO y cambios. Art. 16, II: modalidad simplificada en medios electrónicos. Art. 35: cláusula sobre transferencias. Art. 29: "designará a una persona, o departamento de datos personales". Art. 58, V (infracción) y art. 59, II (multa de 100 a 160,000 UMA) | Alta | Elaborar el "Aviso de privacidad integral y simplificado de [empresa]" con: finalidades primarias (inscripción, curso, evaluación, juicio de competencia, gestión del certificado ante el CONOCER y la ECE, DC-3 y listas DC-4) y secundarias (promoción, con opción de negarse); datos (nombre, CURP, contacto, evidencias de evaluación; ningún dato sensible salvo ajustes razonables por discapacidad, con consentimiento expreso y por escrito, art. 8); transferencias (ECE, CONOCER y patrón para la DC-3) con su fundamento (art. 36, IV y VII) y cláusula de aceptación; conservación; medios ARCO y revocación (art. 7); departamento de datos (art. 29) |
| T2 | 15 (QUINTA y anexo B; nota preliminar) | "[Elegir: … / LA INSTITUCIÓN paga por los participantes que inscriba / esquema mixto]" | Cuando una dependencia o entidad federal paga un servicio, la vía es un contrato conforme a la LAASSP, no un convenio de colaboración. La nota preliminar lo advierte, pero la cláusula ofrece la opción | LAASSP art. 1: aplica a dependencias y organismos descentralizados, y "Las dependencias y entidades se abstendrán de… celebrar actos o cualquier tipo de contratos, que evadan lo previsto en este ordenamiento". Universidades autónomas: su propia normatividad, y la LAASSP "sólo en lo no previsto" | Alta | Para instituciones públicas, limitar la QUINTA al esquema "cada participante paga directamente a LA EMPRESA". Si la institución paga, sustituir el convenio por el contrato que resulte del procedimiento aplicable (LAASSP, ley estatal o normatividad de la autónoma) y dejar el convenio solo para la colaboración académica |
| T3 | 15 (nota 1, SEGUNDA a); 17 (2.2 y 3.1); CLAUDE.md (mercado de egreso) | "Opción de titulación o requisito de egreso para los programas [ ]" | En una institución pública, condicionar el egreso a una evaluación y un certificado de pago a un particular puede ser contrario al principio de gratuidad. Como opción de titulación voluntaria, junto con otras gratuitas, el riesgo baja | CPEUM art. 3, IV: "Toda la educación que el Estado imparta será gratuita". LGES art. 6, VIII: gratuidad para "eliminar progresivamente los cobros… por conceptos de inscripción, reinscripción y cuotas escolares ordinarias". Art. 41: las instituciones establecen los "requisitos académicos y administrativos" de titulación | Alta (instituciones públicas); baja (particulares con RVOE) | En la cláusula SEGUNDA a): "Opción de titulación voluntaria, adicional a las que prevé la normatividad de LA INSTITUCIÓN. En instituciones públicas no se establece como requisito obligatorio de egreso sujeto a pago; si LA INSTITUCIÓN la establece como requisito, cubre el costo o garantiza una alternativa sin costo para el estudiante". Por confirmar con el abogado de cada subsistema |
| T4 | 04 (marco jurídico, LFDA); 10 (2.4) | "consentimiento para usar el retrato de una persona"; "La Ley Federal del Derecho de Autor protege el retrato de las personas" | Desde la reforma del 14-05-2026, el art. 87 protege la imagen y la voz de artistas intérpretes y ejecutantes, incluidos los clones con IA (arts. 118, VII y 121). La imagen de cualquier otra persona se protege por el CCF (daño moral) y como dato personal | LFDA art. 87: "La imagen, incluida la voz, de las personas artistas intérpretes o ejecutantes…". Art. 231, II: infracción en materia de comercio. CCF art. 1916: "…vida privada, configuración y aspecto físicos…". LFPDPPP art. 2, V | Media | 04: "Consentimiento expreso para usar la imagen o la voz de artistas, incluidos los resultados de IA (art. 87, reforma de mayo de 2026); para cualquier persona, protección de su imagen como dato personal y frente al daño moral (CCF art. 1916)". 10: "La ley protege la imagen y la voz de las personas: como dato personal, frente al daño moral y, en el caso de artistas, también por derecho de autor, incluso cuando se recrean con IA" |
| T5 | 08 (reactivo 8, clave b); 11 (tema 2.1); 12 (2.1, nota ya agregada); 13 (9.4); 17 (3.1) | "Comunicar datos personales a un proveedor que los trata por cuenta de la organización es: b) Una remisión" | La respuesta correcta depende de que el reglamento de 2011 siga aplicándose a la ley de 2025. Un reactivo de certificación con base jurídica incierta puede impugnarse | LFPDPPP 2025: no define remisión; art. 2, XX la excluye de transferencia ("distinta… de la persona encargada"). RLFPDPPP art. 2, IX y art. 53: "Las remisiones… entre un responsable y un encargado no requerirán ser informadas al titular ni contar con su consentimiento" | Media | Reactivo 8: "…es: a) una transferencia; b) una comunicación a la persona encargada, que no es transferencia; c) una publicación; d) una cesión de derechos", con clave b). En los textos, decir "comunicación a la persona encargada (remisión, en el reglamento de 2011)" |
| T6 | 09 (sección 8); 11 (sección 8); 15 (TERCERA.7) | "A quien aprueba el curso se le puede expedir la constancia de competencias o de habilidades laborales (formato DC-3)" | La DC-3 forma parte del sistema de capacitación de los trabajadores de una empresa: lleva los datos del patrón, la autentica la Comisión Mixta o el patrón y se reporta en la lista DC-4. No aplica a estudiantes ni a particulares sin patrón. Además, la empresa solo puede expedirla si está registrada como agente capacitador externo | Acuerdo STPS 2013, art. 24: la constancia se expide "por… La entidad instructora cuando se trate de agentes capacitadores externos" y se autentica "por la Comisión Mixta… o por el patrón". LFT art. 153-T y art. 153-A, tercer párrafo ("autorizados y registrados") | Media | "La constancia DC-3 se expide a las personas trabajadoras cuyo patrón incluya el curso en su plan de capacitación, por LA EMPRESA como agente capacitador externo registrado ante la STPS, y la autentica la Comisión Mixta o el patrón. A estudiantes y participantes sin patrón se les entrega una constancia de participación, que no es DC-3" |
| T7 | 03 (E3, producto 2); 14 (5.4 y anexo 5); 13 (7.3) | Lista de verificación de proveedores: entrenamiento, conservación, ubicación, eliminación, seguridad, incidentes, terceros | Falta el criterio jurídico central: si el proveedor de IA actúa como **persona encargada** (contrato con instrucciones, sin fines propios) o como **tercero** (transferencia: aviso con cláusula y, en su caso, consentimiento). Un proveedor que usa los datos "para entrenar sus modelos" es tercero | LFPDPPP art. 2, XX; art. 35: "…el aviso de privacidad… contendrá una cláusula en la que se indique si la persona titular acepta o no la transferencia…"; art. 58, XII y XIII (infracciones). RLFPDPPP arts. 50 y 51 (por confirmar). Por analogía, LGPDPPSO art. 58, c): abstenerse de condiciones que permitan "asumir la titularidad o propiedad de la información" | Media | Agregar a la lista: "Calidad del proveedor: persona encargada (trata los datos solo por cuenta y conforme a instrucciones de la organización, con contrato) o tercero receptor (transferencia: requiere cláusula en el aviso y, en su caso, consentimiento). Transferencias internacionales: país y fundamento". En el EC-B, producto 2: "Contiene criterios sobre la calidad del proveedor como persona encargada o tercero" |
| T8 | 14 (9.2.3); 12 (2.3) | "…salvo que la finalidad lo justifique y la ley lo permita" | En el empleo, la LFT prohíbe sin excepción negarse a contratar por esos criterios. La salvedad abierta puede leerse como permiso para discriminar | LFT art. 133, I: prohibido "Negarse a aceptar trabajadores por razón de… edad,… estado civil o cualquier otro criterio que pueda dar lugar a un acto discriminatorio". LFPDPPP art. 8 (datos sensibles). LFPED | Media | "…se excluyen los datos personales sensibles y las variables que puedan discriminar, como la edad, el sexo, el estado civil o el número de hijos. Solo pueden usarse cuando una disposición legal lo exija o para una acción afirmativa documentada, con revisión del área jurídica" |
| T9 | 15 (DÉCIMA PRIMERA.1); 17 (3.1 y 3.4); 18 (4.3) | "Los cursos, guías, materiales e instrumentos de LA EMPRESA son de su propiedad" | La titularidad no está asegurada: (a) si los elaboran empleados con contrato escrito sin pacto, los derechos se presumen divididos por partes iguales; (b) los colaboradores externos y los integrantes del grupo técnico deben ceder por escrito; (c) la ley reconoce como autor a la persona física, lo que debilita la protección de lo generado con IA sin aporte humano; (d) los instrumentos y claves se protegen mejor como secreto industrial | LFDA art. 84: "…a falta de pacto en contrario, se presumirá que los derechos patrimoniales se dividen por partes iguales entre empleador y empleado". Art. 83 (obra por encargo). Art. 30: transmisión "onerosa y temporal" y "por escrito, de lo contrario serán nulos de pleno derecho". Art. 12: "Autor es la persona física…". LFPPI art. 163, I (secreto industrial: medios "suficientes para preservar su confidencialidad") | Media | Firmar con cada empleado, consultor e integrante del grupo técnico una cesión o licencia escrita, con contraprestación y plazo. Documentar la autoría y revisión humana de cada material. Clasificar los instrumentos y claves como secreto industrial, con acceso restringido, registro de quién accede y cartas de confidencialidad (ya previstas en 17, 3.4). Registrar las obras ante INDAUTOR y las marcas comerciales de los cursos ante el IMPI |

### 4.1 Documento 02 · EC-A

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 02-1 | Referencias de información | "Ley Federal del Derecho de Autor." | Falta la fecha de la reforma de IA (14-05-2026), que fundamenta el criterio sobre voz e imagen | LFDA arts. 87, 118, VII y 121 | Baja | "Ley Federal del Derecho de Autor (última reforma DOF 14 de mayo de 2026)". Agregar "Código Civil Federal, artículo 1916" |
| 02-2 | Elemento 2, desempeño 2 | "Etiquetando como generado con IA el contenido sintético de imagen, audio o video." | Es una buena práctica, no una obligación legal general vigente en México (la "Ley Antimemes" no está publicada). No contraviene la ley, pero como criterio universal puede leerse como deber legal | No se localizó disposición federal vigente que obligue a etiquetar. **Por confirmar** al publicarse la reforma en trámite | Baja | "Etiquetando como generado con IA el contenido sintético de imagen, audio o video, conforme a la política de la organización." |
| 02-3 | Elemento 1, desempeño 3 | "Solicitando autorización al responsable designado cuando la tarea requiere información clasificada que no puede depurarse." | La autorización interna no sustituye el fundamento legal (consentimiento o excepción) para tratar datos sensibles | LFPDPPP art. 8: "…consentimiento expreso y por escrito de la persona titular…" | Baja | "…solicitando autorización al responsable designado, quien verifica que exista fundamento para ese tratamiento." |
| 02-4 | Glosario E1 | Definiciones de dato personal y dato sensible | Coinciden con el art. 2, V y VI (corregidas el 9-10-2026) | — | — | Sin cambio |

### 4.2 Documento 03 · EC-B

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 03-1 | Elemento 3, producto 2 | Lista de verificación de proveedores (cinco criterios) | Ver T7: falta la calidad del proveedor como persona encargada o tercero, y las transferencias internacionales | LFPDPPP arts. 2, XX; 35 y 36 | Media | Agregar: "Contiene criterios sobre la calidad del proveedor como persona encargada o tercero receptor, y sobre las transferencias internacionales," |
| 03-2 | Elemento 3, producto 1 | "Indica las consecuencias de su incumplimiento" | Sin vínculo con el reglamento interior de trabajo, las sanciones de la política pueden no ser aplicables a las personas trabajadoras | LFT art. 423, X: el reglamento contiene las "Disposiciones disciplinarias y procedimientos para su aplicación. La suspensión… no podrá exceder de ocho días…". Art. 424, III: "No producirán ningún efecto legal las disposiciones contrarias a esta Ley…" | Baja | "Indica las consecuencias de su incumplimiento conforme al reglamento interior de trabajo y a los contratos aplicables, e" |
| 03-3 | Elemento 3, producto 1 | (No existe) | La política no exige verificar que los usos de IA con datos personales estén informados en el aviso de privacidad y tengan fundamento | LFPDPPP arts. 7, 14 y 15, III | Media | Agregar: "Establece que los usos de IA que traten datos personales estén informados en el aviso de privacidad y cuenten con fundamento para su tratamiento," |
| 03-4 | Elemento 2, conocimiento 4 | "Usos de IA que afectan derechos de las personas trabajadoras…" | Conviene anclarlo a sus fundamentos: no discriminación, oposición a decisiones automatizadas y supervisión proporcional en teletrabajo | LFT arts. 133, I y 330-I ("…deberán ser proporcionales a su objetivo, garantizando el derecho a la intimidad…"). LFPDPPP art. 26, II | Baja | "…selección, evaluación del desempeño, supervisión y terminación de la relación laboral; no discriminación, oposición a decisiones automatizadas y proporcionalidad de la supervisión." |
| 03-5 | Glosario E4, "Vulneración de seguridad" | Lista de pérdida, robo, extravío… | Coincide con RLFPDPPP art. 63 y LGPDPPSO art. 32; la ley para particulares no la define | Ver sección 3 | Baja | Mantener; en la nota 6 citar también el RLFPDPPP art. 63 (vigencia por confirmar) |
| 03-6 | Elemento 4, desempeño 2 | "…vulneración de seguridad… que deba informarse a las personas titulares conforme a la normatividad aplicable" | Coincide con el art. 19 | LFPDPPP art. 19 | — | Sin cambio |

### 4.3 Documento 04 · Exposición de motivos

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 04-1 | Marco jurídico, fila LFDA | "Autorización para usar obras protegidas y consentimiento para usar el retrato de una persona" | Ver T4 | LFDA art. 87 (DOF 14-05-2026); CCF art. 1916 | Media | Ver T4 |
| 04-2 | Marco jurídico, fila LFPDPPP | "Vigente desde el 21 de marzo de 2025" | Correcto (transitorio primero: entra en vigor al día siguiente de su publicación). Falta la reforma del 14-11-2025 | LFPDPPP, transitorio primero; encabezado "Última reforma publicada DOF 14-11-2025" | Baja | "Vigente desde el 21 de marzo de 2025 (última reforma DOF 14 de noviembre de 2025)" |
| 04-3 | Marco jurídico, fila "Ley Antimemes" | "Aprobada por el Senado el 30 de septiembre de 2026 y por la Cámara de Diputados, con cambios, el 7 de octubre; regresa al Senado" | Basada en notas de prensa; no hay texto oficial. La reforma a la LFDA de mayo de 2026, ya vigente, cubre parte del tema (clones de voz e imagen de artistas) | Sin texto oficial: **por confirmar** | Baja | Agregar una fila "Reforma a la LFDA en materia de IA (DOF 14-05-2026)" y marcar la "Ley Antimemes" como "en proceso legislativo; texto por confirmar" |
| 04-4 | Beneficios, "Gobierno" | "…para pedir personal acreditado a sus proveedores…" | Exigir una certificación específica en una contratación pública puede limitar la libre participación si no se justifica | LAASSP art. 40, V: los requisitos de participación "no deberán limitar la libre participación, concurrencia y competencia económica" | Baja | "…y, cuando la normatividad de contrataciones lo permita y sin limitar la libre participación, para pedir personal certificado a sus proveedores." |
| 04-5 | Principios, "Adopción voluntaria" | "…una autoridad podrá referirlos solo dentro de sus facultades" | Correcto. La LICal permite que una NOM atienda "objetivos legítimos de interés público", entre ellos la integridad de los trabajadores y la educación (art. 10). Que una NOM exija un EC del CONOCER es posible, pero no está previsto expresamente | LICal art. 10 | — | Sin cambio |

### 4.4 Documentos 05 a 08 · Instrumentos de evaluación

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 05-1 | Preparación, punto 3; Parte C | "Grabe la nota de voz con el guion…" | La voz de quien graba es un dato personal y se usa con miles de candidatos. Hace falta su consentimiento documentado | LFPDPPP arts. 2, V y 7 | Baja | "Grabe la nota de voz con una persona del Centro que haya firmado su autorización, o con una voz sintética." |
| 05-2 y 07-1 | Notas, "Evaluación a distancia" | "Probar una versión por videollamada…" | Si se graba, se tratan imagen, voz e identificación de la persona candidata. Requiere aviso específico y medidas de seguridad | LFPDPPP arts. 14, 15 y 18 | Media | "…sujeta a lo que autorice el CONOCER; si la sesión se graba, informarlo en el aviso de privacidad, recabar la aceptación antes de iniciar y fijar el plazo de conservación." |
| 06-1 | Cuestionario, reactivo 18 | "Una imagen generada con IA para un comunicado debe: … d) Llevar la leyenda de contenido generado con IA" | Presentado como deber absoluto. Es regla de la política del caso (anexo A1, punto 8), no de la ley | Ver 02-2 | Baja | "Conforme a la política del caso (Anexo A1), una imagen generada con IA para un comunicado debe:" |
| 06-2 | Cuestionario, reactivo 15 | "Para usar la voz de una persona recreada con IA se requiere: c) Su consentimiento" | Correcto como regla general (dato personal y, para artistas, LFDA art. 87) | LFPDPPP art. 7; LFDA art. 87 | — | Sin cambio |
| 06-3 | Anexo A3, dato sensible | "Salud, origen étnico, creencias, opiniones políticas, preferencia sexual, información genética, entre otros" | Coincide con el art. 2, VI (corregido) | — | — | Sin cambio |
| 08-1 | Cuestionario, reactivo 8 | Clave "b) Una remisión" | Ver T5 | — | Media | Ver T5 |
| 08-2 | Cuestionario, reactivos 21, 22, 25 y 26 | LFT; constancia; vulneraciones | Coinciden con LFT arts. 153-A y 153-V, LFPDPPP art. 19 y RLFPDPPP art. 63 | — | — | Sin cambio |
| 07-2 | Clave del caso, determinación del incidente | "…tratamiento no autorizado por un tercero…" | Coincide con RLFPDPPP art. 63, III y LGPDPPSO art. 32, III | — | — | Sin cambio |

### 4.5 Documentos 09 a 12 · Cursos y guías

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 09-1 y 11-1 | Sección 8, "Constancia DC-3" | "A quien aprueba el curso se le puede expedir… (formato DC-3)" | Ver T6 | Acuerdo STPS 2013, art. 24; LFT arts. 153-A y 153-T | Media | Ver T6 |
| 09-2 y 11-2 | Sección 8 | (No existe) | Las constancias no pueden sugerir que la STPS avala el curso | Acuerdo STPS 2013, art. 25: "no se deberán utilizar imágenes, ni textos que identifiquen o hagan referencia a que la Secretaría avala el desarrollo, contenido o calidad de los cursos" | Baja | Agregar: "La constancia no incluye logotipos ni textos que sugieran que la STPS o el CONOCER avalan el curso." |
| 09-3 | Sección 9, modalidades | "Universidades y bachilleratos" | En bachillerato puede haber menores de edad. Se requiere el consentimiento de quien ejerza la patria potestad o la tutela, y el aviso debe preverlo. Confirmar si el CONOCER evalúa a menores | LGPDPPSO art. 7 ("…privilegiar el interés superior…") y art. 14 (consentimiento conforme a "las reglas de representación previstas en la legislación civil"). Para particulares, por confirmar en el CCF | Media | "Universidades y bachilleratos (con personas menores de edad: consentimiento de su madre, padre o tutor, y confirmar con el CONOCER la edad mínima para certificarse)" |
| 10-1 | 2.4, derechos de terceros | "La Ley Federal del Derecho de Autor protege el retrato de las personas…" | Ver T4 | LFDA art. 87; CCF art. 1916 | Media | Ver T4 |
| 10-2 | 1.4 y referencias | "Ley Federal de Protección de Datos Personales… (Diario Oficial de la Federación, 20 de marzo de 2025)" | Falta la reforma del 14-11-2025 | Encabezado del texto vigente | Baja | Agregar "última reforma DOF 14 de noviembre de 2025" en 10 y 12 |
| 11-3 | Tema 2.1 | "…las transferencias y las remisiones…" | Ver T5 | — | Baja | "…las transferencias y la comunicación a personas encargadas…" |
| 11-4 | Nota al reactivo 15 | "…confirmar la redacción vigente antes de aplicarlo" | Ya se confirmó: LFT art. 153-E | LFT art. 153-E | Baja | Sustituir la nota por "Fundamento: LFT art. 153-E (verificado el 9 de octubre de 2026)" |
| 12-1 | 2.3, decisiones sobre personas | "…salvo que la finalidad lo justifique y la ley lo permita" | Ver T8 | LFT art. 133, I | Media | Ver T8 |
| 12-2 | 2.3, supervisión | "Supervisión: cámaras, monitoreo de equipos, geolocalización, análisis de productividad" | Falta el límite legal: proporcionalidad, intimidad y aviso de privacidad para el personal | LFT art. 330-I: "Solamente podrán utilizarse cámaras de video y micrófonos para supervisar el teletrabajo de manera extraordinaria…". LFPDPPP arts. 12 y 14 | Baja | Agregar: "La supervisión debe ser proporcional, informarse en el aviso de privacidad del personal y, en teletrabajo, usar cámaras y micrófonos solo de manera extraordinaria (LFT art. 330-I)." |
| 12-3 | 4.3, aviso de la encargada | "…debe avisar de inmediato a la organización responsable, conforme al contrato…" | Correcto: para particulares el deber nace del contrato. Para instituciones públicas está en la ley | LGPDPPSO art. 53, IV | — | Sin cambio |

### 4.6 Documento 13 · Diagnóstico empresarial

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 13-1 | 10, confidencialidad y datos | "Solo recibe los datos de contacto de las personas entrevistadas…" | La empresa recaba datos de entrevistados y notas con sus opiniones. Es responsable de esos datos y debe darles a conocer su aviso (T1) | LFPDPPP arts. 14 y 16 | Media | En 7.2, "Apertura": "…pedir permiso para tomar notas y dar a conocer el aviso de privacidad simplificado de la empresa consultora." |
| 13-2 | 10 | "…la empresa consultora actúa como encargada y se firma el contrato correspondiente…" | Correcto. Conviene listar las cláusulas mínimas | RLFPDPPP arts. 50 y 51 (por confirmar); por analogía, LGPDPPSO art. 53 | Baja | Remitir a un modelo de contrato de encargo con: instrucciones, finalidad limitada, seguridad, confidencialidad, aviso de vulneraciones, subcontratación solo autorizada, devolución o supresión |
| 13-3 | 9.4 | "(Ley… DOF 20 de marzo de 2025): medidas de seguridad, aviso de privacidad, remisiones y transferencias…" | Falta la reforma; "remisiones" (T5) | — | Baja | "(…DOF 20-03-2025; última reforma DOF 14-11-2025): …comunicación a personas encargadas y transferencias…" |
| 13-4 | 3 y 12 | "No es una opinión jurídica…"; "Le evitamos multas" (prohibido) | Correcto. Faltan el contrato de servicios y la limitación de responsabilidad | CCF art. 1916 y reglas de responsabilidad contractual; LFPC art. 32 (publicidad veraz) | Media | Elaborar un contrato de prestación de servicios profesionales con alcance, entregables, exclusión de opinión jurídica, límite de responsabilidad, confidencialidad y encargo de datos |
| 13-5 | 5, registro técnico agregado | "…sin contenido ni identificación de personas" | Correcto: minimización conforme al principio de proporcionalidad | LFPDPPP art. 12 | — | Sin cambio |

### 4.7 Documento 14 · Plantilla de política de uso de IA

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 14-1 | 3, definiciones | "Dato personal: cualquier información concerniente a una persona física identificada o identificable." / "Dato personal sensible: … como el estado de salud, el origen racial o étnico, las creencias, las opiniones políticas y la preferencia sexual." | Incompletas frente al texto vigente | LFPDPPP art. 2, V y VI | Media | Copiar las definiciones literales del glosario del documento 02 |
| 14-2 | 6.1, tabla, "Dato personal sensible" | "No se ingresa, salvo autorización expresa y registrada de [Responsable de protección de datos]" | La autorización interna no sustituye el consentimiento expreso y por escrito de la persona titular (o una excepción legal). Ingresar datos a un proveedor externo también exige que sea persona encargada con contrato (T7) | LFPDPPP art. 8: "…consentimiento expreso y por escrito… a través de su firma autógrafa, firma electrónica…"; art. 58, XIII (infracción) | Alta | "No se ingresa. Solo por excepción, con autorización registrada de [Responsable de protección de datos], quien verifica que exista consentimiento expreso y por escrito de la persona titular o una excepción legal, y que el sistema esté autorizado y contratado con el proveedor como persona encargada." |
| 14-3 | 6.1, tabla, "Dato personal" | "…y con autorización registrada de [Responsable de protección de datos]" | Igual que 14-2: hace falta un fundamento (consentimiento o excepción) y un contrato de encargo con el proveedor | LFPDPPP arts. 7, 9 y 35 | Media | Agregar: "…y siempre que el tratamiento esté informado en el aviso de privacidad y el proveedor actúe como persona encargada." |
| 14-4 | 10.3 | "[Tecnologías de la Información]… conserva los registros técnicos de su uso." | El monitoreo del personal debe informarse en el aviso de privacidad para empleados, limitarse a equipos y cuentas de la organización y tener un plazo de conservación | LFPDPPP arts. 12 y 14; LFT art. 330-I (teletrabajo); CPEUM art. 16 ("Las comunicaciones privadas son inviolables") | Media | "…conserva los registros técnicos de acceso de los equipos y cuentas de la organización, sin el contenido de las comunicaciones, durante [plazo], conforme al aviso de privacidad para el personal." |
| 14-5 | 9.2.3 | "…salvo que la finalidad lo justifique y la ley lo permita." | Ver T8 | LFT art. 133, I | Media | Ver T8 |
| 14-6 | 9.2.4 | "Se establece un medio para que la persona pida una aclaración o una revisión." | Correcto. Conviene citar el derecho de oposición | LFPDPPP art. 26, II | Baja | "…una revisión, sin perjuicio de su derecho de oposición (art. 26, fracción II, de la ley de datos personales)." |
| 14-7 | 11.5 y 15.1 | "La omisión o el ocultamiento de un incidente sí es motivo de sanción." | Las sanciones solo son exigibles si están en el reglamento interior de trabajo o en los contratos. La suspensión disciplinaria no puede exceder de ocho días y la persona debe ser oída. La nota 5 ya lo advierte | LFT art. 423, X | Baja | "…es motivo de las medidas disciplinarias que prevea el reglamento interior de trabajo." |
| 14-8 | 2.1, alcance | "…incluidos [practicantes, becarios, personal por honorarios y de empresas contratistas]" | Aplicar directamente la política y sus sanciones al personal de contratistas puede ser indicio de subordinación. Para ellos rige el contrato (2.3) | LFT arts. 12 y 13 (subcontratación) | Baja | "…y, por medio de sus contratos, al personal de empresas contratistas y prestadores de servicios." |
| 14-9 | 12.3 | "[Recursos Humanos] registra la capacitación conforme a la Ley Federal del Trabajo y expide las constancias correspondientes." | La constancia la expide la entidad instructora externa o la empresa (si el instructor es interno), y la autentica la Comisión Mixta o el patrón | Acuerdo STPS 2013, art. 24 | Baja | "…registra la capacitación, recaba las constancias DC-3 que expida el agente capacitador o las expide si el instructor es interno, y presenta las listas a la STPS." |
| 14-10 | Notas | (No existe) | Falta la designación del departamento de datos personales y la actualización del aviso de privacidad del personal | LFPDPPP art. 29 | Baja | Agregar una nota: "Designa a la persona o departamento de datos personales (art. 29) y actualiza el aviso de privacidad del personal y de clientes." |

### 4.8 Documento 15 · Convenio tipo con instituciones educativas

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 15-1 | QUINTA y anexo B | Opción "LA INSTITUCIÓN paga por los participantes" | Ver T2 | LAASSP art. 1 | Alta | Ver T2 |
| 15-2 | SEGUNDA a) | "Opción de titulación o requisito de egreso…" | Ver T3 | CPEUM art. 3, IV; LGES arts. 6, VIII y 41 | Alta | Ver T3 |
| 15-3 | CUARTA.3 | "Proporcionar las aulas, el equipo de cómputo y la conectividad…" | En una institución pública, prestar bienes a un particular para un servicio que cobra puede ser uso indebido de recursos públicos sin autorización o contraprestación | LGRA art. 71: "Será responsable por el uso indebido de recursos públicos el particular que… haga uso indebido o desvíe del objeto para el que estén previstos los recursos públicos…" | Media | "…conforme a las disposiciones de LA INSTITUCIÓN sobre el uso de sus instalaciones y, en su caso, a la contraprestación o autorización que estas exijan." |
| 15-4 | CUARTA.2 | "Difundir entre su comunidad la oferta de alineación, evaluación y certificación." | Una institución pública que promueve el servicio de pago de un particular sin un procedimiento de selección puede afectar la imparcialidad | LGRA art. 7: las personas servidoras públicas observarán los principios de "…legalidad, objetividad, profesionalismo, honradez, lealtad, imparcialidad…" | Baja | "Informar a su comunidad, como opción voluntaria, de la oferta de alineación, evaluación y certificación, sin perjuicio de otras opciones." |
| 15-5 | NOVENA y anexo D | "Fundamento: Aviso de privacidad de LA EMPRESA" | El aviso informa, pero no es el fundamento. Los fundamentos son el consentimiento (art. 7) o una excepción (art. 9, IV: obligaciones de una relación jurídica). La transferencia al CONOCER y a la ECE requiere cláusula en el aviso (art. 35) y se apoya en el art. 36, IV o VII. Las "reglas del CONOCER" no son "una Ley o Tratado" (art. 36, I) | LFPDPPP arts. 7, 9, 35 y 36 | Media | Columna "Fundamento": "Consentimiento de la persona titular (art. 7) y relación jurídica con LA EMPRESA (art. 9, IV); transferencia al CONOCER y a la ECE conforme a los arts. 35 y 36, fracciones IV y VII, informada en el aviso de privacidad" |
| 15-6 | NOVENA | (No existe) | Cuando la institución pública inscribe a su personal o a sus estudiantes y paga, LA EMPRESA puede ser su persona encargada. La LGPDPPSO exige un instrumento con cláusulas mínimas | LGPDPPSO art. 53: "La relación entre el responsable y la persona encargada deberá estar formalizada mediante contrato…" con cláusulas I a IV y siguientes; art. 60 (transferencias formalizadas) | Media | Agregar NOVENA.7: "Cuando LA EMPRESA trate datos personales por cuenta de LA INSTITUCIÓN, actuará como persona encargada y se obliga a: tratarlos conforme a sus instrucciones; no usarlos para otros fines; aplicar medidas de seguridad; guardar confidencialidad; informar de inmediato las vulneraciones; no subcontratar sin autorización; y suprimirlos o devolverlos al terminar." |
| 15-7 | NOVENA | (No existe) | Si participan menores de edad (bachillerato), se requiere el consentimiento de quien los represente | LGPDPPSO arts. 7 y 14; legislación civil aplicable | Media | Agregar: "Si participan personas menores de edad, se recaba el consentimiento de quien ejerza la patria potestad o la tutela." |
| 15-8 | TERCERA.7 | "Expedir las constancias de capacitación que correspondan…" | Ver T6 | Acuerdo STPS 2013, art. 24 | Media | "Expedir la constancia de participación a quienes aprueben el curso y, a las personas trabajadoras de LA INSTITUCIÓN, la constancia DC-3 como agente capacitador externo registrado." |
| 15-9 | DÉCIMA PRIMERA.1 | "…una licencia no exclusiva y gratuita…" | La licencia debe constar por escrito (se cumple con el convenio). Para la transmisión de derechos, la LFDA exige onerosidad; si una licencia gratuita es válida, debe confirmarse | LFDA art. 30 | Baja | Por confirmar con el abogado; alternativa: "licencia no exclusiva, cuya contraprestación queda comprendida en las cuotas del anexo B" |
| 15-10 | DÉCIMA TERCERA | "…no será considerada patrón solidario ni sustituto." | La cláusula no impide la responsabilidad solidaria que fija la ley si hay subcontratación. Si el personal de la empresa presta servicios en beneficio de la institución dentro de su actividad preponderante (educación), se debe revisar el régimen de servicios especializados | LFT art. 12 ("Queda prohibida la subcontratación de personal…"), art. 13 (servicios especializados con registro) y art. 14 (responsabilidad solidaria) | Media | Mantener, y agregar: "LA EMPRESA presta sus servicios con su propio personal, bajo su dirección, y cumple sus obligaciones laborales y de seguridad social." Determinar con el abogado si se requiere registro de servicios especializados (art. 15) |
| 15-11 | Cláusulas generales | (No existen) | El convenio está equilibrado en terminación (DÉCIMA QUINTA), confidencialidad y datos. Le faltan: incumplimiento y rescisión; responsabilidad por daños y por reclamaciones de terceros (datos, propiedad intelectual); prohibición de ceder derechos; domicilios para notificaciones; para entes federales, la declaración de no conflicto de interés de quien firma | CCF (contratos, por confirmar los artículos aplicables); LGRA art. 58 (conflicto de interés) | Media | Agregar las cláusulas de rescisión por incumplimiento con aviso y plazo para subsanar, responsabilidad de cada parte por sus actos, no cesión, notificaciones y declaración de no conflicto de interés |
| 15-12 | DÉCIMA NOVENA | "…se someten a [los tribunales competentes de la ciudad de ___]…" | Para entes públicos federales suele pactarse la jurisdicción de los tribunales federales | **Por confirmar** según la naturaleza de la institución | Baja | "[Para instituciones públicas federales: los tribunales federales con sede en ___]" |
| 15-13 | SÉPTIMA.2 | "Quien imparta el curso de alineación a un grupo no evalúa… a las personas de ese grupo." | Coincide con la regla del CONOCER | M-DGAOSU-02, página 103: "revisar que el personal que capacita, no evalúe en el mismo proceso de la misma candidata o candidato" | — | Sin cambio |

### 4.9 Documento 16 · Plan de la prueba piloto

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 16-1 | Anexo 1, punto 5 | "…conforme al aviso de privacidad de [empresa], que recibí…" | El aviso no existe (T1). El consentimiento debe precisar las finalidades del piloto, incluido el uso de resultados para análisis y su entrega agregada al CONOCER | LFPDPPP arts. 7 y 15, III | Alta (mientras no exista el aviso) | Agregar: "Mis resultados se usan para analizar los instrumentos y se informan al CONOCER solo de forma agregada." |
| 16-2 | 6.1 | "La participación o el resultado no afectan calificaciones, empleo ni evaluaciones de desempeño." | Correcto y necesario. Con personas trabajadoras de empresas piloto, debe asegurarse que el consentimiento sea libre y que el patrón no conozca quién no participó | LFPDPPP art. 7 (consentimiento) | Baja | Agregar: "La empresa piloto no recibe la lista de quienes no aceptaron participar." |
| 16-3 | 3.1.6 | "Evaluación a distancia… por videollamada con pantalla compartida" | Ver 05-2 | LFPDPPP arts. 14, 15 y 18 | Media | Ver 05-2 |
| 16-4 | 2, participantes | "Estudiantes de últimos semestres" | Normalmente son mayores de edad; si se incluye bachillerato, ver 09-3 | LGPDPPSO art. 14 | Baja | "…mayores de edad; con menores, consentimiento de su madre, padre o tutor." |

### 4.10 Documento 17 · Gobernanza

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 17-1 | 3.4, carta | Confidencialidad y conflicto de interés | Falta la cesión o licencia de las aportaciones de cada integrante a los estándares e instrumentos (T9) y el aviso de privacidad de sus datos | LFDA arts. 30 y 83; LFPDPPP art. 14 | Media | Agregar a la carta: "Autorizo a [empresa / CGC] a usar, modificar e incorporar mis aportaciones en los estándares, instrumentos y materiales, y cedo los derechos patrimoniales correspondientes en los términos del anexo." Agregar el aviso de privacidad de integrantes |
| 17-2 | 3.1, perfil de datos | "…transferencias y remisiones" | Ver T5 | — | Baja | "…transferencias y comunicación a personas encargadas" |
| 17-3 | 2.1, recomendación | "…plantear ambas opciones a la directora del CONOCER…" | La relación cercana con la titular del CONOCER exige canales formales: la servidora pública debe excusarse de los asuntos en que tenga conflicto de interés, y el particular no debe usar influencia para obtener ventajas | LGRA art. 58 (actuación bajo conflicto de interés: "…solicitando sea excusado…") y art. 68 (tráfico de influencias de particulares: "…use su influencia… con el propósito de obtener… un beneficio o ventaja…") | Media | "…plantear ambas opciones al CONOCER por los canales formales (oficio y reunión con minuta), y documentar las interacciones." |

### 4.11 Documento 18 · Decisión EC o ECM

| # | Ubicación | Texto actual | Problema | Fundamento | Gravedad | Redacción propuesta |
|---|---|---|---|---|---|---|
| 18-1 | 4.4 | "Convenios con universidades y empresas… firmados antes de que lleguen otros prestadores." | Correcto mientras los convenios no sean exclusivos. Con instituciones públicas, una exclusividad sin procedimiento sería impugnable | LAASSP art. 1 (instituciones federales); principio de imparcialidad (LGRA art. 7) | Baja | Agregar: "Los convenios con instituciones públicas no son exclusivos." |
| 18-2 | 3, primera fila | "Fuerte. Un estándar público y neutral es más fácil de citar en una norma…" | Razonable, pero que una NOM o una contratación exija un EC depende de la autoridad, de sus facultades y de no limitar la participación | LICal art. 10; LAASSP art. 40, V (libre participación) | Baja | Agregar "(por confirmar con la autoridad competente en cada caso)" |
| 18-3 | 2, "Quién evalúa" | Reglas del manual de 2016 | Correcto según el manual; su vigencia está por confirmar | M-DGAOSU-02, puntos 4.1.2, 4.2.2 y 4.6 | — | Sin cambio |

---

## 5. Riesgos para la empresa

| Papel | Riesgo | Fundamento | Gravedad | Mitigación |
|---|---|---|---|---|
| Desarrolladora | Responder por el contenido de los estándares | Acuerdo SE/III-26/05,R: el contenido "es responsabilidad exclusiva de la Institución" | Media | Revisión jurídica antes de presentar; minutas del grupo técnico; registro de fuentes (`verificacion/`) |
| Desarrolladora | Materiales sin titularidad clara (empleados, consultores, grupo técnico, apoyo de IA) | LFDA arts. 12, 30, 83 y 84 | Media | T9: cesiones escritas, documentación de autoría humana, registro ante INDAUTOR, marcas ante el IMPI |
| Desarrolladora | Percepción de influencia indebida por la relación con la titular del CONOCER | LGRA arts. 58 y 68 | Media | Canales formales, minutas, excusa de la servidora pública cuando proceda; evitar regalos y beneficios (convenio, DÉCIMA OCTAVA) |
| Centro evaluador | Tratar datos de candidatos sin aviso o con transferencias no informadas al CONOCER y la ECE | LFPDPPP arts. 15, 35, 58 (V, X y XIII) y 59 (multas de hasta 320,000 UMA, hasta el doble si hay datos sensibles); delitos de los arts. 62 y 63 | Alta | T1: aviso integral y simplificado, cláusula de transferencias, departamento de datos, medidas de seguridad, plazo de conservación de evidencias |
| Centro evaluador | Pérdida de la autorización por no separar capacitación y evaluación | M-DGAOSU-02, página 103 | Media | Mantener la SÉPTIMA.2 del convenio y registrar quién capacitó y quién evaluó a cada persona |
| Centro evaluador | Filtración de instrumentos y claves | LFPPI art. 163 (secreto industrial, requiere medios suficientes de confidencialidad) | Media | Acceso restringido, registro de accesos, cartas de confidencialidad, versiones paralelas |
| Capacitadora | Expedir DC-3 sin registro como agente capacitador, o a personas sin patrón | LFT art. 153-A; Acuerdo STPS 2013, arts. 24 y 25 | Media | Tramitar el registro; DC-3 solo para personas trabajadoras; constancia de participación para el resto; sin logotipos de la STPS |
| Capacitadora | Publicidad engañosa ante consumidores (obligatoriedad, empleo garantizado) | LFPC art. 32: la información o publicidad "deberán ser veraces, comprobables, claros y exentos de… descripciones que induzcan o puedan inducir a error" | Media | Mantener los mensajes permitidos de 09, 11, 13 y 15; agregar política de cancelaciones y reembolsos para personas que pagan |
| Capacitadora | Cobro de un requisito de egreso en instituciones públicas | CPEUM art. 3, IV; LGES art. 6, VIII | Alta | T3 |
| Consultora | Responsabilidad por recomendaciones o por datos del cliente | CCF (responsabilidad contractual, art. 1916 para daño moral); LFPDPPP art. 58 si actúa como responsable | Media | Contrato de servicios con alcance y límite de responsabilidad; contrato de encargo; no usar datos del cliente para fines propios (si lo hace, asume el carácter de responsable: RLFPDPPP art. 53) |
| Consultora | Que la plantilla de política lleve a un cliente a tratar datos sensibles sin consentimiento | LFPDPPP art. 8 | Alta | Corregir 14-2 antes de entregar la plantilla |
| Todas | Contratar con instituciones públicas por convenio cuando procede un contrato | LAASSP art. 1; LGRA art. 71 | Alta | T2 y 15-3 |

---

## 6. Requiere dictamen de un abogado mexicano

1. **Vigencia del reglamento de 2011** de la ley de datos frente a la ley de 2025. Determina si las figuras "remisión" y "encargado", la lista de vulneraciones y los contenidos de su notificación siguen siendo exigibles a particulares (T5, 03-5, 13-2).
2. **Requisito de egreso en instituciones públicas.** Compatibilidad de una certificación de pago con la gratuidad (CPEUM art. 3; LGES), por subsistema: federal, estatal y autónomo (T3).
3. **Vía de contratación con cada tipo de institución pública:** dependencia o desconcentrado (por ejemplo, TecNM), organismo descentralizado estatal (universidades tecnológicas y politécnicas), autónoma, o bachillerato federal. Incluye el uso de sus instalaciones (T2, 15-3, 15-4).
4. **Régimen laboral de los servicios en sedes de clientes e instituciones:** subcontratación y servicios especializados (LFT arts. 12 a 15) (15-10, 14-8).
5. **Contratos tipo de la empresa** (los cuatro faltan):
   - Prestación de servicios de consultoría.
   - Contrato de encargo de datos personales.
   - Cesión de derechos de autor con empleados y consultores.
   - Términos y condiciones para personas que pagan cursos y evaluaciones.
6. **Avisos de privacidad** (candidatos, participantes, entrevistados, integrantes del grupo técnico, personal de la empresa) y la designación del departamento de datos (T1).
7. **Validez de la licencia gratuita** de materiales en el convenio y forma de pactar la contraprestación (LFDA art. 30) (15-9).
8. **Menores de edad.** Si el CONOCER evalúa a personas menores, y cómo recabar el consentimiento en instituciones públicas (LGPDPPSO) y particulares (legislación civil) (09-3, 15-7).
9. **Etiquetado de contenido sintético y uso de imagen y voz.** Alcance de la reforma a la LFDA de mayo de 2026 y de la reforma en trámite ("Ley Antimemes") antes de presentarlas como fundamento (T4, 02-2, 04-3).
10. **Conflicto de interés y trato con el CONOCER**, por la relación de la empresa con su titular y su doble papel como desarrolladora y centro evaluador (17-3).

---

## 7. Por confirmar (sin texto oficial disponible)

- Texto vigente de las Reglas Generales y Criterios para la Integración y Operación del Sistema Nacional de Competencias, y vigencia de los manuales del CONOCER de 2015 y 2016.
- Catálogo oficial de áreas temáticas de la DC-3 (la clave 8000 solo aparece en copias de terceros).
- Lineamientos del aviso de privacidad aplicables a la ley de 2025.
- Texto de la "Ley Antimemes" y de las iniciativas de ciberseguridad.
- Si una licencia gratuita de derechos de autor es válida (LFDA art. 30).
- Jurisdicción que exigen las instituciones públicas en sus convenios.
- Requisitos de edad mínima del CONOCER para certificarse.
- Artículos del CCF aplicables a la rescisión y la responsabilidad contractual del convenio y del contrato de consultoría.
- Cómo aplica cada institución pública el principio de imparcialidad (LGRA art. 7, verificado) a la difusión de servicios de particulares.
