---
title: "Microsoft Cloud Adoption Framework"
type: "Entity"
description: "Microsoft's structured guidance for cloud migration, security, governance, and strategy on Azure."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, migration, governance]
sources:
  - "/sources/adopting-azure-first-steps-of-migrating-to-the-cloud.md"
---

# Microsoft Cloud Adoption Framework

The Microsoft Cloud Adoption Framework (CAF) is [Microsoft](/entities/microsoft.md)'s structured guidance for organizations moving to Azure, covering migration scenarios, security, governance, and strategy before, during, and after adoption. In this corpus it is the reference model for getting environment configuration right early, because changing deployments after resources become interdependent is painful.

## Recommended First Steps

- **Networking:** avoid "allow all traffic" defaults; isolate resources in Virtual Networks, alongside Azure Firewall, VPNs, and Network Security Groups.
- **Resource organization:** create separate management groups and subscriptions for production, test, development, sandbox, and platform.
- **Policy:** Azure Policies can deny non-compliant deployments and continuously monitor the environment for compliance — an application of [policy as code](/concepts/policy-as-code.md).
- **Tagging and naming:** apply owner, project, and business-unit tags for traceability and billing, and use the framework's resource-type abbreviations for consistent naming.
- Even a rename can break dependencies, so the framework's emphasis on early, deliberate configuration is the core lesson.

Supporting evidence for this page is currently thin — the framework appears in a single summary here — but it is the anchor reference for Azure [cloud migration](/concepts/cloud-migration.md) guidance.

## Related

- [cloud migration](/concepts/cloud-migration.md) — the activity the framework guides
- [policy as code](/concepts/policy-as-code.md) — Azure Policies as enforced governance
- [infrastructure as code](/concepts/infrastructure-as-code.md) — organized, repeatable resource deployment
- [Microsoft](/entities/microsoft.md) — the vendor publishing the framework
