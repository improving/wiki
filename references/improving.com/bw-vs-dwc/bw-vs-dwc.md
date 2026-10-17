---
type: Reference
title: "(BW vs BW on HANA vs BW/4HANA) vs Data Warehouse for Cloud (DWC)"
resource: "https://www.improving.com/thoughts/bw-vs-dwc/"
author: "Shelby Sansone Stephens"
published: '2022-05-04'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

SAP BW is constantly evolving. New features are added in SAP BW on HANA up to the BW 7.5 version. Many of the limitations of the previous classic version of BW are overcome in the latest version of SAP BW/4HANA.

SAP BW on HANA and SAP BW/4HANA are different application suites running on the same database. BW on HANA uses SAP’s legacy BW software but moves it to the HANA database, while BW/4HANA uses a re-engineered software suite designed to fully harness the power of the HANA database.

### BW vs DWC

BW is the classic SAP data warehouse solution. Typically, BW replicates SAP source systems data using pre-installed BI Content but can also be enhanced, according to customer requirements.

BW requires hardware and software installation, and this hardware will need administration activities (Backups, DB optimizations, Software updates, etc.)

### What is DWaaS (Data Warehouse as a Service)?

DWaaS is an outsourcing model in which a service provider configures and manages the hardware and software resources required for a data warehouse, and the customer provides the data and pays for the managed service. Because the service provider is responsible for administration and management, the customer does not have to worry about staffing the data warehouse.

DWC is a DWaaS solution. It also replicates data from several sources into a Cloud DB. It doesn’t require a hardware installation or DB Admin activities.

SAP is working on the integration of all the SAP platforms to enhance the communication between DWC and several (SAP and non-SAP) source systems.

This table compares the characteristics of the different SAP data warehouse products.

## So Which Product is Better?

*The answer depends on what you need*:

Accelerated implementation? Good performance? Constant evolution?

There are some considerations to take into account when choosing your platform:

### Implementation Time

Developments in DWC are made from scratch, while BiContent (pre-installed BW solution) supports operational SAP applications. Bear in mind that BiContent (in most cases) will need adjustments and enhancements to suit customer requirements.

### Performance

Currently, SAP HANA (in-memory database) is the most efficient (and SAP-integrated) database, but in the near future, DWC will increasingly approach the efficiency of HANA DB.

### Hardware

DWC has a great advantage over BW: you don’t need to manage a database.

Consider this comparison of qualities for each SAP data warehouse product:

**SAC Connectivity**

**DWC -> SAC**

There are two ways to visualize data from DWC in SAC.

- Space Aware Connectivity: As part of the embedded strategy of the SAP Analytics Cloud, each SAP data warehouse cloud contains an SAP Analytics Cloud embedded version. With this, you can directly access the data that is available in the warehouse. If DWC and SAC are on the same Tenant, they are automatically connected.
- Cross-Tenant Connectivity: When DWC and SAC are in different Tenants.

**BW on HANA and BW/4HANA -> SAC**

BW on HANA and BW/HANA and be configured as SAC data sources. BW versions prior to 7.4 are not supported as SAC data sources, however, it is possible to load flat files from any system.

At **Improving**, as SAP Gold Certified partners, we can help you understand these data warehouse products and which would be most suitable for your organization and help you implement the best solution for you.
