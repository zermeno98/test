# Familia de Estándares de Competencia en Inteligencia Artificial

**Documento de trabajo – Índice de diseño**
Versión 0.1 · Octubre 2026 · Borrador interno, sujeto a validación con el Comité de Gestión por Competencias y con CONOCER.

> Nota: la estructura descrita sigue el formato con el que CONOCER publica los Estándares de Competencia (EC) en el DOF. Antes de redactar debe confirmarse contra la plantilla vigente y contra un EC que el centro evaluador ya opere.

---

## Parte I. Cómo se compone un Estándar de Competencia CONOCER

Un EC no es un temario ni un curso: describe **lo que una persona hace en su trabajo y cómo se demuestra**. Se integra por:

### 1. Datos generales del EC
1. Código (lo asigna CONOCER)
2. Título del EC
3. Propósito del EC
4. Descripción general del EC
5. Nivel en el Sistema Nacional de Competencias (1 a 5)
6. Comité de Gestión por Competencias que lo desarrolló
7. Fecha de aprobación por el Comité Técnico del CONOCER y de publicación en el DOF
8. Periodo sugerido de revisión / actualización
9. Ocupaciones relacionadas (catálogo SINCO)
10. Clasificación según el sector productivo (SCIAN)
11. Organizaciones participantes en su desarrollo
12. Relación con otros Estándares de Competencia
13. Aspectos relevantes de la evaluación (lugar, apoyos, duración estimada en gabinete y en campo)
14. Referencias de información

### 2. Perfil del EC
Lista de los **Elementos** que conforman el estándar (normalmente de 2 a 5).

### 3. Cada Elemento contiene
- **Referencia, código y título** del elemento
- **Criterios de evaluación**, divididos en:
  - **Desempeños**: lo que el evaluador observa que la persona hace.
  - **Productos**: lo que la persona entrega y queda como evidencia.
  - **Conocimientos**: lo que debe saber, con su nivel (conocimiento, comprensión, aplicación…).
  - **Actitudes / hábitos / valores**: cómo se manifiestan durante el desempeño (p. ej. responsabilidad, orden).
  - **Glosario** de términos.

### 4. Documentos que acompañan al EC (no se publican en el DOF, pero son obligatorios)
- **Mapa funcional**: propósito principal → funciones clave → funciones individualizadas (de aquí salen los elementos).
- **Instrumento de Evaluación de Competencia (IEC)**: guías de observación, cuestionarios, listas de cotejo de productos, situaciones simuladas.
- **Prueba piloto** del IEC y sus resultados.
- Acta de formalización del **Comité de Gestión por Competencias** y del **grupo técnico de expertos**.

---

## Parte II. Índice de trabajo para diseñar la familia

### Bloque 0. Gobernanza y arranque
- 0.1 Comité de Gestión por Competencias: integrantes (universidades, empleadores, cámaras, especialistas en datos personales y seguridad de la información).
- 0.2 Grupo técnico de expertos por estándar.
- 0.3 Revisión del RENEC: estándares existentes de IA (EC1657, EC1691, EC1705 y EC1827, EC1828 y EC1829 del Acuerdo SE/III-26/05,R, DOF 7-ago-2026; sin traslape) para evitar duplicidad. Ver `01-mapa-funcional.md`.
- 0.4 Formato oficial: F21-COOPYD-01 (versión 08 en EC publicados 2025–2026).
- 0.5 Marco de referencia: LFPDPPP 2025, LFT art. 153-A, reforma "Ley Antimemes" (cuando se publique), ISO/IEC 27001, ISO/IEC 42001, NIST AI RMF.


### Bloque 1. Mapa funcional común
- Propósito principal: *Utilizar y gestionar sistemas de inteligencia artificial en las organizaciones de forma segura, responsable y conforme a la normatividad aplicable.*
- Función clave A → **EC-A (usuario)**
- Función clave B → **EC-B (responsable)**

### Bloque 2. EC-A – Usuario

| Dato | Propuesta |
|---|---|
| Título de trabajo | Protección de la información en el uso de herramientas de inteligencia artificial generativa en actividades de trabajo *(renombrado para diferenciarlo del EC1705)* |
| Propósito | Servir como referente para evaluar y certificar a las personas que utilizan herramientas de IA generativa en actividades académicas o laborales, protegiendo la información y verificando los resultados. |
| Población | Estudiantes por egresar, personal administrativo y operativo, mandos medios |
| Nivel SNC propuesto | 2 (a confirmar) |
| Duración de evaluación estimada | 2–3 h en gabinete, situación simulada |

