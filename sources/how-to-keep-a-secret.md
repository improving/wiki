---
title: "How to Keep a Secret"
type: "Source Summary"
description: "The best way to keep secrets is to have fewer of them — eliminate, then scope, then detect — because every storage mechanism trades one risk for another."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, improving.com]
sources:
  - "references/improving.com/how-to-keep-a-secret/how-to-keep-a-secret.md"
---

# How to Keep a Secret — Summary

**Original source**: `references/improving.com/how-to-keep-a-secret/how-to-keep-a-secret.md`

## Summary

A developer argues that secret management is never "solved" by a single mechanism; the highest-leverage move is to eliminate secrets entirely, then scope what remains, and finally detect leaks proactively. It separates secret classes and maps each to a threat-model decision.

## Key Claims

- Not all secrets are alike: passwords, client secrets, trade secrets, and PII have different storage rules — passwords are hashed (bcrypt/scrypt), client secrets must be decryptable on the server, and PII should be stored minimally and deleted quickly.
- Every threat gets one of four decisions: accept, eliminate, mitigate, or transfer.
- Even competent practices fail: threat actor Storm-0558 forged tokens through a compromised Microsoft key to reach Exchange mailboxes.
- Eliminate secrets by deleting old PII, using identity-based access (managed identity) instead of client secrets, and having build servers cause deployment via a queue and Function rather than hold infrastructure credentials.
- FIDO keys are phishing-resistant; SMS MFA is not. Third-party services (Okta, Entra ID, Authentik) can delegate password handling.
- Use canary tokens for proactive leak alerts, secret scanners (TruffleHog) in pre-commit hooks, and vault API access rather than environment variables to avoid exposure via tools like Spring Boot Actuator.

## Relevance

A practical treatment of [secrets management](/concepts/secrets-management.md), [least privilege](/concepts/least-privilege.md), and [zero trust security](/concepts/zero-trust-security.md) across the development lifecycle.

## Quality

Deep, opinionated longread by an Improving developer; concrete and well-referenced, with some vendor recommendations.

## Entities Mentioned

- [Microsoft](/entities/microsoft.md) — Storm-0558 key compromise example
- [GitHub](/entities/github.md) — Actions environment secrets
- [Jenkins](/entities/jenkins.md) — build server with a checkered security record
- [Okta](/entities/okta.md) — delegated identity service
- [Entra ID](/entities/entra-id.md) — delegated identity service
- [AWS](/entities/aws.md) — client-secret and canary-token examples
- [OWASP](/entities/owasp.md) — Secrets Management Cheat Sheet

## Concepts Covered

- [secrets management](/concepts/secrets-management.md) — main topic
- [least privilege](/concepts/least-privilege.md) — narrowing blast radius and scope
- [zero trust security](/concepts/zero-trust-security.md) — assume compromise
- [application security](/concepts/application-security.md) — secret handling in code
- [software supply chain security](/concepts/software-supply-chain-security.md) — secret scanning and trade secrets
- [shift-left security](/concepts/shift-left-security.md) — pre-commit scanning and threat modeling
