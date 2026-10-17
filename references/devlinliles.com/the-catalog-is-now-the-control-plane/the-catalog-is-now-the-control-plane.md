---
type: Reference
title: "The Catalog Is Now the Control Plane"
resource: "https://www.devlinliles.com/the-catalog-is-now-the-control-plane/"
author: "Devlin Liles"
published: '2026-08-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2021, Gartner retired the Metadata Management Magic Quadrant and replaced it with a market guide. In 2025, they launched the inaugural Magic Quadrant for Data and Analytics Governance Platforms. That four-year arc, from a market guide signaling disruption to a Magic Quadrant signaling consolidation, is the most useful single indicator of where governance ended up.

The consolidation Gartner is naming is real and consequential: point tools are converging into unified platforms that govern both data and AI. Not data governance over here and AI governance over there. A single control plane that tracks lineage, enforces access, monitors quality, and governs model outputs with the same infrastructure.

This is the frontier that the previous eight posts were building toward.

## What AI-Augmented Catalogs Actually Do

The term "AI-augmented catalog" covers three distinct capabilities worth separating.

The first is automated metadata generation. The historical problem with catalogs was that they depended on humans writing descriptions, tagging assets, and maintaining documentation. AI-augmented catalogs use language models to generate initial metadata from the data itself: descriptions of what a table contains, suggested tags for sensitivity classification, identification of potential PII. They pull from column names, from existing documentation. The human reviews and approves; the AI does the first-pass curation. This removes the most friction-heavy part of the governance workflow: starting from a blank page.

The second is semantic search and discovery. Rather than requiring analysts to know the exact name of the table they're looking for, AI-augmented catalogs let them ask in natural language. "Find me a customer-level table that includes purchase history and churn risk signals" is a query that a semantic layer can execute against the catalog's understanding of what each asset contains, not just its name and description. Discovery improves dramatically when analysts can express intent rather than remembering taxonomy.

The third is agentic governance. This one is still being built in real time. Alation's Agentic Platform (released in beta after acquiring Numbers Station AI in May 2025) and Collibra's AI Governance capability (after acquiring Deasy Labs in July 2025 for unstructured and LLM asset governance) both point in the same direction: governance that doesn't just observe but acts. An agent that detects a policy violation and creates a remediation workflow. An agent that monitors model drift and triggers a governance review. An agent that classifies unstructured data assets ingested by a RAG system and applies appropriate access controls automatically.

That last use case is the new frontier: governing the unstructured data that feeds generative AI. RAG systems pull from document stores, email archives, web content, and internal knowledge bases. These aren't traditional tables with schemas and documented ownership. They're blobs of content with complex privacy and accuracy implications. Governing them requires capabilities that classical data governance frameworks weren't designed for.

## The BCBSM View of What's Coming

At BCBSM, the AI/BI Genie capability represents the near-term version of AI-augmented governance. Analysts query curated Gold-layer datasets in natural language. The system answers from governed data: access-controlled, lineage-tracked, and quality-validated by Unity Catalog. The analyst gets AI assistance on top of trustworthy data. The governance isn't loosened to enable the AI experience; it's what makes the AI experience reliable.

When we built out the Mosaic AI Agent Framework for BCBSM, the same principle applied at higher complexity. Production AI agents with multi-step reasoning and RAG needed to pull from BCBSM's internal knowledge base and health plan data. The governance controls (which data the agents could access, which queries they could execute, what they were allowed to include in responses) were enforced through Unity Catalog and AI Gateway. The agent was powerful because the data it operated on was trustworthy and appropriately permissioned.

This is the direction the whole field is moving. AI capabilities that are reliable because they're built on governed data, with governance that runs in the platform rather than in a committee.

The MLflow Model Registry gave BCBSM's data science team something they didn't have before: a governance layer for the models themselves. Every model in the registry has documented lineage to its training data, captured evaluation metrics, and an approval record before it advances from Dev through Stage and UAT to production. Model governance is a natural extension of data governance when the platform provides the infrastructure for both.

## The Interoperability Bet

The broader architectural bet, from both Databricks and Snowflake, is that the catalog becomes the universal control plane through open standards. Databricks open-sourced Unity Catalog under the Linux Foundation in mid-2024 and added support for Apache Iceberg REST Catalog, allowing external engines to interact with Unity Catalog governance policies. Snowflake's Horizon is built on Apache Polaris, the same Iceberg REST standard.

The intent is that policy follows data across engines. An access policy defined in the catalog governs that data wherever it travels: Databricks, Snowflake, external compute environments. The governance isn't tied to a specific vendor's processing layer; it's tied to the catalog, which sits below and across all of them.

The practical reality in 2026 is that cross-catalog policy enforcement is still imperfect, as discussed in an earlier post. But the direction is clear: the industry is converging on the catalog as the authoritative governance layer, not as a documentation artifact alongside the platform.

## Where the Series Lands

This nine-post series started with a statistic from 2020: 8% of governance programs were highly successful. The policy-practice gap was structural, the frameworks were mature but ineffective, and the root cause was behavioral. You can write a policy, but you can't make people follow it with a policy document.

Six years of change later, the picture is different. Governance is embedded in platforms. Policies execute at runtime. Contracts enforce quality at build time. Observability detects anomalies before stakeholders do. Federated ownership is becoming tractable as platforms provide the computational enforcement that makes decentralization safe. AI governance is extending the same infrastructure to training data, feature stores, and model lineage.

The 80% failure prediction is still accurate for programs that haven't made this transition. Running governance as hygiene and compliance, with bolt-on tools and human-effort curation, still produces the same failure modes documented in 2020.

But the organizations that have made the architectural shift (governance runs in the platform, policies execute automatically, the catalog functions as the control plane) are building something durable. They're not perfect. They still have interoperability problems and coverage gaps and organizational change challenges. But they've solved the structural problem.

The policy binder didn't change anyone's behavior. The control plane does.

---

*Sources: Gartner inaugural Magic Quadrant for Data and Analytics Governance Platforms (2025); Alation Agentic Platform (beta, May 2025, following Numbers Station AI acquisition); Collibra AI Governance (following Deasy Labs acquisition, July 2025); Databricks Unity Catalog OSS (Linux Foundation, mid-2024); Apache Iceberg REST Catalog / Apache Polaris; Gartner survey of 1,203 data management leaders (July 2024); Improving/BCBSM Xcelerate Health Data & AI Platform case study.*
