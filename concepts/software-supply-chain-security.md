---
title: "software supply chain security"
type: "Concept"
description: "Securing dependencies, builds, and artifacts against tampering, malicious packages, and compromised maintainers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, devops, platform]
sources:
  - "/sources/software-supply-chain-security-package-age-enforcement.md"
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
  - "/sources/human-cost-security-ai-era.md"
  - "/sources/security-the-thing-that-everyone-loves-to-hate.md"
  - "/sources/owasp-top-10-llm-security-guide.md"
---

# software supply chain security

Software supply chain security protects the path from dependency to running artifact: the packages you install, the build pipeline that compiles them, and the signed binaries you ship. The corpus treats it as the highest-stakes area of [application security](/concepts/application-security.md), because a single compromised link scales — SolarWinds' compromised build pipeline shipped a legitimately signed update to roughly 18,000 organizations, and the xz-utils backdoor was planted by a contributor who spent two years building trust.

## Key Claims

- CVE scanners and dependency auditors only catch known vulnerabilities, leaving a window between a malicious package landing and detection; a 7-day minimum package age closes it, since most attacks are caught within 24–48 hours.
- Recent incidents share a pattern — the axios compromise (over 100M weekly downloads), the TanStack npm attack, and the shai-hulud Python attack — and Dependabot and lockfiles miss them because there is no CVE and the publisher account is legitimate.
- Signing proves a key was used, not that the signer is trusted: Sigstore's public Fulcio only trusts a fixed allow-list (Google, Microsoft, GitHub Actions), so a certificate says nothing about current employment.
- AI-enabled adversaries increased attacks 89% year-over-year; the 2026 TeamPCP compromise of Aqua Security's Trivy scanner used stolen CI/CD credentials and reached 2,500+ organizations.
- SBOMs, dependency confusion defenses, and inventory of third-party models, plugins, vector databases, and MCP servers are standard controls; prompt injection (OWASP LLM01) is now a supply chain surface.
- Governance spans the whole chain: secret scanning pre-commit, least-privilege CI credentials, and admission-time enforcement of signatures, which tooling still lags on.

## Related

- [artifact signing](/concepts/artifact-signing.md) — binding signatures to verified identity
- [shift-left security](/concepts/shift-left-security.md) — enforcing controls at install and build time
- [application security](/concepts/application-security.md) — the broader vulnerability surface
- [Keycloak](/entities/keycloak.md) — identity provider used as a signing trust root
- [Sigstore](/entities/sigstore.md) — keyless signing infrastructure (Fulcio, Cosign, Rekor)
