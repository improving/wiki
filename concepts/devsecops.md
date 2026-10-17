---
title: "DevSecOps"
type: "Concept"
description: "Embedding security into DevOps culture and pipelines rather than bolting it on as a final gate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, devops, culture]
sources:
  - "/sources/devsecops-still-matters.md"
  - "/sources/a-security-model-for-developers.md"
  - "/sources/how-to-keep-a-secret.md"
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# DevSecOps

DevSecOps extends DevOps' shared-responsibility model to security, so security answers "how" instead of "no" and becomes everyone's job rather than a last-minute gate. It is not a passing trend but a durable culture change: the ideas that made DevOps valuable apply just as well to security, provided leadership treats security as part of its culture. Automation carries the load — SAST and DAST in the pipeline, and security rules expressed as configuration alongside infrastructure and configuration as code.

## Key Claims

- DevOps began as a thing you do — open, shared communication between development and operations — not a role or a product; DevSecOps adds security to that model.
- SAST runs during the build against source code; DAST runs post-deployment (usually pre-production) against a live application.
- Security rules live in "Security as Code" configuration files, alongside Infrastructure as Code and Configuration as Code.
- Every role has a security part: product owners, UX, architects, developers, testers, and operations.
- If security is not part of leadership's culture, it will fail when deadlines force cuts; adoption needs a champion, an inventory of existing practices ([OWASP](/entities/owasp.md) training, [SOC 2 Type II](/entities/soc-2-type-ii.md), ISO 27001), and a prioritized roadmap.
- Shift-left in practice: threat modeling, secret scanners such as TruffleHog in pre-commit hooks, and keyless artifact signing bound to organizational identity.
- The developer model chains policy → standard → principle → guideline → requirements → user story → test case, turning secure-design principles like least privilege into testable requirements.

## Related

- [DevOps](/concepts/devops.md) — the shared-responsibility foundation
- [shift-left security](/concepts/shift-left-security.md) — moving checks earlier in the lifecycle
- [secrets management](/concepts/secrets-management.md) — credential handling in code
- [application security](/concepts/application-security.md) — finding and fixing vulnerabilities across delivery
- [software supply chain security](/concepts/software-supply-chain-security.md) — securing dependencies and artifacts
- [OWASP](/entities/owasp.md) — training and cheat sheets cited as foundations
