---
title: "infrastructure as code"
type: "Concept"
description: "Defining infrastructure in version-controlled code that is reviewed and applied automatically, with reusable constructs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [platform, cloud, devops]
sources:
  - "/sources/infrastructure-as-actual-code-an-introduction-to-the-construct.md"
  - "/sources/multiple-environments-with-terraform.md"
  - "/sources/adopting-azure-first-steps-of-migrating-to-the-cloud.md"
  - "/sources/lessons-learned-on-the-path-to-cloud-transformation.md"
  - "/sources/auto-generate-terraform-configuration-files.md"
---

# infrastructure as code

Infrastructure as code (IaC) defines infrastructure in version-controlled code that is reviewed and applied automatically, so environments are reproducible rather than hand-built. It is repeatedly named as the goal line organizations fall short of, because hidden day-to-day infrastructure work keeps pulling teams back to the console. The practice ranges from declarative resource definitions through higher-level constructs that package whole architecture patterns, and it underpins multi-environment delivery, policy enforcement, and cost optimization.

## Key Claims

- Versioned, checked-in, automated infrastructure is the target — but many organizations fall short because of hidden day-to-day infrastructure work.
- Declarative tools like [Terraform](/entities/terraform.md) and CloudFormation force explicit definition of every resource, producing boilerplate and little abstraction.
- The Construct Programming Model — AWS CDK, CDKtf, CDK8s, and Projen — defines infrastructure in imperative languages across three tiers; roughly 20 lines of L3 code synthesize over 2,000 lines of CloudFormation JSON.
- Internally curated constructs let application teams self-serve while meeting security requirements, with non-standard use routed through infosec approval — but abstraction is no substitute for foundational cloud knowledge.
- Multi-environment [Terraform](/entities/terraform.md): workspaces are not meant for environment isolation, and plain modules still duplicate state backends; Terragrunt centralizes inputs, modules, providers, and state backends so environments can override selectively and pin module versions.
- On Azure, Microsoft's [Cloud Adoption Framework](/entities/cloud-adoption-framework.md) prescribes separate management groups and subscriptions per environment, Azure Policy to deny non-compliant deployments, and tags for owner, project, and business unit.
- Importing existing resources: Azure Terrafy (Azure-only), Former2 (AWS-only), TerraCognita, Terraformer, and native import (state but not configuration); verify with `terraform plan` expecting "No changes."

## Related

- [cloud migration](/concepts/cloud-migration.md) — moving console-built resources into code
- [multi-cloud](/concepts/multi-cloud.md) — IaC as the portability layer across providers
- [cloud cost management](/concepts/cloud-cost-management.md) — cost strategies implemented in code
- [GitOps](/concepts/gitops.md) — Git as the source of truth for declarative state
- [Terraform](/entities/terraform.md) — the most cited IaC tool
- [HashiCorp](/entities/hashicorp.md) — maker of Terraform and Packer
