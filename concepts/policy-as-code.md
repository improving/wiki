---
title: "Policy as Code"
type: "Concept"
description: "Encoding governance rules as executable checks enforced by systems at runtime, instead of documents enforced by committees after the fact."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, automation, compliance]
sources:
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
  - "/sources/the-policy-binder-didnt-change-anyones-behavior.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
  - "/sources/your-ai-governance-policy-is-not-governance.md"
  - "/sources/your-stakeholders-are-your-data-quality-system.md"
---

# Policy as Code

Policy as code turns governance rules into executable, versioned checks that systems run at build time and runtime. This corpus treats it as the only form of policy that survives contact with agents acting at machine speed, where a document cannot see, stop, or detect a violation.

## Key Claims

- A policy document cannot see, stop, or detect violations; a runtime control plane can.
- Agentic chains execute in milliseconds, so post-hoc governance is impossible; active governance needs rules, gating, behavior, and evidence at runtime.
- 91% of organizations deployed agents but only 10% have a governance strategy; indirect prompt injection is OWASP's top LLM risk, so permissions — not the model — are the perimeter.
- Governance must be enforced computationally rather than through committees, which is data mesh's hardest principle; domain engineers often do not know which data are protected.
- dbt Core v1.5 access, contracts, and versions enforce governance at build time.
- Manual tests scale with engineering time while the data estate grows faster, so governance has to run as code and observability.

## Related

- [Data Governance](/concepts/data-governance.md) — the program policy-as-code executes
- [AI Governance](/concepts/ai-governance.md) — policy for agents at machine speed
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the enforcement layer
- [Boundary enforcement](/concepts/boundary-enforcement.md) — the architectural form of the same idea
- [Embedded Governance](/concepts/embedded-governance.md) — governance inside the platform
- [Your AI Governance Policy Is Not Governance](/sources/your-ai-governance-policy-is-not-governance.md) — primary source
