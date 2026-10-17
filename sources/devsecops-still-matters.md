---
title: "DevSecOps Still Matters"
type: "Source Summary"
description: "DevSecOps is no fad but a durable culture change that weaves security into shared responsibility and automated pipelines."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devops, improving.com]
sources:
  - "references/improving.com/devsecops-still-matters/devsecops-still-matters.md"
---

# DevSecOps Still Matters — Summary

**Original source**: `references/improving.com/devsecops-still-matters/devsecops-still-matters.md`

## Summary

Erik Boemanns argues DevSecOps is not a passing trend: the core ideas that made DevOps valuable extend to security, which must become everyone's responsibility rather than a last-minute gate. He describes how SAST and DAST automation plus "Security as Code" enforce secure practices without slowing delivery, and frames adoption as a culture change that needs leadership buy-in and a champion.

## Key Claims

- DevOps began as a thing you do — open, shared communication between development and operations — not a role or product.
- DevSecOps adds security to that shared-responsibility model, so security answers "how" instead of "no."
- SAST runs during the build against source code; DAST runs post-deployment (usually pre-production) against a live application.
- Security rules live in "Security as Code" configuration files, alongside Infrastructure as Code and Configuration as Code.
- Every role has a security part: product owners, UX, architects, developers, testers, and operations.
- If security is not part of leadership's culture, it will inevitably fail when deadlines force cuts.
- Adoption needs a champion, an inventory of existing practices (OWASP training, SOC 2, ISO 27001), and a prioritized roadmap that addresses each stakeholder's concerns.

## Relevance

Informs [DevSecOps](/concepts/devsecops.md), [shift-left security](/concepts/shift-left-security.md), and [security culture](/concepts/security-culture.md), building on the shared-responsibility ideas of [DevOps](/concepts/devops.md).

## Quality

Practitioner explainer by Erik Boemanns, based on an Improving webinar; sound on concepts and culture, light on tool specifics.

## Entities Mentioned

- [OWASP](/entities/owasp.md) — training cited as a foundation for secure coding
- [SOC 2 Type II](/entities/soc-2-type-ii.md) — existing audit named as a DevSecOps foundation
- [Improving](/entities/improving.md) — consultancy offering DevSecOps adoption help

## Concepts Covered

- [DevSecOps](/concepts/devsecops.md) — security woven into DevOps practices
- [shift-left security](/concepts/shift-left-security.md) — SAST/DAST in the build and release lifecycle
- [security culture](/concepts/security-culture.md) — shared responsibility and leadership buy-in
- [DevOps](/concepts/devops.md) — the shared-responsibility foundation DevSecOps extends
