---
title: "Blue Cross Blue Shield of Minnesota"
type: "Entity"
description: "A health insurer whose Databricks medallion platform is cited as a case study in embedded, runtime-enforced data governance."
created: '2026-10-17'
updated: '2026-10-17'
tags: [case-study, data-governance, healthcare]
sources:
  - "/sources/ai-governance-is-data-governance-with-consequences.md"
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
---

# Blue Cross Blue Shield of Minnesota

Blue Cross Blue Shield of Minnesota (BCBSM) appears throughout this corpus as the concrete case study for [embedded governance](/concepts/embedded-governance.md): governance encoded into a [Databricks](/entities/databricks.md) medallion platform with [Unity Catalog](/entities/unity-catalog.md) and an onboarding framework, rather than documented in a policy binder.

## Overview

The pattern the posts draw from BCBSM is [federated computational governance](/concepts/data-mesh.md) — the principle most organizations skip — where enforcement happens at runtime instead of in committees. It also grounds the argument that [AI governance](/concepts/ai-governance.md) is data governance with consequences, because regulators can now audit the training data lineage behind a model.

## Key Claims

- Unity Catalog and MLflow Model Registry gave BCBSM auditable training data lineage.
- Governance must be enforced computationally at runtime, not through review committees.
- Domain engineers often do not know which data are protected or regulated, creating an accountability gap.
- EU AI Act Article 10 imposes data quality requirements on high-risk training data, making lineage auditable.
- NIST AI RMF omits explicit data governance references and data steward roles, so platform-level lineage fills a gap the framework leaves open.

## Related

- [Embedded Governance](/concepts/embedded-governance.md) — the strategy BCBSM embodies
- [Unity Catalog](/entities/unity-catalog.md) — the lineage and policy layer
- [Data Mesh](/concepts/data-mesh.md) — federated governance as the hardest principle
- [AI Governance](/concepts/ai-governance.md) — the consequence-bearing framing
- [AI Governance Is Data Governance With Consequences](/sources/ai-governance-is-data-governance-with-consequences.md) — primary source
