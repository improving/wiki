---
title: "Velero"
type: "Entity"
description: "Kubernetes backup and restore tool used to migrate resources and persistent volumes between clusters."
created: '2026-10-17'
updated: '2026-10-17'
tags: [kubernetes, backup, platform-engineering]
sources:
  - "/sources/backup-and-restore-kubernetes-resources-across-vclusters-using-velero.md"
  - "/sources/platform-engineering-maturity-model.md"
---

# Velero

Velero is a Kubernetes backup and restore tool that captures cluster resources and persistent volumes. It appears in the corpus as the way to migrate workloads between virtual clusters (vClusters) that lack built-in backup, and is referenced in platform engineering writing as a standard component of a Kubernetes stack.

## Key Facts

- Velero backs up and restores cluster resources and persistent volumes, supports migration, and can replicate production into dev/test.
- A walkthrough moves a MySQL pod between vClusters using Velero with the Azure provider: a storage account and blob container, a service principal with the "Storage Blob Data Contributor" role, and BSL and cloud credentials.
- Velero is installed via Helm in both source and destination vClusters using the same values.yaml, with two parameters differing.
- After a restore job is deleted, Argo CD automatically re-syncs and recreates it, tying the backup workflow to GitOps.
- It is linked as a Kubernetes backup example in the platform engineering maturity model.

## Related

- [container orchestration](/concepts/container-orchestration.md) — the Kubernetes substrate it protects
- [GitOps](/concepts/gitops.md) — the delivery model that re-creates its restore jobs
- [Argo CD](/entities/argo-cd.md) — the tool that re-syncs the restore job
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the Helm-based install pattern
