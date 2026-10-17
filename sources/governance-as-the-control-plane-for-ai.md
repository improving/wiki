---
title: "Governance as the Control Plane for AI"
type: "Source Summary"
description: "AI governance is data governance with the safety margin removed; the fix is a runtime control plane, not a policy document."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/governance-as-the-control-plane-for-ai/governance-as-the-control-plane-for-ai.md"
---

# Governance as the Control Plane for AI — Summary

**Original source**: `references/devlinliles.com/governance-as-the-control-plane-for-ai/governance-as-the-control-plane-for-ai.md`

## Summary

Devlin Liles argues that data governance failed for structural reasons — a policy document is not a system — and that those reasons compound when an agent, not a person, consumes ungoverned data at machine speed. AI governance, he contends, is data governance with the safety margin removed, and the fix in both cases is to build a [control plane](/concepts/control-plane.md) instead of writing policy. He traces the arc from active metadata through data contracts and federated enforcement to a four-layer runtime governance architecture, anchored by the catalog as the control plane.

## Key Claims

- Only 8% of organizations with a formal governance program rated it highly successful (TDWI, 2020); the top barrier was getting employees to adhere, because policy was never in the room when an engineer built a pipeline.
- A data contract makes the producer responsible for what they publish: a pipeline violating its declared contract fails the build, caught at the producer rather than the consumer.
- The four runtime layers are policy and compliance, [AI inventory](/concepts/ai-inventory.md), [model monitoring and drift detection](/concepts/model-drift-detection.md), and [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — a dependency chain you cannot skip.
- EU AI Act Article 10 makes training-data quality a governance requirement (fines up to €35M or 7% of turnover, from August 2, 2026); NIST's AI RMF has no explicit data-governance reference.
- An agent completing each step correctly 95% of the time has roughly a 36% chance of finishing a twenty-step chain error-free.
- METR's March 2026 study found ~half of 296 automated-grader-approved PRs would not have been merged by human maintainers, a 24-point gap that did not shrink as models improved.

## Relevance

Synthesizes [Embedded Governance](/concepts/embedded-governance.md), [Runtime Lineage](/concepts/runtime-lineage.md), and [Data Governance](/concepts/data-governance.md) into an [AI Governance](/concepts/ai-governance.md) architecture.

## Quality

Practitioner blog post by Devlin Liles. Broad and well-cited with named studies and client cases; the argument is synthetic and persuasive, leaning on illustrative examples.

## Entities Mentioned

- [Unity Catalog](/entities/unity-catalog.md) — the catalog acting as the governance control plane
- [Microsoft Purview](/entities/microsoft-purview.md) — suggested layer-one default for Microsoft-centric organizations
- [NIST AI RMF](/entities/nist-ai-rmf.md) — voluntary framework lacking explicit data-governance reference
- [EU AI Act](/entities/eu-ai-act.md) — Article 10 data requirements and penalties
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — large-scale governed-AI client case
- [METR](/entities/metr.md) — study comparing automated grading to human review
- [Databricks](/entities/databricks.md) — platform hosting the catalog and client work
- [Snowflake](/entities/snowflake.md) — Horizon as a competing embedded catalog
- [Gartner](/entities/gartner.md) — 2024 80%-failure prediction and metadata reframe
- [Collibra](/entities/collibra.md) — catalog integrated into the DHCS pipeline

## Concepts Covered

- [Control plane](/concepts/control-plane.md) — the central architectural argument
- [AI Inventory](/concepts/ai-inventory.md) — layer two, discovering unknown AI usage
- [Model Drift Detection](/concepts/model-drift-detection.md) — layer three, continuous monitoring
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — layer four, gating actions before execution
- [Data Contract](/concepts/data-contract.md) — producer accountability enforced at build time
- [Embedded Governance](/concepts/embedded-governance.md) — governance inside the platform
- [Data Governance](/concepts/data-governance.md) — the discipline AI governance extends
- [Active Metadata](/concepts/active-metadata.md) — metadata captured as a byproduct of operation
- [Runtime Lineage](/concepts/runtime-lineage.md) — lineage observed at query execution
- [Data Mesh](/concepts/data-mesh.md) — federated computational governance principle
- [Audit Trail](/concepts/audit-trail.md) — records generated at the decision itself
- [Agent identity](/concepts/agent-identity.md) — least-privilege scope enforced by the catalog
- [Stacking Errors](/concepts/stacking-errors.md) — why long agent chains need runtime gating
- [Evaluation harness](/concepts/evaluation-harness.md) — the evaluation-governance flywheel baseline
- [AI Governance](/concepts/ai-governance.md) — the overall frame
