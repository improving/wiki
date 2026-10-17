---
title: "CI/CD"
type: "Concept"
description: "Automated integration and delivery pipelines that build, test, and deploy on every change — and the scaffolding they encode."
created: '2026-10-17'
updated: '2026-10-17'
tags: [devops, platform, delivery]
sources:
  - "/sources/your-ci-cd-pipeline-is-already-cognitive-scaffolding.md"
  - "/sources/from-ci-cd-to-the-intelligence-operating-system.md"
  - "/sources/multiple-environments-with-terraform.md"
  - "/sources/leveraging-multi-and-hybrid-architectures-for-next-gen-platform.md"
  - "/sources/platform-engineering-excellence-streamlining-cloud-data-and-app.md"
---

# CI/CD

CI/CD automates integration and delivery so every change is built, tested, and deployed by a pipeline rather than by hand. Beyond efficiency, the pipeline is cognitive scaffolding in Edwin Hutchins' distributed-cognition sense: version control, automated tests, and continuous delivery encode a team's history, expected behavior, and operational knowledge in executable form, so that knowledge survives attrition and compounds. The same delivery mental models — source control, CI, CD, progressive delivery, and observability — transfer directly to governing AI agent pipelines.

## Key Claims

- The delivery-to-governance mapping: version control ↔ audit trails, automated tests ↔ quality gates, CI/CD ↔ agent boundaries, and PR review ↔ human approval points.
- CI's broken-build rule becomes: surface failures at the earliest pipeline stage and treat a degraded quality gate as a broken build.
- Progressive delivery separates deployment from release — the model for scoping agent autonomy to a population, task class, or risk level and extending it as trust is earned.
- Organizations with strong delivery scaffolding are best positioned to build strong AI governance scaffolding, because the discipline transfers rather than starting from scratch.
- CI/CD is a pillar of the [internal developer platform](/concepts/internal-developer-platform.md), alongside version control (Git), cloud, [infrastructure as code](/concepts/infrastructure-as-code.md) (Terraform), observability, and a self-service portal.
- Multi-environment delivery needs environment isolation — global plus per-environment configs (Terragrunt) — rather than Terraform workspaces, and consistent releases across providers in a [multi-cloud](/concepts/multi-cloud.md) setup.

## Related

- [GitOps](/concepts/gitops.md) — Git as the source of truth for delivery
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the other automation pillar
- [DevOps](/concepts/devops.md) — the culture CI/CD operationalizes
- [cognitive scaffolding](/concepts/cognitive-scaffolding.md) — what the pipeline really encodes
- [quality gates](/concepts/quality-gates.md) — the checks the pipeline enforces
- [Jenkins](/entities/jenkins.md) — long-standing CI automation server
