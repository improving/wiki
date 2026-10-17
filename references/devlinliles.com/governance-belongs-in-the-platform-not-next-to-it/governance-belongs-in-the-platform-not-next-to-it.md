---
type: Reference
title: "Governance Belongs in the Platform, Not Next to It"
resource: "https://www.devlinliles.com/governance-belongs-in-the-platform-not-next-to-it/"
author: "Devlin Liles"
published: '2026-07-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The bolt-on era of data governance had a predictable failure mode: the governance layer was separate from the platform where data actually moved. You had your Snowflake or Databricks instance, and then separately you had a Collibra or Alation catalog that someone was supposed to keep synchronized with the reality inside the platform. The gap between those two systems was the gap between what governance intended and what actually happened.

The shift that occurred between 2021 and 2024 closed that gap architecturally. Databricks announced Unity Catalog at their 2021 Data + AI Summit. Snowflake responded with Horizon. Both made the same bet: governance should live inside the compute and storage layer, not alongside it.

This is not a feature upgrade. It's an architectural change in where governance lives, and that location change has consequences that run through access control, lineage, quality enforcement, and eventually AI governance.

## What "Embedded" Actually Means at the Technical Level

Unity Catalog governs data at the catalog layer, below the compute engines that access it. Access control to the row and column level, automated lineage captured at query execution time, and audit logs written for every data access. This happens regardless of which Databricks interface or notebook or pipeline is running the query. The policy doesn't live in the ETL tool or the BI layer or the application. It lives in the catalog, and the catalog enforces it for everything that touches the data.

The lineage case is particularly important. In a bolt-on model, lineage is documented by humans: someone writes down that table A feeds table B feeds the dashboard. That documentation is approximately accurate on the day it's written and drifts from reality immediately after. In Unity Catalog, lineage is observed at runtime. When a pipeline runs, the catalog records what tables were read and what tables were written. The lineage graph builds automatically from actual execution, not from documentation intent.

The practical consequence: when something breaks, you can trace it. When a column gets deprecated upstream, you know which downstream assets depend on it. When a data quality incident occurs, you have the full lineage to identify every affected consumer. This is incident response for data, and it only works if the lineage data is accurate. Manual lineage documentation is not accurate enough to rely on in a production incident. Runtime-captured lineage from the platform is.

## The BCBSM Implementation

When Improving built the data platform for Blue Cross Blue Shield of Minnesota, Unity Catalog was the governance architecture, not a governance add-on. Every data asset in the Analytical Store (across eleven domains, 133 subdomains, and 88-plus data suppliers) was governed through Unity Catalog. Access control at the column level for PHI and PII fields. Automated lineage from Bronze ingestion through Silver transformation to Gold analytical outputs. Audit logs for every access, satisfying HIPAA's audit trail requirements without a separate compliance workflow.

The AI governance implication was direct. When BCBSM's data science team built AI models on Databricks, the training data those models consumed was governed by Unity Catalog. Unity Catalog knew what data went into a model because the lineage captured it. When a model went to production, there was an auditable answer to "what data trained this model, who had access to that data, and was the data appropriately governed" because Unity Catalog had tracked it from the first pipeline run.

This is the governance architecture that makes regulated AI deployable. BCBSM operated under HIPAA and HITRUST. Every AI feature had to be enabled through a formal approval process that included verifying data governance controls. Unity Catalog as the control plane gave that approval process something real to verify: not documentation assertions, but an enforced governance architecture.

Six SCAN security approvals for new capabilities across the engagement. Each one required demonstrating that governance controls were in place. The platform architecture made that demonstration straightforward because the controls were in the platform, not in a policy document somewhere.

## Ascend: The Snowflake + dbt Model

Unity Catalog and Snowflake Horizon are the platform-level solutions. dbt's governance features operate at the transformation layer. For teams not yet working in a lakehouse model, dbt's contracts, access controls, and versioning provide many of the same embedded governance capabilities, at the pipeline level rather than the storage level.

When we built Ascend's data platform on Snowflake and dbt, the governance architecture worked at the transformation layer. Access declarations in the YAML define which downstream models can reference an upstream model. Contracts enforce the schema at build time. Versions signal breaking changes before they break downstream consumers. The Dagster orchestrator provides additional observability into pipeline execution and failures.

The governance controls run every time the pipeline runs. Not on a schedule, not when a steward has time to review, not when a stakeholder notices something is wrong. During the build, as a side effect of data transformation. A schema violation fails the build before the table materializes. An unauthorized model reference fails the build before the dependency takes effect.

For a charter school system that had been dependent on vendor data systems with minimal visibility into what was happening to their data, this was a governance step change. The platform architecture established ground truth: at any point, you could ask "what does the data in this table look like, who can access it, and does it conform to its declared schema" and get an accurate answer from the system, not from documentation.

## The Interoperability Problem

The practical caveat in the embedded governance story is multi-engine environments. If your data moves across Databricks, Snowflake, and other systems (and many enterprise data estates do), you don't have one embedded governance layer, you have multiple competing ones. Unity Catalog governs assets in Databricks. Snowflake Horizon governs assets in Snowflake. The policies do not automatically synchronize.

Both vendors are converging on the Apache Iceberg REST Catalog standard as a mechanism for cross-engine interoperability, but the Snowflake engineering team's own documentation is honest about the current state: fine-grained policies do not automatically carry across catalog boundaries. Organizations running multi-engine estates have to decide whether to treat one catalog as the authority and bridge to the others, or manage governance in multiple systems independently.

This is not a reason to avoid platform-native governance. It's a reason to make deliberate architecture decisions about which catalog is authoritative and how governance information flows across system boundaries. The alternative is running separate bolt-on governance tools across all engines, which reintroduces exactly the synchronization problem that embedded governance solves.

The bet both vendors are making is correct: governance belongs in the platform. The engineering work to make that work seamlessly across multiple platforms is ongoing. The organizations that get ahead of it now will be in a better position when AI governance becomes non-negotiable. For those operating in the EU, that's a deadline, not a preference.

---

*Sources: Databricks Unity Catalog announcement (Data + AI Summit 2021; public preview April 2022); Snowflake Horizon; Databricks Unity Catalog OSS (Linux Foundation, mid-2024); Apache Polaris/Iceberg REST Catalog; Snowflake engineering blog on cross-catalog policy; dbt Core v1.5 release notes (April 2023); Improving/BCBSM Xcelerate Health Data & AI Platform case study; Improving/Ascend Data Estate Maturity case study.*
