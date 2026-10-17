---
type: Reference
title: "The Data Contract Is an API for Trust"
resource: "https://www.devlinliles.com/the-data-contract-is-an-api-for-trust/"
author: "Devlin Liles"
published: '2026-07-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

When GoCardless engineer Andrew Jones was dealing with data quality problems in 2020, he didn't reach for a new governance framework. He asked a different question: what if data had an interface the way services do?

Software engineers understand API contracts. You publish an endpoint. You document the schema. You version it when you make breaking changes. Consumers build against your specification. If you violate the spec, you've broken a contract. The downstream consumers know it. There's an enforcement mechanism.

Data didn't have that. A table could change its schema on any given morning. A pipeline could start producing nulls in a field that had never been null. A new column could appear with a name that shadowed an existing one. Downstream consumers would find out when their reports broke or when a stakeholder noticed something was wrong. The producer and consumer were connected at the storage level but invisible to each other at the contract level.

Jones called what he built at GoCardless a "data contract." The analogy is tight: it's like an API for data. An enforceable interface between the producer and the consumer, with schema declarations, ownership designations, and service-level objectives. Produce what you said you'd produce. Signal when you can't.

## What a Contract Actually Contains

A data contract isn't documentation. Documentation you can ignore. A contract is a specification that the system validates.

The core elements: schema (what columns exist, what types they are, what constraints apply), ownership (who is accountable for this data product), SLOs (freshness expectations, availability windows, row count ranges), and compatibility guarantees (how breaking changes will be signaled and managed). Some implementations add lineage declarations (where the data comes from) and quality expectations (what distributions are normal and what thresholds trigger alerting).

The enforcement is what makes it a contract. At GoCardless, the implementation ran against their inter-service event stream in BigQuery and PubSub. A pipeline producing data that violated its declared contract would fail. The violation was detectable at the producer, not at the consumer. That's the shift in accountability: the producer is responsible for what they publish, not just for getting data into a table.

Within six months, data contracts covered roughly 50% of GoCardless's asynchronous inter-service events. Analytics data was slower to adopt. The data teams that owned analytics pipelines were less accustomed to the producer-consumer mental model than the service teams that owned event streams. But the concept spread fast. Chad Sanderson at Convoy built a parallel version on Protobuf and Kafka. Microsoft documented an internal implementation. ThoughtWorks put the Data Contract CLI on their Technology Radar in the Trial ring.

## The Organizational Consequence

The governance consequence of data contracts is not primarily technical. It's organizational.

When you mandate that data products have contracts, you force the question of ownership. To write a contract for a dataset, someone has to be accountable for the declarations in it. That conversation covers the basics governance programs have been trying to settle for years: who owns this data, who is responsible when it breaks, what are the SLOs. Data contracts give it a forcing function. The contract can't exist without an owner. The CI pipeline can't validate the contract without someone having written it.

This is governance working the way software governance works. Code review is enforced by the PR process. Testing is enforced by the CI pipeline. Dependency management is enforced by the build tool. Data contracts move data governance into the same enforcement model: the policy runs in the system, not in a committee.

## Ascend: Ownership as the Foundation

When we partnered with Ascend on their data estate modernization, the fundamental governance problem wasn't tooling. It was that they didn't own their data. Their educational data flowed through vendor systems that Ascend had limited visibility into, with no clear accountability for what those systems produced or what the expectations for that data were.

The first governance move was establishing ownership. We built their platform on Snowflake, dbt, and Dagster, which brought data management in-house, and made the governance architecture the foundation. Before we wrote a single dbt model, we had a conversation about what data was whose, what each dataset was supposed to look like, and what would constitute a failure.

The dbt models we built have explicit schema declarations. The output of each model is tested against those declarations as part of the build. Not downstream, not in a monitoring dashboard, not when a stakeholder notices something is wrong. At build time, before anything reaches production. This is the data contract pattern applied at the transformation layer.

The vendor dependency that had been a governance risk (Ascend's data was in systems they didn't control, couldn't observe, and couldn't enforce standards on) became a data quality baseline that they owned. When the build passes, the schema is what they said it would be. When it fails, the system tells them before the report gets built.

## Where Contracts Have Limits

Data contracts are not magic. The GoCardless implementation was honest about this: analytics data was harder to contract than event streams because analytics datasets often have fuzzier expectations. A pipeline that generates a business intelligence table is harder to declare SLOs for than an event stream that has well-defined producers and consumers.

The other honest limitation is that contracts require maturity to write. A team that doesn't understand their own data well enough to declare its schema, ownership, and quality expectations can't write a useful contract. Data contracts are not a starting point for a governance program. They're a milestone. You need to understand your data products before you can formalize them.

The right sequencing: establish ownership first, understand the data enough to describe it, then formalize that description into a contract the system can validate. The contract is the mechanism. The ownership and understanding are the prerequisites.

That sequencing is also why data contracts and data mesh fit together naturally. The mesh principle of "data as a product" requires that domains be accountable for what they publish. The contract is the formal expression of that accountability: the declaration a domain makes to its consumers about what they're committing to. Without the contract, "data as a product" is an aspiration. With the contract, it's an enforceable commitment.

---

*Sources: Andrew Jones, "Driving Data Quality with Data Contracts" (Packt, 2023); Jones internal GoCardless conception (August 2020), public article (April 2021), implementation description (December 2021); Chad Sanderson / Convoy implementation; ThoughtWorks Technology Radar; Improving/Ascend Data Estate Maturity case study.*
