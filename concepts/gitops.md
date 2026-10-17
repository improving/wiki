---
title: "GitOps"
type: "Concept"
description: "Using Git as the source of truth for declarative infrastructure and deployment state, reconciled by a delivery tool."
created: '2026-10-17'
updated: '2026-10-17'
tags: [platform, devops, kubernetes]
sources:
  - "/sources/building-golden-paths.md"
  - "/sources/enabling-sso-authentication-argo-cd.md"
  - "/sources/resilient-hybrid-kafka-automating-on-prem-deployments-with-confluent.md"
  - "/sources/backup-and-restore-kubernetes-resources-across-vclusters-using-velero.md"
---

# GitOps

GitOps makes Git the source of truth for declarative infrastructure and deployment state, with a continuous-delivery tool watching the repository and reconciling the cluster to match it. In the golden-path playbook it is Phase 3, and it changes only the last step of delivery — a `git push` instead of `kubectl apply` — while giving audit trails and rollback for free. Because the repository is the desired state, anything that drifts (or is deleted) is recreated from Git, which is what makes the model self-correcting.

## Key Claims

- A golden path is built in four phases — standardize, validate, GitOps, self-service — where GitOps swaps the final apply step for a push, with a CD tool like [Argo CD](/entities/argo-cd.md) watching the repo.
- Git as desired state yields audit trails and rollback "for free," because every change is a reviewed commit.
- [Argo CD](/entities/argo-cd.md) is used by large organizations including Alibaba, Cisco, and Indeed; wiring SSO through its bundled Dex server replaces manually created accounts and inherits MFA configured at GitHub or GitLab.
- A regulated Fortune 100 deployment used a distribution-center template to automate deploying Kafka clusters, document databases, and Java applications to local Kubernetes clusters, making rollouts repeatable and GitOps-friendly.
- GitOps is self-correcting: a Velero restore job deleted after completion is automatically re-synced and recreated by Argo CD.
- Common Argo CD pitfalls are configuration, not concept — a mismatched Dex callback URI or forgetting to restart Dex after editing `argocd-cm`.

## Related

- [CI/CD](/concepts/ci-cd.md) — the pipeline GitOps delivery extends
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the declarative state Git holds
- [container orchestration](/concepts/container-orchestration.md) — the Kubernetes substrate
- [golden path](/concepts/golden-path.md) — the supported route GitOps makes safe
- [Argo CD](/entities/argo-cd.md) — the GitOps delivery tool
- [Kubernetes](/entities/kubernetes.md) — the reconciliation target
