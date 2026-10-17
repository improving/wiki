---
title: "Co-development in Power BI: Version Control and Continuous Integration and Continuous Delivery (CI/CD)"
type: "Source Summary"
description: "Power BI Project files and Fabric developer mode bring Git version control and CI/CD to Power BI reports."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, microsoft, improving.com]
sources:
  - "references/improving.com/co-development-in-power-bi-version-control-and-continuous-integration/co-development-in-power-bi-version-control-and-continuous-integration.md"
---

# Co-development in Power BI: Version Control and Continuous Integration and Continuous Delivery (CI/CD) — Summary

**Original source**: `references/improving.com/co-development-in-power-bi-version-control-and-continuous-integration/co-development-in-power-bi-version-control-and-continuous-integration.md`

## Summary

Eduardo Ferreira explains how Power BI Desktop Developer Mode and Fabric solve a longstanding collaboration problem: PBIX files are binary and not diffable, so multiple developers cannot easily track changes. Saving reports as Power BI Project (PBIP) files splits the report and dataset into diffable text files that can be tracked in Git, enabling co-development, Git integration with a Power BI Service workspace, and deployment pipelines that promote reports from development to test to production. The post walks through enabling the preview feature, initializing a repository in VS Code, and wiring the workspace to DevOps.

## Key Claims

- PBIX files are binary and not directly diffable, so collaborative editing is hard to track.
- Power BI Project (PBIP) files split report and dataset definitions into diffable text files.
- PBIP files can be tracked in Git (for example in VS Code) and hosted on GitHub or Azure DevOps.
- Fabric's Git integration links a Premium workspace to a repo, tracking changes without republishing.
- Deployment pipelines promote reports from development to test to production.
- Git integration and deployment pipelines require Fabric and a Premium workspace.

## Relevance

Brings [CI/CD](/concepts/ci-cd.md) to [business intelligence](/concepts/business-intelligence.md) work, echoing the governance concerns of [low-code development](/concepts/low-code-development.md).

## Quality

Hands-on how-to by Eduardo Ferreira; step-by-step and current, but preview-feature and Fabric-dependent.

## Entities Mentioned

- [Power BI](/entities/power-bi.md) — the reporting tool being version-controlled
- [Microsoft Fabric](/entities/microsoft-fabric.md) — provides Git integration and pipelines
- [GitHub](/entities/github.md) — a hosting option
- [Microsoft](/entities/microsoft.md) — the vendor

## Concepts Covered

- [CI/CD](/concepts/ci-cd.md) — automated promotion across environments
- [business intelligence](/concepts/business-intelligence.md) — the domain of Power BI
- [low-code development](/concepts/low-code-development.md) — Power Platform's low-code context
