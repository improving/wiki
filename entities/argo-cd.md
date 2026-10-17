---
title: "Argo CD"
type: "Entity"
description: "GitOps continuous-delivery tool for Kubernetes, used for declarative deployments and SSO-secured access."
created: '2026-10-17'
updated: '2026-10-17'
tags: [gitops, kubernetes, platform-engineering]
sources:
  - "/sources/enabling-sso-authentication-argo-cd.md"
  - "/sources/building-golden-paths.md"
  - "/sources/platform-engineering-maturity-model.md"
  - "/sources/platform-engineering-service-organizations.md"
  - "/sources/backup-and-restore-kubernetes-resources-across-vclusters-using-velero.md"
---

# Argo CD

Argo CD is a GitOps continuous-delivery tool for Kubernetes that reconciles cluster state against a Git repository. It recurs across the corpus's platform engineering writing as the delivery layer of a golden path, a security surface to be wired into SSO, and a reusable pattern in a service organization's capability layer.

## Key Facts

- Argo CD is used by large organizations including Alibaba, Cisco, and Indeed; its bundled Dex server implements OIDC across LDAP, SAML, and OAuth2.
- Integrating Argo CD with GitLab or GitHub replaces manually created accounts, enabling SSO and inherited MFA while reducing credential sprawl.
- In a golden-path build, Phase 3 swaps `kubectl apply` for a git push, with a CD tool like Argo CD watching the repo — giving audit trails and rollback for free.
- It appears in the platform engineering maturity model's golden-path examples and as a GitOps pattern in a service organization's capability layer.
- After a Velero restore job is deleted, Argo CD automatically re-syncs and recreates it.

## Related

- [GitOps](/concepts/gitops.md) — the delivery model Argo CD implements
- [golden path](/concepts/golden-path.md) — the supported route it deploys
- [single sign-on](/concepts/single-sign-on.md) — how its access is governed
- [Velero](/entities/velero.md) — the backup tool whose restore jobs it re-syncs
