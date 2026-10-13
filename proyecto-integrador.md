# Proyecto Integrador — DPL1046

**Programación en Python y Manipulación de Datos** · Diplomado en Ingeniería de Datos con Python · UDLA

El proyecto integrador es la **evaluación central del curso (100% del examen)**. Construyes un **pipeline de datos completo en Python**, que corre **localmente en tu computador**, sobre el dataset del curso (Olist). Se desarrolla en equipo a lo largo de las tres unidades y se presenta en la **Clase 9**.

---

## Cómo funciona

- **Equipos de 4 personas.**
- Cada equipo **elige uno de los 10 temas** de abajo, todos sobre el **dataset del curso (Olist Brazilian E-Commerce)**.
- El tema se desarrolla en **tres entregas**, una por unidad, que se van construyendo en las prácticas de cada clase.
- **Opcional (suma valor):** complementar el análisis con un **dataset propio** (datos.gob.cl, INE, Banco Central, CMF, Kaggle, etc.) o con una **API externa**.
- **La IA es tu copiloto, no tu piloto:** puedes y se espera que la uses como asistente de código, pero tienes que entender y poder explicar cada parte de lo que entregas.
- Tu proyecto **no se sube a este repositorio**: este repo es del profesor y sirve para recibir el material de las clases. La entrega se hace como indique el profesor (Blackboard u otro).

---

## Los 10 temas

Todos usan las 9 tablas de Olist (órdenes, ítems, pagos, reseñas, productos, vendedores, clientes, geolocalización, traducción de categorías). El "ángulo IA" es una **idea opcional** para enriquecer el proyecto con IA local (Clase 8).

**1. Radar de satisfacción del cliente**
Analizar las reseñas (puntaje + comentario) por categoría y vendedor. *Tablas:* reviews, order_items, products. *Ángulo IA:* clasificar sentimiento y temas de los comentarios.

**2. Mapa logístico de entregas**
Tiempos de entrega (estimado vs real) y retrasos por región/estado. *Tablas:* orders, customers, geolocation. *Ángulo IA:* resumen ejecutivo automático de cuellos de botella.

**3. Segmentación de clientes (RFM)**
Recencia, frecuencia y monto para identificar clientes valiosos. *Tablas:* orders, order_payments, customers. *Ángulo IA:* describir en lenguaje natural cada segmento.

**4. Performance de vendedores**
Ranking de sellers por ventas, flete, reseñas y tiempos de despacho. *Tablas:* sellers, order_items, reviews. *Ángulo IA:* generar "fichas" de vendedor a partir de sus métricas.

**5. Análisis de métodos de pago**
Uso de tarjeta/boleto/voucher, cuotas y ticket por medio de pago. *Tablas:* order_payments, orders. *Ángulo IA:* detectar patrones y explicarlos.

**6. Pronóstico de demanda / ventas**
Serie de tiempo de ventas por categoría y mes, con estacionalidad. *Tablas:* orders, order_items, products. *Ángulo IA:* narrar tendencias y anomalías detectadas.

**7. Análisis de categorías de producto**
Qué categorías venden más, su flete y cómo se evalúan. *Tablas:* products, category_translation, order_items, reviews. *Ángulo IA:* clasificar productos sin categoría a partir de su descripción.

**8. Geografía de ventas**
Ventas por estado/ciudad y relación distancia cliente-vendedor vs flete. *Tablas:* geolocation, customers, sellers, order_items. *Ángulo IA:* resumen regional automático.

**9. Detección de órdenes en riesgo**
Predecir cancelaciones, retrasos o malas reseñas. *Tablas:* orders, order_items, reviews. *Ángulo IA:* clasificar el riesgo de una orden y explicar el porqué.

**10. Dashboard 360 del negocio**
Panorama ejecutivo con KPIs integrales (GMV, ticket promedio, satisfacción, entregas, top categorías). *Tablas:* todas. *Ángulo IA:* generar el "resumen para gerencia" del dashboard.

---

## Entregables por unidad

| Unidad | Entregable |
|---|---|
| **Unidad 1 (Clases 1–3)** | Script que lee ≥2 tablas/fuentes del dataset, valida la calidad de los datos y genera un reporte básico del tema elegido. |
| **Unidad 2 (Clases 4–6)** | Pipeline ETL con pandas: limpieza, transformación y carga a Parquet o base de datos local (SQLite/PostgreSQL). Logging, tests y configuración externalizada. |
| **Unidad 3 (Clases 7–9)** | Pipeline integrado: ≥2 fuentes (idealmente una API externa) y resultados en formato ejecutivo. Un componente de IA local suma valor. |

---

## Rúbrica de evaluación

| Criterio | Peso | Qué se evalúa |
|---|---|---|
| Funcionalidad del pipeline | 35% | Corre de principio a fin con un solo comando, integra ≥2 fuentes (ingesta + transformación + salida) y entrega resultados reproducibles. |
| Calidad del código | 30% | Código modular y legible (PEP 8, docstrings), `try/except` + logging, tests con `pytest` (≥3 por función de transformación) y dominio del propio código. |
| Buenas prácticas | 15% | Rutas relativas y configuración externalizada, `requirements.txt`, estructura clara con README, pipeline idempotente, sin credenciales en el código. |
| Presentación y valor de negocio | 20% | Problema → solución → valor, 15 minutos + 5 de preguntas, demo del pipeline funcionando. |

Aprobación: nota 4,0 · asistencia mínima de 70% a las sesiones sincrónicas.

Un ejemplo completo de proyecto que cumple la rúbrica, y la revisión de esta rúbrica, se trabajan en la Clase 8.

---

## Checklist de entrega

- [ ] Carpeta del proyecto con el pipeline en Python (scripts organizados).
- [ ] Corre localmente en VS Code, de principio a fin, con un comando.
- [ ] Al menos 2 fuentes/tablas de Olist integradas.
- [ ] Validación de datos + manejo de errores con logging.
- [ ] Tests con `pytest` (incluye la salida de `pytest -v` en el README).
- [ ] `requirements.txt` con las dependencias.
- [ ] README claro: qué hace, cómo instalarlo y cómo ejecutarlo.
- [ ] Presentación final (15 min) basada en el template del curso.

---

## Presentación final (Clase 9)

Formato demo ejecutiva: **problema de negocio → datos → arquitectura → demo del pipeline → resultados → valor generado**. **15 minutos por equipo + 5 de preguntas.**
