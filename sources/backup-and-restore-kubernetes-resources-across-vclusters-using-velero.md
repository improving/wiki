---
title: "Backup and Restore Kubernetes Resources Across vClusters using Velero"
type: "Source Summary"
description: "A step-by-step guide to migrating Kubernetes workloads between vCluster virtual clusters using Velero with the Azure provider."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, kubernetes, cloud, improving.com]
sources:
  - "references/improving.com/backup-and-restore-kubernetes-resources-across-vclusters-using-velero/backup-and-restore-kubernetes-resources-across-vclusters-using-velero.md"
---

# Backup and Restore Kubernetes Resources Across vClusters using Velero — Summary

**Original source**: `references/improving.com/backup-and-restore-kubernetes-resources-across-vclusters-using-velero/backup-and-restore-kubernetes-resources-across-vclusters-using-velero.md`

## Summary

Virtual clusters (vCluster) give teams isolated, on-demand Kubernetes environments that share one host cluster, but they lack built-in backup and migration. This tutorial shows how Velero fills that gap by backing up resources and persistent volumes from one vCluster and restoring them into another. It walks through an Azure-based setup, a MySQL pod migration, and troubleshooting.

## Key Claims

- vCluster runs inside a host-cluster namespace with its own API server, control plane, and syncer, giving stronger isolation than namespaces.
- Velero backs up and restores cluster resources and persistent volumes, supports migration, and replicates production to dev/test.
- The walkthrough uses Azure: a storage account and blob container, a service principal with the "Storage Blob Data Contributor" role, and BSL and cloud credentials.
- Velero is installed via Helm in both source and destination vClusters using the same values.yaml, with two parameters differing.
- Steps: deploy a MySQL pod, add data (test1.txt, test2.txt), back up, restore, and verify by attaching the PVC to a pod.
- Troubleshooting covers PartiallyFailed/FailedValidation backups, node-agent pods not scheduled on a node, and restarts.
- After a restore job is deleted, ArgoCD automatically re-syncs and recreates it.

## Relevance

A hands-on treatment of [container orchestration](/concepts/container-orchestration.md) and Kubernetes backup, touching [GitOps](/concepts/gitops.md) via ArgoCD and [infrastructure as code](/concepts/infrastructure-as-code.md) via Helm.

## Quality

Practical tutorial by Richa Mishra; concrete and reproducible, though screenshot-heavy and specific to Azure.

## Entities Mentioned

- [Velero](/entities/velero.md) — backup and restore tool
- [Argo CD](/entities/argo-cd.md) — re-syncs the restore job
- [Kubernetes](/entities/kubernetes.md) — the orchestration substrate

## Concepts Covered

- [container orchestration](/concepts/container-orchestration.md) — vClusters and workloads
- [GitOps](/concepts/gitops.md) — ArgoCD-driven restore
- [infrastructure as code](/concepts/infrastructure-as-code.md) — Helm chart deployment
