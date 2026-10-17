---
type: Reference
title: "The Fourth Principle: Federated Governance and the Hardest Problem in Data Mesh"
resource: "https://www.devlinliles.com/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh/"
author: "Devlin Liles"
published: '2026-07-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Zhamak Dehghani published her data mesh article in May 2019. Most of the attention landed on two of the four principles: domain-oriented ownership and data as a product. Those two are conceptually satisfying and relatively tractable. You can reorganize teams. You can define what a data product looks like. You can make progress on both without fundamentally restructuring how governance works.

The fourth principle, federated computational governance, is the one most organizations quietly skip, and it's the one that determines whether the whole thing holds together.

The idea is this: central standards, domain autonomy, and computational enforcement. Domains own their data products. A global governance layer sets interoperability standards: common schemas, security requirements, privacy policies, regulatory compliance. And critically: that governance layer enforces those standards computationally, not through committees and review processes. Policy as code. Enforcement at runtime.

The third part is where most implementations stall.

## Why the First Three Principles Are Tractable

Domain ownership makes sense to engineers. Owning the data your team produces is a cleaner accountability model than having a central data team be responsible for understanding every domain's semantics. If the logistics team owns logistics data and builds it as a product with SLAs, there's a clear owner when something breaks.

Data as a product gives engineers a frame they can work with. Think about the downstream consumer. Define the interface. Document the contract. Publish to a discoverable catalog. That's software product thinking applied to data, and engineers know how to build products.

These two principles distribute responsibility in a way that scales. A central lake owned by a central team is a bottleneck. Distributed data products, each owned by the domain that produces them, can scale with the business.

## Where the Fourth Principle Gets Hard

The computational enforcement part requires things that most organizations don't have ready. Domains need to be able to autonomously publish data products, which means they need infrastructure that doesn't require the platform team to intervene for every deployment. That's a self-serve data platform, the third principle. Most organizations underinvest in this, which means domain teams can't move independently even when they're supposed to.

But the harder problem is the governance piece. Academic research on data mesh implementations (specifically a study of fifteen industry expert interviews) identifies the shift from centralized to federated governance as the dominant challenge practitioners face. The researchers found something specific: domain employees are often "unaware of which data are protected and regulated." The domain engineer building the data product doesn't know which fields are subject to GDPR, which tables contain PII, or which outputs require regulatory review. The knowledge lived in the central data team. You can't federate what hasn't been made explicit.

This creates an accountability gap that's different from the earlier governance failures. In the old model, governance failed because the central team couldn't enforce policies everywhere. In the mesh model, governance fails because the domains can't comply with policies they don't fully understand, and there's no central enforcement mechanism to catch the gaps. You've distributed ownership, but you haven't distributed the knowledge required to exercise that ownership responsibly.

ThoughtWorks, one of the early advocates for data mesh, eventually put a warning on their own Technology Radar: vendors were "distracting organizations from the hard socio aspects" of data mesh: the decentralized ownership, the operating model, the change management. The tooling is not the bottleneck. The human system is.

## What We Learned at BCBSM

When Improving was building the data platform for Blue Cross Blue Shield of Minnesota, we were dealing with a version of the federated governance problem at scale. BCBSM's Analytical Store spans eleven domains, 133 subdomains, and 88-plus data suppliers. Not a simple hub-and-spoke model. A complex, distributed ecosystem of data producers, each with their own processes, their own systems, and their own understanding of what the data means.

The approach we used (a medallion architecture in Databricks with Unity Catalog as the governance layer) was specifically designed to solve the federated enforcement problem. Unity Catalog sits below the compute layer. Domain teams can work in their own Databricks workspaces, with their own development practices, while the catalog enforces access policies and lineage tracking at the storage level. They can't accidentally expose PII to unauthorized consumers, because the authorization check happens before the data reaches them, not after.

The domain inventory and portfolio onboarding framework we built handles the knowledge problem: when a new data supplier is onboarded, there's a structured process for mapping data assets, identifying sensitive fields, and establishing ownership and SLOs. The governance knowledge that lived in one team's heads got encoded into an onboarding workflow that can be executed consistently across all 88-plus suppliers.

That's what computational governance actually looks like in practice. Not policy documents sent to domain teams. Not a central governance committee that reviews everything. A platform with governance built in, an onboarding process that captures governance requirements upfront, and enforcement that runs automatically every time data moves.

## The Honest Assessment

Data mesh works. Netflix, Zalando, Intuit, and Roche have implemented meaningful versions of it. But academic and practitioner reviews consistently reach the same conclusion: the successful implementations share a pattern. They started small. They invested in the self-serve platform before the federated model could work. They encoded governance requirements into the platform rather than trying to train domain teams on everything they needed to know.

If domains lack engineering capacity to own products (a real constraint in many organizations), the federated model doesn't help them. Decentralizing ownership to teams that can't exercise it just moves the bottleneck without removing it. In those cases, the pragmatic path is to centralize longer and invest in building domain capability before federating.

The fourth principle is the right goal. The path to it is slower and harder than the principle makes it sound. That's not a reason to abandon it. It's a reason to be honest about what has to be true before it can work.

---

*Sources: Zhamak Dehghani, "How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh" (martinfowler.com, May 20, 2019); Dehghani, Data Mesh: Delivering Data-Driven Value at Scale (O'Reilly, 2022); arXiv 2302.01713, "Towards Avoiding the Data Mess" (15 expert interviews); arXiv 2304.01062 gray-literature review; ThoughtWorks Technology Radar; Improving/BCBSM Xcelerate Health Data & AI Platform case study.*
