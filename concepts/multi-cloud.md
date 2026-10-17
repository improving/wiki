---
title: "multi-cloud"
type: "Concept"
description: "Running across more than one cloud provider to reduce lock-in and improve resilience, at the cost of complexity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, platform, resilience]
sources:
  - "/sources/multi-cloud-strategies-for-developers.md"
  - "/sources/leveraging-multi-and-hybrid-architectures-for-next-gen-platform.md"
  - "/sources/managing-cloud-cost.md"
  - "/sources/ai-sovereignty-escaping-the-single-vendor-trap.md"
---

# multi-cloud

Multi-cloud runs workloads across more than one cloud provider — for example AWS for web applications and Oracle Cloud for ERP — to reduce vendor lock-in, improve resilience, satisfy regulation, and optimize cost. Containerization and orchestration made it feasible and increasingly a best practice, loosening the single-cloud commitment that brings limited flexibility and service-deprecation risk. The benefit comes only if an organization accepts the added operational complexity, so the strategy has to be purpose-built to business needs.

## Key Claims

- Single-cloud commitments bring vendor lock-in, limited flexibility, and service-deprecation risk; containerization and orchestration let teams use the best services across providers.
- Four drivers: resilience and disaster recovery via failover; avoiding vendor lock-in; regulatory/compliance needs (PCI, HIPAA, regional storage); and cost optimization by matching workloads to providers.
- Multi-cloud design maps onto the Well-Architected Framework pillars — operational excellence, security, reliability, cost optimization, and performance — with reliability called the most important for multi-cloud.
- The four considerations are architecture purpose, provider compatibility, interoperability, and governance/monitoring; robust [observability](/concepts/observability.md) keeps security and performance from degrading across providers.
- Complexities: redundant resources, data-transfer/egress premiums, and the need for AWS/Azure/GCP specialists across differing services and terminologies.
- Simplifiers: architectural planning, [infrastructure as code](/concepts/infrastructure-as-code.md) ([Terraform](/entities/terraform.md)) for portability, [CI/CD](/concepts/ci-cd.md) for consistent releases, unified authentication, and native cost-management tools.
- Hyperscaler abstraction and open-weight models extend the same logic to AI, escaping single-vendor pricing and viability risk.

## Related

- [hybrid cloud](/concepts/hybrid-cloud.md) — combining on-premises and cloud
- [cloud cost management](/concepts/cloud-cost-management.md) — exploiting provider price differences
- [cloud migration](/concepts/cloud-migration.md) — moving workloads across providers
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the portability layer
- [Terraform](/entities/terraform.md) — IaC tool recommended for portability
- [Google Cloud](/entities/google-cloud.md) — one of the hyperscalers requiring specialists
