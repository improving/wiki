---
title: "zero trust security"
type: "Concept"
description: "Verifying every request as if the network is already breached, with least privilege and continuous checks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, platform, identity]
sources:
  - "/sources/improving-microsoft-services-team-security-and-zero-trust.md"
  - "/sources/a-security-model-for-developers.md"
  - "/sources/how-to-keep-a-secret.md"
  - "/sources/your-agents-have-keys-nobody-changed-the-locks.md"
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# zero trust security

Zero trust security replaces trust-by-default with trust-by-exception: every request is verified as though the network is already breached, and access is granted at the least privilege each action needs. It became urgent as remote and mobile work forced organizations to secure applications, data, devices, and people beyond a perimeter that no longer exists. The model extends naturally to AI agents, which are credentialed non-human identities with a blast radius of their own but are rarely governed like employees.

## Key Claims

- Microsoft's three guiding principles: verify explicitly, use least-privilege access (Just-In-Time and Just-Enough-Access), and assume breach.
- Those principles are backed by seven pillars: secure identity, endpoints, applications, data, infrastructure, networks, and visibility/automation/orchestration.
- Case: Towpath Credit Union used Defender for Endpoint for real-time monitoring and Intune to enforce device policies, blocking access to critical business systems when deviations were detected.
- The developer model chains policy → standard → principle → guideline → requirements → user story → test case, so secure design becomes testable rather than an acronym.
- Agents are non-human identities: 92% of enterprise security leaders lack full visibility into what their AI agents can access and 86% enforce no access policies on them at all.
- The human identity lifecycle applies to agents — provision with least privilege, audit regularly, revoke on change — and the gap is assumption, not tooling.
- A signature proves a key was used, not that the signer is currently trusted; self-hosting Fulcio against a [Keycloak](/entities/keycloak.md) realm binds certificates to managed identity, so offboarding propagates.

## Related

- [DevSecOps](/concepts/devsecops.md) — security woven into delivery rather than bolted on
- [secrets management](/concepts/secrets-management.md) — eliminating and scoping credentials
- [least privilege](/concepts/least-privilege.md) — the access principle at the core
- [agent identity](/concepts/agent-identity.md) — agents as governed non-human principals
- [software supply chain security](/concepts/software-supply-chain-security.md) — verifying the signer, not just the signature
- [Microsoft](/entities/microsoft.md) — owner of the Zero Trust framework described
- [Sigstore](/entities/sigstore.md) — keyless signing bound to identity
