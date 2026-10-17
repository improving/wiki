---
title: "secrets management"
type: "Concept"
description: "Reducing and controlling credentials through elimination first, then scoping, then proactive leak detection."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, platform, identity]
sources:
  - "/sources/how-to-keep-a-secret.md"
  - "/sources/your-agents-have-keys-nobody-changed-the-locks.md"
  - "/sources/cloud-computing-in-2024-the-complete-guide.md"
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# secrets management

Secrets management is the practice of reducing and controlling credentials — passwords, client secrets, API keys, and PII — across the development lifecycle. It is never "solved" by a single mechanism, because every storage choice trades one risk for another; the highest-leverage move is to eliminate secrets entirely, then scope what remains, then detect leaks proactively. The discipline now extends to AI agents, which hold keys with real blast radius but are often exempted from the identity lifecycle that governs employees.

## Key Claims

- Not all secrets are alike: passwords are hashed (bcrypt/scrypt), client secrets must be decryptable on the server, and PII should be stored minimally and deleted quickly.
- Every threat gets one of four decisions: accept, eliminate, mitigate, or transfer.
- Eliminate by deleting old PII, using identity-based access (managed identity) instead of client secrets, and having build servers cause deployment via a queue and Function rather than hold infrastructure credentials.
- FIDO keys are phishing-resistant; SMS MFA is not. Delegate password handling to [Okta](/entities/okta.md), [Entra ID](/entities/entra-id.md), or Authentik.
- Detect with canary tokens for proactive leak alerts, secret scanners such as TruffleHog in pre-commit hooks, and vault API access rather than environment variables, to avoid exposure through tools like Spring Boot Actuator.
- Even competent practice fails: threat actor Storm-0558 forged tokens through a compromised [Microsoft](/entities/microsoft.md) key, and long-lived signing keys can leak for their whole lifetime.
- Supply-chain mitigation means rotating keys and credentials regularly and encrypting and securely storing secrets; agents need the same provisioning, auditing, and revocation as people.

## Related

- [least privilege](/concepts/least-privilege.md) — narrowing the blast radius of what remains
- [zero trust security](/concepts/zero-trust-security.md) — assuming compromise and verifying every request
- [DevSecOps](/concepts/devsecops.md) — secret scanning in the delivery pipeline
- [application security](/concepts/application-security.md) — secret handling in code
- [software supply chain security](/concepts/software-supply-chain-security.md) — key rotation and artifact signing
- [Entra ID](/entities/entra-id.md) — delegated identity service for credential handling
