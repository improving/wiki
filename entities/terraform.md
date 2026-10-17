---
title: "Terraform"
type: "Entity"
description: "HashiCorp's infrastructure-as-code tool, used across this corpus for multi-environment, multi-cloud provisioning."
created: '2026-10-17'
updated: '2026-10-17'
tags: [infrastructure-as-code, hashicorp, cloud]
sources:
  - "/sources/multiple-environments-with-terraform.md"
  - "/sources/auto-generate-terraform-configuration-files.md"
  - "/sources/infrastructure-as-actual-code-an-introduction-to-the-construct.md"
  - "/sources/simplify-fastly-cdn-with-improvings-terraform-module.md"
  - "/sources/accelerating-scientific-research-in-the-public-sector.md"
---

# Terraform

HashiCorp's infrastructure-as-code tool and the default way this corpus expresses cloud infrastructure in version-controlled, reviewable form. It anchors [infrastructure-as-code](/concepts/infrastructure-as-code.md) practice across multi-environment setups, resource import, curated modules, and multi-cloud provisioning.

## Multi-Environment Practice

- Terraform workspaces store state per environment, but HashiCorp warns they are not appropriate for system decomposition or deployments needing separate credentials and access controls.
- HCP Terraform workspaces address some issues but require the cloud platform and leave room for drift and duplication.
- Terragrunt centralizes dynamic configuration for inputs, modules, providers, and state backends; a global directory holds shared module calls and ACLs while each environment overrides what it needs.
- Environments can pin different module release versions, useful for sandbox testing.

## Adoption and Import

- Importing existing resources is a common migration path; tool choice depends on provider, accuracy, and whether configuration and state are created automatically.
- Azure Terrafy is Azure-only; Former2 is AWS-only; TerraCognita, Terraformer, and native Terraform import are broader.
- HashiCorp's native import creates state but not configuration files, requiring manual authoring; a clean `terraform plan` should report "No changes."
- State should live in S3 with DynamoDB locking and versioning, with configuration in version control.

## Modules and Abstraction

- The Construct Programming Model (AWS CDK, CDKtf, CDK8s) defines infrastructure in real programming languages and offers L1–L3 abstraction tiers; ~20 lines of L3 code can synthesize over 2000 lines of CloudFormation.
- Improving's open-source terraform-fastly-service module manages Fastly CDN configuration as code, with Terragrunt for DRY multi-environment setups.
- High-level constructs create [golden-path](/concepts/golden-path.md) self-service while carrying [abstraction-debt](/concepts/abstraction-debt.md) risk; test synthesized output with the provided unit-test utilities.

## Related

- [HashiCorp](/entities/hashicorp.md) — maker of Terraform and Packer
- [infrastructure-as-code](/concepts/infrastructure-as-code.md) — defining infrastructure in version-controlled code
- [golden-path](/concepts/golden-path.md) — curated constructs as the supported route
- [cloud-migration](/concepts/cloud-migration.md) — bringing existing resources under code
