---
title: "Fastly"
type: "Entity"
description: "Edge cloud and CDN provider, managed via an Improving Terraform module."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, platform, security]
sources:
  - "/sources/simplify-fastly-cdn-with-improvings-terraform-module.md"
---

# Fastly

Fastly is an edge cloud and CDN provider that appears in this corpus through Improving's open-source terraform-fastly-service module, which manages Fastly configuration as code. The write-up treats Fastly as a service whose manual, UI-driven configuration is error-prone, and whose many security and observability features are easy to overlook by hand.

## Managed as Code

- Manually managing Fastly services through the UI leads to inconsistencies, deployment errors, and environments that drift out of sync.
- Improving's terraform-fastly-service module abstracts Fastly features through the Terraform Fastly provider: domains, backends, load balancing, health checks, cache logic, VCL, snippets, dictionaries, network ACLs, WAF, rate limiting, DDoS protection, gzip, image optimization, and logging endpoints.
- It supports multi-environment deployments with shared global configuration plus per-environment overrides for dev, staging, production, and ephemeral environments; combined with Terragrunt it keeps multi-environment config DRY.
- Recommended practices: version control and audit every change, separate environments, never hardcode credentials, and enable logging to observability platforms.

## Related

- [infrastructure as code](/concepts/infrastructure-as-code.md) — the practice the module applies to the CDN
- [secrets management](/concepts/secrets-management.md) — credentials for Fastly must not be hardcoded
- [CI/CD](/concepts/ci-cd.md) — automating multi-environment edge delivery
- [observability](/concepts/observability.md) — logging endpoints and traceability
- [Terraform](/entities/terraform.md) — the tool the module is built on
- [HashiCorp](/entities/hashicorp.md) — Terraform's maker
