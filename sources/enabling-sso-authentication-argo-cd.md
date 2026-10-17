---
title: "Enabling SSO Authentication for Argo CD with GitLab or GitHub"
type: "Source Summary"
description: "A step-by-step guide to wiring Argo CD SSO through GitLab or GitHub OAuth using the bundled Dex identity provider, plus common errors."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, security, improving.com]
sources:
  - "references/improving.com/enabling-sso-authentication-argo-cd/enabling-sso-authentication-argo-cd.md"
---

# Enabling SSO Authentication for Argo CD with GitLab or GitHub — Summary

**Original source**: `references/improving.com/enabling-sso-authentication-argo-cd/enabling-sso-authentication-argo-cd.md`

## Summary

A client using Argo CD relied on manually created accounts, which was time-consuming and hard to govern. The post walks through integrating Argo CD with GitLab or GitHub as an identity provider via the Dex server bundled with Argo CD, enabling SSO and inherited MFA while reducing credential sprawl.

## Key Claims

- Single Sign-On lets users log in once and access many applications, simplifying experience and reducing the need to manage multiple credentials.
- Argo CD is used by large organizations including Alibaba, Cisco, and Indeed; Dex ships with Helm-chart and YAML-manifest installs and implements OIDC across LDAP, SAML, and OAuth2.
- The fix replaces individual Argo CD accounts with GitHub/GitLab credentials, inheriting MFA configured at the identity provider.
- Steps: configure a GitLab/GitHub OAuth application (with redirect URI `https://argocd-domain.com/auth/callback`, scopes like API and read_user), edit the `argocd-cm` ConfigMap with a Dex `gitlab` connector, and restart the Dex server.
- Common error #1, "no session information," traces to the callback URL — the `redirectURI` must point to the Dex server at `http://argocd-dex-server:5556/dex/callback`.
- Common error #2, "dex config unmodified," requires restarting Dex to reflect configuration changes.
- Support is available via the `#argo-cd` channel on CNCF Slack.

## Relevance

Covers [single sign-on](/concepts/single-sign-on.md) in a [GitOps](/concepts/gitops.md) delivery setup, tying Argo CD to [container orchestration](/concepts/container-orchestration.md) on Kubernetes.

## Quality

Hands-on how-to by Rucha Bhange, with real error logs and fixes; concrete and reproducible, though scoped to a specific installation method.

## Entities Mentioned

- [Argo CD](/entities/argo-cd.md) — the GitOps continuous-delivery tool being secured
- [GitLab](/entities/gitlab.md) — identity provider and OAuth source
- [GitHub](/entities/github.md) — alternate identity provider
- [CNCF](/entities/cncf.md) — host of the community Slack channel for support

## Concepts Covered

- [single sign-on](/concepts/single-sign-on.md) — centralized authentication across services
- [GitOps](/concepts/gitops.md) — Git as source of truth for declarative delivery
- [container orchestration](/concepts/container-orchestration.md) — Kubernetes-based Argo CD deployment
- [devops](/concepts/devops.md) — streamlining developer access and delivery
