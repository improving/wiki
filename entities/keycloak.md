---
title: "Keycloak"
type: "Entity"
description: "Open-source identity provider used as the trust root for self-hosted Sigstore artifact signing."
created: '2026-10-17'
updated: '2026-10-17'
tags: [identity, security, supply-chain]
sources:
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# Keycloak

Keycloak is an open-source identity provider that appears in the corpus as the trust root for a self-hosted Sigstore deployment. The argument is that because Keycloak is already the source of truth for single sign-on and offboarding, pointing a self-hosted Fulcio at a Keycloak realm ties every artifact signature to an identity the organization currently manages.

## Key Facts

- Self-hosting Fulcio lets an organization control its trust list; adding Keycloak as a trusted issuer binds signing certificates to managed identities.
- Reusing the SSO realm closes a Sigstore gap: public infrastructure proves only that a provider vouches for an email, not that the signer is still employed.
- The implementation registers the issuer in Fulcio, maps claims such as `email_verified` and `aud`, signs with Cosign, verifies, and confirms the failure case fails closed.
- The demo code lives in the `infracloudio/keycloak-fulcio-sigstore` repository.

## Related

- [Sigstore](/entities/sigstore.md) — the signing infrastructure Keycloak anchors
- [single sign-on](/concepts/single-sign-on.md) — the role Keycloak already plays
- [artifact signing](/concepts/artifact-signing.md) — what the identity binding secures
- [software supply chain security](/concepts/software-supply-chain-security.md) — the discipline it serves
