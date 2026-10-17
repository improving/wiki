---
title: "single sign-on"
type: "Concept"
description: "Centralized authentication so users sign in once across services, inheriting MFA and reducing credential sprawl."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, platform, identity]
sources:
  - "/sources/enabling-sso-authentication-argo-cd.md"
  - "/sources/keycloak-sigstore-identity-based-artifact-signing.md"
---

# single sign-on

Single sign-on (SSO) lets a user authenticate once and reach many applications, replacing per-tool accounts with credentials issued and governed by an identity provider. In this corpus it appears as both a delivery-platform convenience — replacing manually created accounts in Argo CD — and, more ambitiously, as the trust root that ties signed build artifacts to identities an organization actually manages.

## Key Claims

- SSO reduces credential sprawl and inherits MFA configured at the identity provider, because users log in with their GitHub or GitLab credentials rather than tool-specific accounts.
- Argo CD ships a Dex identity provider that implements OIDC across LDAP, SAML, and OAuth2; wiring GitLab or GitHub as a connector replaces individual accounts with provider-managed identities.
- The mechanics are concrete: register an OAuth application with a callback at `https://argocd-domain.com/auth/callback`, edit the `argocd-cm` ConfigMap with a Dex connector, and restart Dex for changes to take effect.
- SSO can anchor more than login: self-hosting Fulcio and pointing it at a Keycloak realm makes every short-lived signing certificate traceable to a currently active identity, so offboarding propagates.
- Identity-provider trust is the weak point to design for — Sigstore's public infrastructure only trusts a fixed allow-list, so a certificate proves "Google vouches for this email," not current employment.

## Related

- [artifact signing](/concepts/artifact-signing.md) — reusing the SSO realm as the signing identity source
- [GitOps](/concepts/gitops.md) — Git as source of truth for the delivery platforms SSO protects
- [zero trust security](/concepts/zero-trust-security.md) — verifying identity on every request
- [Keycloak](/entities/keycloak.md) — open-source identity provider used as a signing trust root
- [Argo CD](/entities/argo-cd.md) — GitOps tool secured with SSO
