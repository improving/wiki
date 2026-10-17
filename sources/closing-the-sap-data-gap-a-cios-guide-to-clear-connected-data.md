---
title: "Closing the SAP Data Gap: A CIO’s Guide to Clear, Connected Data"
type: "Source Summary"
description: "Argues CIOs should keep S/4HANA core clean by moving customizations to BTP, and use Business Data Cloud to join SAP with non-SAP data."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, platform, improving.com]
sources:
  - "references/improving.com/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data.md"
---

# Closing the SAP Data Gap: A CIO’s Guide to Clear, Connected Data — Summary

**Original source**: `references/improving.com/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data.md`

## Summary

CIOs face pressure to modernize and add AI without destabilizing the SAP core, and the common mistake is building customizations either directly inside core ERP or in disconnected systems. The post explains SAP's clean core model: build customizations on BTP so upgrades do not touch them, reducing technical debt and avoiding freezes. It cites Improving's xi.Orion vendor portal, built on BTP with Joule, as an example, and notes Business Data Cloud's connectors to Databricks, Snowflake, and Microsoft Fabric. It closes with advice for organizations mid-migration: address clean core and data/analytics before go-live.

## Key Claims

- Building custom processes inside core ERP makes upgrade cycles long and painful; disconnected systems create the same integration burden.
- SAP's recommended approach is to build customizations on BTP, which everything in the SAP Business Suite sits on top of.
- When development happens on BTP, an S/4 upgrade does not touch those processes, and moving workflows out of core can remove the need for some S/4 user licenses.
- xi.Orion, built on BTP following clean core, lets vendors self-serve on purchase requisitions, purchase orders, and invoice payment status, and use Joule to check approval status without touching core ERP.
- Business Data Cloud includes standard connectors to non-SAP systems with direct access to Databricks, Snowflake, and Microsoft Fabric; zero-delta copy for Fabric was expected to reach GA in the second half of the year.
- Mid-migration priorities: move the heaviest custom processes to BTP before go-live, and define the data and analytics program early so users have reports from day one.
- An eighteen-month target: S/4HANA with BTP handling integration (replacing PI/PO), clean core in practice, Business Data Cloud connecting external data, and SAP Analytics Cloud for reporting and forecasting.

## Relevance

Frames [ERP consolidation](/concepts/erp-consolidation.md) and [data platform modernization](/concepts/data-platform-modernization.md) around SAP's clean core, using [SAP BTP](/entities/sap-btp.md) for extension and [data integration](/concepts/data-integration.md) across warehouses.

## Quality

Practitioner guide by Sean Antonello; the most concrete of the SAP series, with a named internal product, but still vendor-aligned.

## Entities Mentioned

- [SAP](/entities/sap.md) — ERP vendor
- [SAP S/4HANA](/entities/sap-s4hana.md) — the core to keep clean
- [SAP BTP](/entities/sap-btp.md) — extension and integration platform
- [SAP Business Data Cloud](/entities/sap-business-data-cloud.md) — connectors to non-SAP data
- [SAP Analytics Cloud](/entities/sap-analytics-cloud.md) — reporting and forecasting layer
- [Microsoft Fabric](/entities/microsoft-fabric.md) — non-SAP data source
- [Databricks](/entities/databricks.md) — non-SAP data source
- [Snowflake](/entities/snowflake.md) — non-SAP data source
- [Sean Antonello](/entities/sean-antonello.md) — author

## Concepts Covered

- [ERP consolidation](/concepts/erp-consolidation.md) — clean core and unified record
- [data platform modernization](/concepts/data-platform-modernization.md) — modern analytics alongside SAP
- [data integration](/concepts/data-integration.md) — joining SAP and external data
- [master data management](/concepts/master-data-management.md) — preserving SAP master relationships
