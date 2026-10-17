---
title: "SAP Datasphere"
type: "Entity"
description: "SAP's cloud business data fabric for governed self-service analytics, evolution of Data Warehouse Cloud and home of BW Bridge."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, sap, analytics]
sources:
  - "/sources/sap-datasphere-bw-bridge-the-way-to-the-cloud.md"
  - "/sources/achieving-self-service-and-data-independence-in-an-sap-world.md"
  - "/sources/closing-the-sap-data-gap-how-chros-turn-people-data-into-informed-action.md"
---

# SAP Datasphere

SAP's cloud data fabric that harmonizes SAP and non-SAP data while preserving business context, giving business users self-service analysis without IT losing governance. In this corpus it is the answer to "data independence" in an SAP world — the layer that lets users access and report on data without being constrained by its source. It is the evolution of SAP Data Warehouse Cloud, adding integration, cataloging, semantic modeling, warehousing, and virtualization.

## Capabilities

- Prepackaged connectors to SAP and non-SAP systems, with real-time federated access or replication chosen by need and data volume.
- A knowledge graph expresses semantic relationships between datasets, so business users can see dependencies.
- Two modeling builders: a data builder for integration and a business builder for refining datasets in business terms.
- Spaces create logical containers for datasets; data tiering scales compute and storage to usage patterns.
- Governance features including [data-lineage](/concepts/data-lineage.md) keep quality and compliance intact from ingestion to access.

## BW Bridge

- BW Bridge provides a migration route from on-premises SAP BW to the cloud, reusing existing extractors, ABAP code, and ETL processes instead of rebuilding.
- It brings SAP BW features into Datasphere: connectivity and business content for ECC and [SAP S/4HANA](/entities/sap-s4hana.md), staging layers with partitioning and error handling, and tool-supported migration.
- Not all object types can be migrated; migration supports remote and/or shell conversion.

## Related

- [SAP](/entities/sap.md) — the ERP environment Datasphere de-silos
- [semantic-layer](/concepts/semantic-layer.md) — governed business meaning over physical data
- [data-governance](/concepts/data-governance.md) — policies and controls over data
- [business-intelligence](/concepts/business-intelligence.md) — decision-ready reporting
