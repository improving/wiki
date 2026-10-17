---
title: "Why Kubernetes GPU Scheduling Keeps Breaking Your Golden Path"
type: "Source Summary"
description: "Argues GPU platform engineering should not abstract over unsettled layers — DRA migration, tenant isolation, driver lifecycle — that hide unmade decisions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, ai, improving.com]
sources:
  - "references/improving.com/gpu-platform-engineering-golden-path/gpu-platform-engineering-golden-path.md"
---

# Why Kubernetes GPU Scheduling Keeps Breaking Your Golden Path — Summary

**Original source**: `references/improving.com/gpu-platform-engineering-golden-path/gpu-platform-engineering-golden-path.md`

## Summary

Good abstractions remove complexity only after the underlying problem is stable, and GPU platform engineering isn't there yet: scheduling, tenant isolation, and driver coordination are all still moving. The post argues that golden paths built on those layers hide decisions teams never consciously made, surfacing as pending pods, data-exposure risk, and driver-upgrade incidents in production.

## Key Claims

- CPU scheduling, isolation, and quota were solved before platform engineering matured; GPU scheduling and isolation are still being rebuilt inside Kubernetes.
- The device plugin model (since 2017) exposes only a count (nvidia.com/gpu: 1); VRAM capacity, NVLink topology, and MIG profiles are invisible, so teams compensate with labels, tolerations, and affinity — "tribal knowledge disguised as YAML."
- Dynamic Resource Allocation (DRA) graduated to general availability in Kubernetes 1.34 and is mutually exclusive with the device plugin on the same node; a DRAExtendedResource shim softens migration.
- Native gang scheduling is alpha in Kubernetes 1.35 (beta targeted for 1.37); until then production gang scheduling means owning Volcano or NVIDIA's KAI Scheduler.
- A MIG profile change costs roughly 30–60 seconds per GPU, so on an 8-GPU node a single change means 4–8 minutes of node-wide drain.
- Three GPU sharing strategies trade isolation for flexibility; the default is usually time-slicing, and fabric-level isolation (which GPUs share an NVLink domain) is a fourth decision teams rarely know they need.
- A durable golden path abstracts what is solved (container packaging, CI, observability, access controls) and keeps visible what is still a live decision: workload class, sharing strategy, and driver/firmware lifecycle.
- The self-service request should ask workload class (training/inference/development, multi-tenant/dedicated, latency-sensitive/batch) rather than "a GPU."

## Relevance

A case study in [platform engineering](/concepts/platform-engineering.md) and the limits of the [golden path](/concepts/golden-path.md), where premature abstraction creates [abstraction debt](/concepts/abstraction-debt.md) and hides decisions from the [internal developer portal](/concepts/internal-developer-portal.md).

## Quality

Practitioner deep-dive by Atulpriya Sharma; technically specific and well-sourced, though version specifics will age quickly.

## Entities Mentioned

- [Atulpriya Sharma](/entities/atulpriya-sharma.md) — author
- [Kubernetes](/entities/kubernetes.md) — the orchestration substrate
- [Nvidia](/entities/nvidia.md) — GPU Operator and KAI Scheduler cited
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [platform engineering](/concepts/platform-engineering.md) — self-service infrastructure as a product
- [golden path](/concepts/golden-path.md) — the opinionated supported route
- [abstraction debt](/concepts/abstraction-debt.md) — cost of abstractions over unstable layers
- [internal developer portal](/concepts/internal-developer-portal.md) — the catalog and request interface
- [container orchestration](/concepts/container-orchestration.md) — scheduling at scale
- [cognitive load](/concepts/cognitive-load.md) — what the platform should absorb
