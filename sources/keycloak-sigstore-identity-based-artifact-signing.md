---
title: "Keycloak + Sigstore: Binding Human Identity to Artifact Signatures"
type: "Source Summary"
description: "Signing proves a key was used, not that the signer is trusted; self-hosting Fulcio with Keycloak binds signatures to org identity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, platform, improving.com]
sources:
  - "references/improving.com/keycloak-sigstore-identity-based-artifact-signing/keycloak-sigstore-identity-based-artifact-signing.md"
---

# Keycloak + Sigstore: Binding Human Identity to Artifact Signatures — Summary

**Original source**: `references/improving.com/keycloak-sigstore-identity-based-artifact-signing/keycloak-sigstore-identity-based-artifact-signing.md`

## Summary

The question that matters in software supply chain security is not whether an artifact was signed but whether the signer is someone the organization currently trusts. Sigstore's keyless signing removes long-lived keys but its public infrastructure trusts a fixed allow-list of identity providers, so offboarding doesn't propagate and CI and human identities live in unrelated trust domains. Self-hosting Fulcio and pointing it at a Keycloak realm ties every certificate to an identity the organization actually manages.

## Key Claims

- A backdoor was planted in xz-utils (2024) by a contributor who spent two years building trust; SolarWinds' compromised build pipeline shipped a legitimately signed update to roughly 18,000 organizations, including US federal agencies.
- Traditional code signing uses a long-lived private key; a key that lives for months or years can leak for that long, with no clean way to know which past signatures to still trust.
- Even without a leak, a signature proves someone with the key signed it — nothing about whether they still hold that access or are still employed.
- Sigstore has three components: Fulcio (a CA issuing short-lived certificates, typically ~10 minutes, after OIDC authentication), Cosign (the signing tool), and Rekor (a public, append-only transparency log).
- Public Sigstore only trusts a fixed allow-list — Google, Microsoft, GitHub Actions — so a certificate proves "Google vouches for this email," not current employment.
- Two failure modes: offboarding doesn't propagate (a GitHub Actions token outlives a suspended Workspace account), and CI versus human identities were never issued from the same place.
- Self-hosting Fulcio lets you control the trust list; adding Keycloak (already the source of truth for SSO and offboarding) as a trusted issuer ties certificates to managed identities.
- GitHub's OIDC issuer works for a single-repo, GitHub-only shop but fails when one policy must cover both CI and humans, or when compliance asks for every signature tied to a currently active employee.
- Implementation walkthrough: register the issuer in Fulcio, map claims (`email_verified` as a real boolean, `aud` matching the client), inspect the decoded token, sign with Cosign, verify — and confirm the failure case fails closed.
- Lessons: decide early whether you need a transparency log (Trillian-backed, a real operational commitment); Fulcio's file-based CA can generate an ephemeral root, so fetch it fresh from `/api/v1/rootCert`; pin the IdP hostname so `iss` is stable; admission-time enforcement tooling is still catching up.
- Full code is at the `infracloudio/keycloak-fulcio-sigstore` repository.

## Relevance

Informs [software supply chain security](/concepts/software-supply-chain-security.md), [artifact signing](/concepts/artifact-signing.md), [zero trust security](/concepts/zero-trust-security.md), and [single sign-on](/concepts/single-sign-on.md).

## Quality

Hands-on technical how-to by Oshi Gupta; specific, reproducible, and candid about pitfalls, though vendor-adjacent (Improving/InfraCloud).

## Entities Mentioned

- [Keycloak](/entities/keycloak.md) — the identity provider used as the trust root
- [Sigstore](/entities/sigstore.md) — keyless signing infrastructure (Fulcio, Cosign, Rekor)
- [GitHub](/entities/github.md) — OIDC issuer for CI and code host
- [Kubernetes](/entities/kubernetes.md) — runs the local Fulcio and Keycloak demo

## Concepts Covered

- [software supply chain security](/concepts/software-supply-chain-security.md) — the source-to-deploy chain and its weak links
- [artifact signing](/concepts/artifact-signing.md) — binding signatures to verified identity
- [zero trust security](/concepts/zero-trust-security.md) — verify the signer's current trust, not just the signature
- [single sign-on](/concepts/single-sign-on.md) — reusing the SSO realm as the signing identity source
