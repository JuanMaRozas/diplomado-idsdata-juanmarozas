# Proyecto Integrador — DPL1046

**Programación en Python y Manipulación de Datos** · Diplomado en Ingeniería de Datos con Python · UDLA

El proyecto integrador es la **evaluación central del curso (100% del examen)**. Se desarrolla en equipo a lo largo de las tres unidades y se presenta en la **Clase 9**.

---

## Cómo funciona

- **Equipos de 4 personas** (≈7 grupos en el curso).
- Cada equipo **elige uno de los 10 temas** de abajo, todos sobre el **dataset del curso (Olist Brazilian E-Commerce)**.
- El tema se desarrolla en **tres entregas**, una por unidad, que se van construyendo en las prácticas de cada clase.
- **Opcional (suma valor):** complementar el análisis con un **dataset propio** —de los que aprendemos a buscar en la Clase 1 (datos.gob.cl, INE, Banco Central, CMF, Kaggle, etc.)— o con una **API externa** en la Unidad 3.

---

## Los 10 temas

Todos usan las 9 tablas de Olist (órdenes, ítems, pagos, reseñas, productos, vendedores, clientes, geolocalización, traducción de categorías). El "ángulo IA" es el componente de la Unidad 3.

**1. Radar de satisfacción del cliente**
Analizar las reseñas (puntaje + comentario) por categoría y vendedor. *Tablas:* reviews, order_items, products. *IA:* clasificar sentimiento y temas de los comentarios con un LLM.

**2. Mapa logístico de entregas**
Tiempos de entrega (estimado vs real) y retrasos por región/estado. *Tablas:* orders, customers, geolocation. *IA:* resumen ejecutivo automático de cuellos de botella.

**3. Segmentación de clientes (RFM)**
Recencia, frecuencia y monto para identificar clientes valiosos. *Tablas:* orders, order_payments, customers. *IA:* describir en lenguaje natural cada segmento.

**4. Performance de vendedores**
Ranking de sellers por ventas, flete, reseñas y tiempos de despacho. *Tablas:* sellers, order_items, reviews. *IA:* generar "fichas" de vendedor a partir de sus métricas.

**5. Análisis de métodos de pago**
Uso de tarjeta/boleto/voucher, cuotas y ticket por medio de pago. *Tablas:* order_payments, orders. *IA:* detectar patrones y explicarlos.

**6. Pronóstico de demanda / ventas**
Serie de tiempo de ventas por categoría y mes, con estacionalidad. *Tablas:* orders, order_items, products. *IA:* narrar tendencias y anomalías detectadas.

**7. Análisis de categorías de producto**
Qué categorías venden más, su flete y cómo se evalúan. *Tablas:* products, category_translation, order_items, reviews. *IA:* clasificar productos sin categoría a partir de su descripción.

**8. Geografía de ventas**
Ventas por estado/ciudad y relación distancia cliente-vendedor vs flete. *Tablas:* geolocation, customers, sellers, order_items. *IA:* resumen regional automático.

**9. Detección de órdenes en riesgo**
Predecir cancelaciones, retrasos o malas reseñas. *Tablas:* orders, order_items, reviews. *IA:* clasificar el riesgo de una orden y explicar el porqué.

**10. Dashboard 360 del negocio**
Panorama ejecutivo con KPIs integrales (GMV, ticket promedio, satisfacción, entregas, top categorías). *Tablas:* todas. *IA:* generar el "resumen para gerencia" del dashboard.

---

## Entregables por unidad

| Unidad | Entregable |
|---|---|
| **Unidad 1 (Clases 1–3)** | Script que lee el dataset desde ≥2 tablas/fuentes, valida la calidad de los datos y genera un reporte básico del tema elegido. Código en GitHub con README. |
| **Unidad 2 (Clases 4–6)** | Pipeline ETL completo con pandas: limpieza, transformación y carga a Parquet o base de datos en cloud (AWS). Logging, tests y configuración externalizada. |
| **Unidad 3 (Clases 7–9)** | Pipeline integrado: ≥2 fuentes (al menos 1 API externa), un componente de IA (clasificación, extracción o síntesis) y resultados en formato ejecutivo. |

---

## Rúbrica de evaluación

| Criterio | Peso | Qué se evalúa |
|---|---|---|
| Funcionalidad | 30% | El pipeline ejecuta sin errores, procesa el dataset completo y produce los outputs definidos. |
| Calidad del código | 20% | Código limpio, comentado, con manejo de errores, logging y tests. Sigue PEP 8. |
| Buenas prácticas | 15% | Seguridad (sin credenciales en el código), configuración externalizada, idempotencia. |
| Integración cloud | 15% | Al menos una fuente o destino en AWS (S3, Athena o equivalente). |
| Componente IA | 10% | Uso justificado y documentado de IA en el pipeline. |
| Presentación y valor de negocio | 10% | Claridad al comunicar el problema, la arquitectura y los resultados. |

---

## Presentación final (Clase 9)

Formato demo ejecutiva: **problema de negocio → arquitectura → demo del pipeline → resultados → valor generado**. 10–12 minutos por equipo + 5 de preguntas. Hay evaluación entre pares además de la del docente.
