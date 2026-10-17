---
title: "5 Tools to Auto-Generate Terraform Configuration Files"
type: "Source Summary"
description: "Compares five tools for importing existing cloud resources into Terraform, with planning, execution, and verification steps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, cloud, improving.com]
sources:
  - "references/improving.com/auto-generate-terraform-configuration-files/auto-generate-terraform-configuration-files.md"
---

# 5 Tools to Auto-Generate Terraform Configuration Files — Summary

**Original source**: `references/improving.com/auto-generate-terraform-configuration-files/auto-generate-terraform-configuration-files.md`

## Summary

Nitin Naidu compares five tools for importing existing cloud resources into Terraform configuration, and lays out a systematic approach to planning, executing, and verifying the import.

## Key Claims

- Tool choice depends on cloud provider, accuracy, and whether both configuration and state files are created automatically.
- Azure Terrafy is Azure-only; Former2 is AWS-only; TerraCognita (AWS/GCP/Azure), Terraformer (many providers), and native Terraform import are broader.
- HashiCorp's native import creates state but not configuration files, requiring manual authoring.
- Start small — one resource or a tag-filtered set — then run `terraform plan` and expect "No changes" to confirm an accurate replication.
- Merge multiple state files with `state mv`; store state in S3 with DynamoDB locking and versioning; keep configuration in version control.
- A comparison table rates the tools on config/state import, module creation, resource listing, and provider support; none is fully mature.

## Relevance

Informs [infrastructure as code](/concepts/infrastructure-as-code.md), [cloud migration](/concepts/cloud-migration.md), and [multi-cloud](/concepts/multi-cloud.md) adoption of Terraform.

## Quality

Hands-on tooling comparison by Nitin Naidu; concrete CLI examples and a comparison table, current as of 2022.

## Entities Mentioned

- [Terraform](/entities/terraform.md) — the target IaC tool
- [HashiCorp](/entities/hashicorp.md) — maker of Terraform and its native import
- [GitHub](/entities/github.md) — host of the sample configs
- [AWS](/entities/aws.md) — a supported provider
- [Google Cloud](/entities/google-cloud.md) — a supported provider
- [Microsoft](/entities/microsoft.md) — maker of Azure Terrafy

## Concepts Covered

- [infrastructure as code](/concepts/infrastructure-as-code.md) — managing cloud resources as code
- [cloud migration](/concepts/cloud-migration.md) — moving console-built resources into Terraform
- [multi-cloud](/concepts/multi-cloud.md) — tools spanning AWS, GCP, and Azure
