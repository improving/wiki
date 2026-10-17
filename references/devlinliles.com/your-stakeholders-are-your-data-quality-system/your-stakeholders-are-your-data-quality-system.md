---
type: Reference
title: "Your Stakeholders Are Your Data Quality System"
resource: "https://www.devlinliles.com/your-stakeholders-are-your-data-quality-system/"
author: "Devlin Liles"
published: '2026-07-25'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2023, 74% of data professionals said business stakeholders find data quality issues "all or most of the time" before the data team does. That number was 47% the year before. Not a marginal drift. A 57% increase in one year.

Read that again. At most organizations, the primary data quality monitoring system is the person building the dashboard who notices something looks wrong. Not a test suite. Not an observability platform. The end user.

This is what data quality failure looks like at scale, and it has a specific cost. Monte Carlo tracked mean time to resolution for data incidents: it rose from roughly six hours per incident in 2022 to fifteen hours in 2023. During those fifteen hours, someone downstream is either building on bad data or has stopped building anything because they don't trust what they have. Neither is good. The first is worse.

## The Testing Didn't Scale

The instinct was always to write more tests. The average data team in Monte Carlo's 2023 survey had 290 tests covering 24 dbt models. That sounds substantial until you work out the ratio: roughly twelve tests per model. And the models being tested are not the whole estate. They're the ones someone decided were important enough to write tests for.

The problem is coverage. Manual testing scales with engineering time. The data estate scales with business complexity. In most organizations these two curves diverge quickly. The team grows linearly; the number of datasets, tables, pipelines, and dependencies grows faster. By the time you have a meaningful data platform, there are more tables than anyone has written tests for, and the untested ones are usually the legacy ones: the exact tables that have been quietly wrong for six months and nobody noticed because the report consumers had learned to distrust the numbers and stopped using them.

The observability category emerged from this gap, and it emerged from a specific problem: how do you know a table is broken without having written a test that catches the specific way it's broken? The answer Monte Carlo, Bigeye, and others built is statistical monitoring. Track the distribution of values, the row counts, the freshness, the schema. When something changes in a way that's anomalous (not wrong in a way anyone anticipated, but unusual relative to the table's own history), surface it. Flag it before the stakeholder does.

This is the governance insight wrapped in an engineering capability. The data contract says "this table will have between 100,000 and 200,000 rows every morning by 6 AM." Observability is what detects when it doesn't.

## The Ascend Model: Automation as Governance

When we partnered with Ascend, a charter school system, their data problem was not observability tooling. It was deeper: they had no reliable data infrastructure at all. Their data strategy was immature, processes were manual, and they were dependent on vendors for critical educational data that they didn't own.

Improving built them a data platform on Snowflake, dbt, and Dagster. But the architecture decision that had the most governance impact was the simplest one: bringing data management in-house. Ascend's data had been flowing through vendor systems in ways that made it hard to know what existed, where it came from, or how accurate it was. The first governance move was establishing ownership: which datasets are ours, who is responsible for each one, and what are the quality expectations.

Then automation followed. The dbt models they now run have explicit contracts. When a pipeline produces output that doesn't conform to the declared schema, the build fails. The failure is not a stakeholder noticing something is off in a report. It's an automated system at the point of data production saying "this doesn't match what we agreed this output should look like." That is governance at the right place in the cycle.

The improvement in data quality was real. Decision-making that had been slowed by uncertainty about whether the data could be trusted got faster. Not because the data magically got better, but because the system now told you when it was good and when it wasn't. Trust in the data infrastructure improved because the infrastructure became trustworthy, which is different from hoping it is.

## dbt Contracts: Governance at Build Time

dbt Core v1.5, released in April 2023, shipped three governance primitives that deserve attention even if the changelog entry didn't make headlines: access, contracts, and versions.

Access controls who can reference a model. A data product team can mark a model as private, meaning downstream teams outside the owning group can't take a dependency on it. Contracts enforce that the model produces exactly the schema you declared in the YAML: column names, types, and constraints, checked at compile time, before the table is materialized. Versions manage breaking changes in a way that gives downstream consumers time to migrate.

These three features together are what "governance as code" means at the engineering level. The access policy isn't in a catalog that someone reads periodically. It's enforced by the build tool. The contract isn't a documented expectation that downstream teams might be aware of. It's a compile-time check that fails before bad output reaches production. The version control isn't a communication plan. It's a migration path with deadlines built in.

The reason this matters is the same reason the observability argument matters: governance that runs in the system is governance that runs every time the system runs. It doesn't require anyone to remember to check the catalog. It doesn't depend on a data steward being available to review a schema change. It executes as a side effect of doing the engineering work. That is the only kind of governance that will actually cover the whole estate.

## What Organizations Still Get Wrong

Deploying observability tooling without establishing ownership first is the most common mistake I see. You get alerts. You don't know whose job it is to act on them. The incident goes stale because no team claims it as theirs, and fifteen hours of mean-time-to-resolution becomes a week.

The operational model for data observability is not "add the tool and watch the dashboard." It's "define which team owns which data product, establish SLOs for that product, configure monitoring against those SLOs, and build an on-call rotation for when the SLOs breach." That is not a technology deployment. It's an organizational commitment.

The teams that use observability well treat it the same way an engineering team treats production monitoring. There is an SRE (or equivalent) culture around data quality. Someone is on call. Incidents have owners. Resolution timelines are tracked. The tool is the detection mechanism. The process is the response mechanism. You need both.

The 74% figure (stakeholders catching issues first) is not a data observability benchmark you should be comfortable with. It's the number that tells you your governance is running in your users' heads. That's the most expensive monitoring system you can have.

---

*Sources: Monte Carlo State of Data Quality surveys (Wakefield Research; 200 professionals March 2023, ~300 in 2022 edition); dbt Core v1.5 release notes (April 2023); Improving/Ascend Data Estate Maturity case study.*
