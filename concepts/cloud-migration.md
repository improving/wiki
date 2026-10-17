---
title: "cloud migration"
type: "Concept"
description: "Moving workloads to the cloud, from lift-and-shift to containerized and cloud-native re-architecture."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, modernization, platform]
sources:
  - "/sources/lessons-learned-on-the-path-to-cloud-transformation.md"
  - "/sources/managing-cloud-cost.md"
  - "/sources/adopting-azure-first-steps-of-migrating-to-the-cloud.md"
  - "/sources/legacy-modernization-cloud-replatforming-companies.md"
  - "/sources/auto-generate-terraform-configuration-files.md"
---

# cloud migration

Cloud migration moves workloads from on-premises infrastructure to the cloud, and there is no golden recipe — only well-worn paths to failure. The chief trap is assuming the cloud is automatically cheaper and lift-and-shifting virtual servers without restructuring them for the platform. The three broad approaches — lift-and-shift, containerized, and cloud-native — each trade upfront effort for long-term operational cost and efficiency, so the choice is a cost-and-approach decision rather than a single destination.

## Key Claims

- The cloud's foundation is that running virtual environments at scale is cheaper than at small scale; ignoring that is why naive lift-and-shift is expensive.
- Fastest migration (physical-to-virtual) trades speed for higher operating cost, treating the cloud as leased data center space.
- Containerizing with Docker and Kubernetes gives flexibility and automated management on AWS, Azure, and GCP, but long-term maintenance must include application teams.
- Cloud-native builds leveraging packaged platform services have the highest conversion cost and the greatest efficiency.
- Migration signals: end-of-life support, licensing costs outpacing business value, integration gaps, week- or month-long deployment cycles, retiring legacy talent, and audit findings.
- The [7 R strategies](/concepts/application-modernization-strategy.md) run from rehosting through replatforming and refactoring/re-architecting to a full rebuild, reserved for systems too brittle to migrate incrementally.
- Get environment configuration right early: separate management groups and subscriptions, tags for ownership, and naming conventions, because a rename can break interdependent resources after deployment.
- A telehealth case met an over-8× volume surge while halving the planned migration time and maintaining HIPAA, SOC 2, and HITRUST compliance.

## Related

- [legacy modernization](/concepts/legacy-modernization.md) — evolving legacy systems rather than rewriting them
- [application modernization](/concepts/application-modernization.md) — moving apps to modern architectures
- [infrastructure as code](/concepts/infrastructure-as-code.md) — versioned, automated environments
- [multi-cloud](/concepts/multi-cloud.md) — spanning more than one provider
- [hybrid cloud](/concepts/hybrid-cloud.md) — keeping some workloads on-premises
- [Terraform](/entities/terraform.md) — importing and managing migrated resources
