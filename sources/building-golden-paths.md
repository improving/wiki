---
title: "Everyone Talks About Golden Paths. Nobody Talks About Building Them"
type: "Source Summary"
description: "A maturity-first playbook for building a golden path incrementally — standardize, validate, GitOps, self-service — without a big platform team or budget."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, developer-experience, improving.com]
sources:
  - "references/improving.com/building-golden-paths/building-golden-paths.md"
---

# Everyone Talks About Golden Paths. Nobody Talks About Building Them — Summary

**Original source**: `references/improving.com/building-golden-paths/building-golden-paths.md`

## Summary

Conference talks explain why you need a platform and golden paths but rarely how to build one without a large team or budget, leaving most teams stuck staring at a mess of legacy deployment scripts. Atulpriya Sharma, writing up his KubeCon Europe 2026 Platform Engineering Day talk, argues you don't need a full IDP to start: a golden path is an opinionated, self-service, safe-by-default, progressive route to production that should be treated as a product, not a mandate. He maps the CNCF Platform Engineering Maturity Model's five pillars onto a four-phase construction sequence — standardize, validate, GitOps, self-service — where the interface changes but the logic doesn't.

## Key Claims

- A golden path is not "done" unless it is opinionated, self-service, safe by default, and progressive.
- Most teams are already in Phase 0 (chaos): ten scripts with ten different outcomes, images pinned to latest, missing resource limits and health checks.
- Phase 1 (Standardize) is the most important and easiest to ship: pick one template every team uses, enforcing resource limits, health checks, labels, and namespaces by default.
- Phase 2 (Validate) moves to a declarative, config-driven interface where a validation layer rejects bad configs early with clear errors.
- Phase 3 (GitOps) changes only the last step — a git push instead of kubectl apply, with a CD tool like ArgoCD watching the repo — giving audit trails and rollback for free.
- Phase 4 (IdP and self-service) wraps the same logic in a portal form, so any developer can deploy safely without YAML or kubectl.
- The approach earns ROI on day one, reduces cognitive load, earns developer trust by meeting them where they are, and gives leadership predictable, measurable language.
- The complete demo is available in a public Git repository designed as a forkable template.

## Relevance

A practical treatment of [golden paths](/concepts/golden-path.md) within [platform engineering](/concepts/platform-engineering.md), tied to the [internal developer platform](/concepts/internal-developer-platform.md) and [internal developer portal](/concepts/internal-developer-portal.md), and grounded in [GitOps](/concepts/gitops.md) and reduced [cognitive load](/concepts/cognitive-load.md).

## Quality

Practitioner playbook by Atulpriya Sharma; unusually concrete with phases, sample configs, and a demo repo, though based on a single conference talk.

## Entities Mentioned

- [Atulpriya Sharma](/entities/atulpriya-sharma.md) — author
- [KubeCon](/entities/kubecon.md) — venue for the original talk
- [CNCF](/entities/cncf.md) — Platform Engineering Maturity Model
- [Argo CD](/entities/argo-cd.md) — GitOps delivery tool
- [Kubernetes](/entities/kubernetes.md) — deployment target

## Concepts Covered

- [golden path](/concepts/golden-path.md) — the post's core subject
- [platform engineering](/concepts/platform-engineering.md) — the discipline
- [internal developer platform](/concepts/internal-developer-platform.md) — the destination
- [internal developer portal](/concepts/internal-developer-portal.md) — self-service interface
- [GitOps](/concepts/gitops.md) — Git as source of truth
- [developer experience](/concepts/developer-experience.md) — reducing friction
- [cognitive load](/concepts/cognitive-load.md) — psychology of safe defaults
