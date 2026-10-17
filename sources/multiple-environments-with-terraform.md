---
title: "Multiple Environments with Terraform"
type: "Source Summary"
description: "Compares DRY multi-environment Terraform approaches and recommends a Terragrunt structure with global and per-env configs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, improving.com]
sources:
  - "references/improving.com/multiple-environments-with-terraform/multiple-environments-with-terraform.md"
---

# Multiple Environments with Terraform — Summary

**Original source**: `references/improving.com/multiple-environments-with-terraform/multiple-environments-with-terraform.md`

## Summary

Compares ways to achieve DRY multi-environment Terraform and recommends Terragrunt. It argues Terraform workspaces aren't meant for environment isolation and plain modules still duplicate state backends and environment configs, then walks through a project structure where a global directory holds shared module calls and ACLs while each environment overrides what it needs.

## Key Claims

- Terraform workspaces store state per environment, but HashiCorp warns they aren't appropriate for system decomposition or deployments needing separate credentials and access controls.
- HCP Terraform workspaces address some issues but require the cloud platform and create room for drift and code duplication.
- Terraform modules keep global settings in the module and dynamic settings in the caller, but state backend configuration is still repeated and environment configs can drift.
- Terragrunt centralizes dynamic configuration for inputs, modules, providers, and state backends, and lets IaC include other IaC without a separate module.
- The sample structure has a global directory (global-main.tf, global-acls.tf), per-environment directories (dev, prod) with acls.tf, variables.tf, and terragrunt.hcl, plus a shared terragrunt-root.hcl.
- Environments can include global ACLs and add their own (dev adds a test ACL) or override entirely, and can pin different module release versions — useful for sandbox testing.
- Execution is simple: terragrunt init/plan/apply --all, with --queue-include-dir to target dev or production.

## Relevance

An [infrastructure as code](/concepts/infrastructure-as-code.md) pattern for multi-environment [CI/CD](/concepts/ci-cd.md) workflows using Terraform.

## Quality

Practitioner how-to by Paul Hassinger; concrete and reproducible, though it assumes familiarity with Terraform and Terragrunt.

## Entities Mentioned

- [Terraform](/entities/terraform.md) — the IaC tool
- [HashiCorp](/entities/hashicorp.md) — Terraform's maker
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [infrastructure as code](/concepts/infrastructure-as-code.md) — declarative, versioned infrastructure
- [CI/CD](/concepts/ci-cd.md) — wiring environments into delivery workflows
