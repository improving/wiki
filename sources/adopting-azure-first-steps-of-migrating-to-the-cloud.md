---
title: "Adopting Azure – First Steps of Migrating to the Cloud"
type: "Source Summary"
description: "Applies Microsoft's Cloud Adoption Framework to early Azure migration: network isolation, resource organization, tagging, and naming."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, microsoft, improving.com]
sources:
  - "references/improving.com/adopting-azure-first-steps-of-migrating-to-the-cloud/adopting-azure-first-steps-of-migrating-to-the-cloud.md"
---

# Adopting Azure – First Steps of Migrating to the Cloud — Summary

**Original source**: `references/improving.com/adopting-azure-first-steps-of-migrating-to-the-cloud/adopting-azure-first-steps-of-migrating-to-the-cloud.md`

## Summary

Enterprises migrating to Azure should get environment configuration right early, because changing deployments after resources become interdependent is painful — even a rename can break dependencies. Drawing on Microsoft's Cloud Adoption Framework, the post covers networking, resource organization, tagging, and naming conventions as first steps.

## Key Claims

- Microsoft's Cloud Adoption Framework provides guidance across migration scenarios, security, governance, and strategy for before, during, and after adoption.
- Avoid "allow all traffic" defaults; use Virtual Networks to isolate resources privately, alongside Azure Firewall, VPNs, and Network Security Groups.
- Deploy resources deliberately, creating separate management groups and subscriptions for production, test, development, sandbox, and platform.
- Azure Policies can deny non-compliant deployments and continuously monitor the environment for policy compliance.
- Apply tags such as owner, project, and business unit so resources are traceable and filterable for reporting and billing.
- Use the Framework's suggested resource-type abbreviations for a consistent naming convention.

## Relevance

Guides early [cloud migration](/concepts/cloud-migration.md) on Azure and shows [policy as code](/concepts/policy-as-code.md) and [infrastructure as code](/concepts/infrastructure-as-code.md) practices, with [data governance](/concepts/data-governance.md) implications from tagging.

## Quality

Practitioner how-to by Nik Bergen, grounded in Microsoft's own framework and a client example; concrete but introductory.

## Entities Mentioned

- [Microsoft](/entities/microsoft.md) — vendor whose Cloud Adoption Framework guides the advice
- [Microsoft Cloud Adoption Framework](/entities/cloud-adoption-framework.md) — the migration and governance guidance referenced

## Concepts Covered

- [cloud migration](/concepts/cloud-migration.md) — moving on-premises systems to Azure
- [policy as code](/concepts/policy-as-code.md) — Azure Policies denying non-compliant deployments
- [infrastructure as code](/concepts/infrastructure-as-code.md) — organized, repeatable resource deployment
- [data governance](/concepts/data-governance.md) — tagging for ownership and traceability
