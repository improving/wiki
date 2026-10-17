---
title: "GitLab"
type: "Entity"
description: "DevOps platform used in this corpus as an SSO identity provider and as a host for built-in feature-flag tooling."
created: '2026-10-17'
updated: '2026-10-17'
tags: [devops, platform, security]
sources:
  - "/sources/enabling-sso-authentication-argo-cd.md"
  - "/sources/unleashing-feature-flags-onto-kafka-consumers.md"
---

# GitLab

GitLab is a DevOps platform that appears in this corpus in two infrastructure roles: as an OAuth/identity provider for single sign-on, and as a host for the Unleash feature-flag platform. Both appearances treat it as a place where authentication and operational controls get centralized rather than managed per-application.

## Role in the Corpus

- A client using [Argo CD](/entities/argo-cd.md) with manually created accounts replaced them with GitHub/GitLab credentials, inheriting MFA configured at the identity provider.
- GitLab is wired to Argo CD's bundled Dex server as an OIDC connector: create a GitLab OAuth application with redirect URI `https://argocd-domain.com/auth/callback` and scopes such as `API` and `read_user`, then edit the `argocd-cm` ConfigMap.
- Common SSO failures trace to configuration: "no session information" comes from the callback URL not pointing at the Dex server (`http://argocd-dex-server:5556/dex/callback`), and "dex config unmodified" requires restarting Dex.

## Feature Flags

- GitLab has offered the open-source Unleash feature-flag platform built into the product since version 13.5.
- That matters for [Apache Kafka](/entities/apache-kafka.md) consumers, where feature flags provide the per-topic on/off signal for pausing and resuming partitions without a costly rebalance.

## Related

- [single sign-on](/concepts/single-sign-on.md) — the identity capability GitLab provides
- [GitOps](/concepts/gitops.md) — the Argo CD delivery model GitLab secures
- [Argo CD](/entities/argo-cd.md) — the tool GitLab authenticates against
- [Apache Kafka](/entities/apache-kafka.md) — where GitLab's built-in Unleash flags are applied
