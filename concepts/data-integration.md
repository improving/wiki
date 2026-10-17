---
title: "data integration"
type: "Concept"
description: "Connecting and consolidating data across sources, batch and streaming."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, integration, engineering]
sources:
  - "/sources/data-integration-engineering-companies.md"
  - "/sources/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data.md"
  - "/sources/etl-modernization-informatica-to-confluent-databricks.md"
  - "/sources/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md"
  - "/sources/closing-the-sap-data-gap-how-chros-turn-people-data-into-informed-action.md"
  - "/sources/what-is-group-reporting-in-sap-s-4hana.md"
---

# data integration

Data integration connects fragmented systems and moves data reliably into a form analytics, applications, and AI can use, replacing manual reconciliation with a trusted foundation. The corpus frames it as a spectrum from overnight batch ETL through streaming and API-led patterns, with governance built in from day one.

## Key Claims

- IT teams spend 39% of their time building custom integrations (Salesforce); organizations using fully managed ELT pipelines are nearly twice as likely to exceed ROI targets on the reclaimed time (Fivetran); 73% run hybrid cloud (Flexera) ([data integration guide](/sources/data-integration-engineering-companies.md)).
- Common models span batch ETL/ELT, real-time streaming (Kafka, Confluent, Azure Event Hubs), API-led integration (REST, GraphQL, iPaaS), cloud warehouse and lakehouse modernization, and fully managed data engineering ([data integration guide](/sources/data-integration-engineering-companies.md)).
- Legacy batch ETL such as Informatica becomes a bottleneck through tightly coupled integrations, costly scaling, on-premises overhead, batch delays, and weak built-in governance ([ETL modernization](/sources/etl-modernization-informatica-to-confluent-databricks.md)).
- SAP Business Data Cloud includes standard connectors to non-SAP systems with direct access to Databricks, Snowflake, and Microsoft Fabric, and a zero-delta copy for Fabric ([CIO's guide](/sources/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data.md)).
- SAP Integration Suite on BTP replicates employee master data from SuccessFactors into S/4HANA and keeps transactional systems in sync, so HR and finance can work from one model ([CHRO's guide](/sources/closing-the-sap-data-gap-how-chros-turn-people-data-into-informed-action.md)).
- A price-optimization engagement joined Databricks lakehouse operational data to S/4HANA financial data with Business Data Cloud's zero-delta copy, giving real-time access without a stale copy ([COO's guide](/sources/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md)).
- Where systems stay separate, embedded consolidation such as S/4HANA Group Reporting can read the Universal Journal live, avoiding an ETL or data-warehousing step entirely ([group reporting](/sources/what-is-group-reporting-in-sap-s-4hana.md)).

## Related

- [ETL](/concepts/etl.md) and [real-time data streaming](/concepts/real-time-data-streaming.md) — the batch and streaming ends of the spectrum
- [master data management](/concepts/master-data-management.md) — aligning the entities being integrated
- [modern data platform](/concepts/modern-data-platform.md) and [data governance](/concepts/data-governance.md)
- [SAP BTP](/entities/sap-btp.md), [SAP Business Data Cloud](/entities/sap-business-data-cloud.md), [Confluent](/entities/confluent.md)
