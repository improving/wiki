---
title: "Amazon ECS"
type: "Entity"
description: "AWS container orchestration service whose capacity providers blend On-Demand and Spot to cut costs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, containers, cost, aws]
sources:
  - "/sources/cost-optimization-in-amazon-ecs.md"
---

# Amazon ECS

Amazon ECS is AWS's container orchestration service. Improving's writing treats it as a cost-optimization surface: running tasks on default On-Demand or Fargate capacity pays a large premium regardless of workload priority, and ECS Capacity Providers let teams blend guaranteed and discounted capacity deliberately.

## Key Claims

- Default On-Demand or Fargate capacity means paying a 70–90% premium on every microservice.
- Spot Instances offer savings up to 90% versus On-Demand, and Fargate Spot is typically about 70% off Fargate On-Demand.
- AWS can reclaim a Spot Instance with a two-minute warning, so fleets should diversify across instance types and Availability Zones.
- The Spot Instance Advisor exposes interruption frequency — for example, c6a.2xlarge at 54% savings with under 5% interruption.
- Attribute-Based Instance Type Selection (ABS) lets you specify vCPU, memory, and generation instead of an instance list, automatically including new generations.
- The Baseline Reliability Strategy sets a high On-Demand base for critical tasks and a higher Spot weight for scale-out (e.g. 100 tasks, base 10/weight 1 On-Demand, base 0/weight 3 Spot).
- The setup is implemented with [Terraform](/entities/terraform.md); capacity-provider strategies are the core mechanism.

## Related

- [container orchestration](/concepts/container-orchestration.md) — ECS capacity providers
- [cloud cost management](/concepts/cloud-cost-management.md) — Spot and capacity strategies
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the Terraform implementation
- [AWS](/entities/aws.md) — the cloud provider and Spot seller
