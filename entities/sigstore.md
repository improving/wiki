---
title: "Sigstore"
type: "Entity"
description: "Keyless signing infrastructure (Fulcio, Cosign, Rekor) for software artifacts."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, supply-chain, identity]
sources:
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# Sigstore

Sigstore is keyless signing infrastructure for software artifacts, composed of three parts: Fulcio, Cosign, and Rekor. It appears in the corpus as the reference approach to software supply chain signing, and as the subject of a critique that a signature proves a key was used, not that the signer is currently trusted.

## Components and Limits

- Fulcio is a certificate authority issuing short-lived certificates, typically around ten minutes, after OIDC authentication.
- Cosign is the signing tool; Rekor is a public, append-only transparency log.
- Public Sigstore only trusts a fixed allow-list — Google, Microsoft, GitHub Actions — so a certificate proves "Google vouches for this email," not current employment.
- Two failure modes: offboarding does not propagate (a GitHub Actions token can outlive a suspended account), and CI versus human identities were never issued from the same place.
- Self-hosting Fulcio lets an organization control the trust list; the corpus pairs it with [Keycloak](/entities/keycloak.md) to bind certificates to managed identities.

## Related

- [Keycloak](/entities/keycloak.md) — the identity provider used as the trust root
- [artifact signing](/concepts/artifact-signing.md) — binding signatures to verified identity
- [software supply chain security](/concepts/software-supply-chain-security.md) — the threat it addresses
- [zero trust security](/concepts/zero-trust-security.md) — verifying the signer's current trust
