---
title: "artifact signing"
type: "Concept"
description: "Cryptographically signing build artifacts and binding signatures to a verified, current identity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, platform, supply-chain]
sources:
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
  - "/sources/software-supply-chain-security-package-age-enforcement.md"
  - "/sources/security-the-thing-that-everyone-loves-to-hate.md"
---

# artifact signing

Artifact signing cryptographically attaches a signature to a build artifact so consumers can verify who produced it and that it has not been altered. The corpus's central insight is that signing alone is not the goal: a signature proves a key was used, so supply chain security depends on binding signatures to an identity the organization currently trusts — which is why [software supply chain security](/concepts/software-supply-chain-security.md) writing here centers on identity, not keys.

## Key Claims

- Traditional code signing relies on a long-lived private key; a key that lives for months or years can leak for that long, with no clean way to know which past signatures to still trust.
- Sigstore replaces long-lived keys with keyless signing in three parts: Fulcio (a CA issuing short-lived certificates, typically ~10 minutes, after OIDC authentication), Cosign (the signing tool), and Rekor (a public, append-only transparency log).
- A signature proves someone with the key signed it — nothing about whether they still hold that access or are still employed, which is exactly the gap SolarWinds and xz-utils exploited.
- Self-hosting Fulcio and pointing it at a Keycloak realm ties every certificate to an identity the organization manages, so offboarding propagates and compliance can prove every signature belongs to a currently active employee.
- Two failure modes matter: offboarding doesn't propagate (a CI token outliving a suspended account), and CI versus human identities were never issued from the same place.
- Signing sits alongside other supply chain controls — SBOMs, secret scanning, and package-age enforcement — as part of a layered [shift-left security](/concepts/shift-left-security.md) posture.

## Related

- [software supply chain security](/concepts/software-supply-chain-security.md) — the chain signing secures
- [single sign-on](/concepts/single-sign-on.md) — the identity source that anchors signer trust
- [zero trust security](/concepts/zero-trust-security.md) — verify the signer's current trust, not just the signature
- [Sigstore](/entities/sigstore.md) — keyless signing infrastructure (Fulcio, Cosign, Rekor)
- [Keycloak](/entities/keycloak.md) — identity provider used as the signing trust root
