---
title: "data debt"
type: "Concept"
description: "The accumulated cost of unreliable, undocumented data that quietly degrades analytics and AI."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, quality, governance]
sources:
  - "/sources/data-debt-ai-predictions.md"
  - "/sources/empowering-your-data-estate-modern-practices-for-data-quality.md"
---

# data debt

Data debt is the accumulated cost of unreliable, inconsistent, or poorly governed data, which compounds like technical debt and hides behind green pipelines. The AI bottleneck has shifted from model capability to data reliability: better models do not fix bad inputs, because models overfit system-level noise and offline metrics can improve while production reliability degrades.

## Key Claims

- Data debt accumulates through ignored data quality, schema drift, weak lineage, fragmented ownership, poor labeling, and brittle transformation pipelines.
- Failures are silent: pipelines stay green and dashboards update while feature distributions diverge between training and inference.
- A recommendation system degraded not because the model was weak but because an upstream service changed its definition of "active users" while a feature pipeline kept serving stale values for nearly a month, leaving half the training data on the old definition and inference on the new one.
- Three telltale signs: accurate tests but wrong-feeling production predictions, recurring issues after every retrain, and dashboards disagreeing on the same metric.
- Failure patterns differ by architecture — forecasting hits schema drift and inconsistent features; RAG hits stale embeddings and corrupted documents; tool-using agents hit conflicting API definitions.
- Prescriptions: data contracts at producer-consumer boundaries, validation at ingestion, and observability and lineage for traceability.
- Self-check questions: can predictions be traced to source, are feature definitions versioned, and is there a single source of truth for core entities?

## Related

- [data quality](/concepts/data-quality.md) — the engineered property that prevents it
- [data lineage](/concepts/data-lineage.md) — the traceability that surfaces it
- [data readiness](/concepts/data-readiness.md) — data maturity bounds AI maturity
- [schema drift](/concepts/schema-drift.md) — one of its recurring mechanisms
