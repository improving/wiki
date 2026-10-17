---
title: "AI Governance Is Data Governance With Consequences"
type: "Source Summary"
description: "AI governance is really data governance under regulatory pressure, with EU AI Act Article 10 and NIST AI RMF exposing the data foundation gap."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/ai-governance-is-data-governance-with-consequences/ai-governance-is-data-governance-with-consequences.md"
---

# AI Governance Is Data Governance With Consequences — Summary

**Original source**: `references/devlinliles.com/ai-governance-is-data-governance-with-consequences/ai-governance-is-data-governance-with-consequences.md`

## Summary

Framing AI governance as separate from data governance is a mistake that organizations will discover the hard way when the EU AI Act's high-risk obligations activate on August 2, 2026. Article 10 requires high-risk training, validation, and testing datasets to be relevant, representative, and as error-free as possible — a data governance requirement with fines up to €35 million or 7% of global turnover. NIST's AI RMF organizes risk around Govern, Map, Measure, Manage but never explicitly references data governance or data stewards, leaving its Map and Measure functions aspirational without lineage infrastructure. The BCBSM/Databricks case shows governed AI built on Unity Catalog lineage.

## Key Claims

- EU AI Act high-risk obligations activate August 2, 2026; Article 10 imposes data quality requirements with fines up to €35 million or 7% of global turnover.
- Gartner found 63% of organizations either lacking or unsure about their data management practices for AI.
- Forrester found data governance has no explicit reference in NIST AI RMF, and data stewards are missing from its defined roles.
- At BCBSM, Unity Catalog plus the MLflow Model Registry gave an auditable answer to what data trained a model and who approved its deployment.
- Gartner predicts organizations will abandon 60% of AI projects unsupported by AI-ready data through 2026; poor data quality costs $12.9 million per year.

## Relevance

Core to [AI governance](/concepts/ai-governance.md) and [data governance](/concepts/data-governance.md), and a direct argument against [bolt-on governance](/concepts/bolt-on-governance.md).

## Quality

Practitioner blog post by Devlin Liles. Draws on named sources and a real client case (BCBSM); the case is single-organization evidence and several figures are framework or vendor citations rather than independent research.

## Entities Mentioned

- [EU AI Act](/entities/eu-ai-act.md) — Article 10 supplies the binding data-quality obligations
- [NIST AI RMF](/entities/nist-ai-rmf.md) — cited for its missing data governance reference
- [Unity Catalog](/entities/unity-catalog.md) — the governance mechanism enabling auditable model lineage at BCBSM
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — the regulated client case study
- [Gartner](/entities/gartner.md) — source of the 63% and 60% statistics

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — argued to be inseparable from data governance
- [Data Governance](/concepts/data-governance.md) — the foundation regulators actually ask about
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the passive variety declared structurally insufficient

## Related Sources

- [Before You Architect Anything, Agree on What the AI Actually Does](/sources/before-you-architect-anything-agree-on-what-the-ai-actually-does.md)
- [Data Is Not the Goal: The Knowledge-Insight-Action Chain](/sources/data-is-not-the-goal-the-knowledge-insight-action-chain.md)
- [Same Model, Different Outcome — Who's Responsible?](/sources/same-model-different-outcome-whos-responsible.md)
- [Somebody Has to Own the Skill Library](/sources/somebody-has-to-own-the-skill-library.md)
- [The Most Important Person in Your AI Governance Program Isn't in Your C-Suite](/sources/the-most-important-person-in-your-ai-governance-program-isnt-in-your-c-suite.md)