**Elementos propuestos**
1. **Preparar el uso de herramientas de IA conforme a la política y a la clasificación de la información**
   - Desempeños: verifica que la herramienta esté autorizada; clasifica la información (pública, interna, confidencial, dato personal, dato sensible); anonimiza o elimina datos antes de ingresarlos.
   - Productos: registro de clasificación de la información del caso.
2. **Generar y verificar productos de trabajo elaborados con IA**
   - Desempeños: formula instrucciones con objetivo y contexto; contrasta el resultado con fuentes; identifica errores, invenciones y sesgos; declara el uso de IA; respeta derechos de autor, imagen y voz de terceros.
   - Productos: documento final con declaración de uso de IA y registro de verificación.
3. **Atender riesgos e incidentes relacionados con el uso de IA**
   - Desempeños: identifica intentos de fraude o suplantación con contenido sintético (voz, video, texto); reporta el ingreso indebido de información; escala al responsable.
   - Productos: reporte de incidente requisitado.

Conocimientos transversales: tipos de datos personales y sensibles; principios de la LFPDPPP; funcionamiento básico y limitaciones de la IA generativa; derechos de autor e imagen; señales de deepfake.
Actitudes: responsabilidad, honestidad (declaración de uso), orden.

### Bloque 3. EC-B – Responsable

| Dato | Propuesta |
|---|---|
| Título de trabajo | Gestión de riesgos y controles en el uso de sistemas de inteligencia artificial en la organización |
| Propósito | Servir como referente para evaluar y certificar a las personas responsables de inventariar, evaluar, controlar y supervisar el uso de sistemas de IA en una organización. |
| Población | Responsables de TI, seguridad de la información, cumplimiento, protección de datos, riesgos |
| Nivel SNC propuesto | 3 o 4 (a confirmar) |
| Duración de evaluación estimada | 4–6 h, gabinete con caso empresarial y entrega de expediente |

**Elementos propuestos**
1. **Integrar el inventario de herramientas y sistemas de IA de la organización**
   - Productos: inventario con herramienta, proveedor, uso, área, responsable y tipo de datos que procesa.
2. **Evaluar los riesgos de los usos de IA identificados**
   - Productos: matriz de riesgos (datos personales, seguridad, errores, sesgo, derechos laborales, propiedad intelectual e imagen, continuidad).
3. **Establecer controles y la política de uso de IA**
   - Productos: política de uso de IA; criterios de autorización de herramientas; lista de verificación contractual con proveedores de IA; programa de capacitación del personal (vinculado al EC-A).
4. **Supervisar el cumplimiento y gestionar incidentes de IA**
   - Productos: registro de incidentes; informe periódico a la dirección; plan de acciones correctivas.

Conocimientos: LFPDPPP 2025 (medidas de seguridad, transferencias y remisiones), LFT art. 153-A, fundamentos de ISO/IEC 27001 y 42001, NIST AI RMF, clasificación de riesgos.
Actitudes: responsabilidad, imparcialidad, perseverancia.

### Bloque 4. Instrumentos de evaluación (uno por EC)
- 4.1 Situación simulada / caso práctico
- 4.2 Guía de observación (desempeños)
- 4.3 Lista de cotejo (productos)
- 4.4 Cuestionario (conocimientos)
- 4.5 Prueba piloto en el centro evaluador y ajuste
- 4.6 Valoración de evaluación a distancia (confirmar con CONOCER)

### Bloque 5. Validación y aprobación
- 5.1 Validación con empresas y universidades piloto
- 5.2 Presentación al Comité Técnico de CONOCER
- 5.3 Publicación en el DOF e inscripción en el RENEC
- 5.4 Acreditación del EC en el centro evaluador / ECE

### Bloque 6. Paquete comercial (fuera del EC)
- 6.1 Curso de alineación EC-A (con constancia DC-3)
- 6.2 Curso de alineación EC-B
- 6.3 Diagnóstico empresarial de uso de IA
- 6.4 Plantilla de política de uso de IA
- 6.5 Convenio tipo con universidades

---

## Documentos de la familia
- `01-mapa-funcional.md` – Mapa funcional y delimitación frente al RENEC
- `02-EC-A-borrador.md` – Borrador completo del EC-A en formato F21-COOPYD-01

## Decisiones pendientes
1. Confirmar niveles SNC con CONOCER.
2. Confirmar que el EC-A no duplique estándares existentes en el RENEC.
3. Definir integrantes del Comité de Gestión por Competencias.
4. ~~Títulos de los EC de IA del DOF del 7-ago-2026~~ (resuelto: EC1827, EC1828, EC1829, sin traslape).
6. Definir si se registra como EC (abierto) o como ECM (Estándar de Competencia de Marca).
5. Confirmar si la evaluación del EC-A puede aplicarse a distancia (clave para volumen).
