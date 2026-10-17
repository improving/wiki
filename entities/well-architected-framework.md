---
title: "AWS Well-Architected Framework"
type: "Entity"
description: "AWS's pillar framework for sound cloud architectures, mirrored by Azure and Google Cloud."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, architecture, standards]
sources:
  - "/sources/multi-cloud-strategies-for-developers.md"
---

# AWS Well-Architected Framework

The AWS Well-Architected Framework is [AWS](/entities/aws.md)'s set of design pillars for building sound cloud architectures. In this corpus it is the shared vocabulary onto which multi-cloud design is mapped — and it is notable that Azure and Google Cloud publish equivalent frameworks with the same core pillars, which is what makes it usable across providers.

## The Pillars

- **Operational excellence, security, reliability, cost optimization, and performance** — AWS, Azure, and GCP each publish a Well-Architected Framework sharing these core pillars.
- **Reliability** — quick recovery from failure through redundancy and failover — is called the most important pillar for [multi-cloud](/concepts/multi-cloud.md).
- Developers should right-size workloads and scale dynamically to satisfy the cost-optimization pillar across providers.

## Multi-Cloud Considerations

- Layered on the pillars, the four decision factors are architecture purpose, provider compatibility, interoperability, and governance and monitoring.
- Robust [observability](/concepts/observability.md) is required to keep security and performance from degrading across providers.

Supporting evidence for this page is currently thin — the framework appears in a single summary here — but it is the reference model this corpus uses to frame multi-cloud architecture.

## Related

- [multi-cloud](/concepts/multi-cloud.md) — the strategy mapped onto the pillars
- [hybrid cloud](/concepts/hybrid-cloud.md) — the related deployment model
- [cloud cost management](/concepts/cloud-cost-management.md) — the cost-optimization pillar
- [observability](/concepts/observability.md) — required to govern across providers
