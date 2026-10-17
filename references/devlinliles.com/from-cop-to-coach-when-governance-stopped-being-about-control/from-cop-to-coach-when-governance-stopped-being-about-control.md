---
type: Reference
title: "From Cop to Coach: When Governance Stopped Being About Control"
resource: "https://www.devlinliles.com/from-cop-to-coach-when-governance-stopped-being-about-control/"
author: "Devlin Liles"
published: '2026-07-25'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In August 2021, Gartner retired its Magic Quadrant for Metadata Management Solutions. They replaced it with a Market Guide for Active Metadata Management. That is a sentence that looks like analyst housekeeping but is actually a declaration about the entire direction of the discipline.

The retirement wasn't about market consolidation. It was about what metadata was being asked to do. The old framing treated a catalog as an inventory: passive metadata management. You put things in it. People looked at things. Someone curated it. The value was documentation. The new framing was something else entirely: always-on, intelligence-driven, action-oriented. Metadata that does things, not just describes them.

Gartner's description of the difference is worth quoting: passive metadata "relies on human effort to curate," while active metadata is a system that doesn't wait for humans to maintain it. That is the shift in one sentence. Not a change in tooling. A change in what governance is for.

## What "Active" Actually Means

The word got picked up fast. Vendors love a Gartner-coined distinction. But the shift entails something specific in practice.

Passive governance looks like this: you have a data warehouse. You also have a catalog. The catalog has documentation about some of the tables in the warehouse, written by someone at some point in the past. When an analyst wants to understand a dataset, they might check the catalog. They might not. When a column gets renamed or deprecated, the catalog may or may not be updated. The catalog is a reference, not a control.

Active governance looks like this: when a pipeline runs, lineage is captured automatically. When access is requested for a sensitive table, a policy evaluation happens in real time. When a data quality threshold is breached, a notification fires and the downstream consumers know before they build a report on stale data. The catalog isn't a documentation artifact. It's a participant in the data system.

The organizational translation of that shift is what Alation captured clearly: passive governance "perceives data through the lens of risk" and "commands who can do what." Active governance formalizes how people already work. One is a compliance mechanism. The other is an enablement mechanism. By 2024, Gartner had reframed governance itself: not from control to chaos, but from control to enablement. The goal isn't restriction. It's giving people trustworthy data faster.

## Why This Matters More Than a Taxonomy Argument

The passive/active distinction is easy to dismiss as analyst wordplay. It isn't. It has direct operational consequences.

A passive catalog requires a maintenance budget. Someone, typically a data steward, has to manually update the catalog when the underlying systems change. That budget is almost always underfunded, which is why passive catalogs go stale. The documentation was accurate six months ago. The system changed. Nobody updated the catalog. The analyst looking at it today doesn't know which version they're reading.

An active catalog eliminates that maintenance loop for a large class of metadata. Runtime lineage is captured from the pipeline execution, not from a human walking through the code. Data quality metrics are computed from the data, not entered by a steward. Access patterns are observed and logged by the system. The metadata is a byproduct of system operation, not a separate human task.

This changes the governance calculus completely. When the cost of governance information drops toward zero (because the system captures it automatically), you can afford to have governance everywhere. You can monitor every table, not just the ones important enough to have a manually assigned steward. You can enforce policies at the column level, not just the dataset level. You can track lineage across the full pipeline, not just the steps that someone documented.

## The DHCS Shift in Practice

When we worked with DHCS on their California behavioral health data platform, the starting point was exactly the passive governance failure mode. Data scattered across Excel, Access, and a Teradata instance that had years of undocumented transformations baked in. Nobody had a complete picture of what data existed, where it came from, or who was responsible for it.

Deploying Collibra wasn't a documentation project. We integrated it into the pipeline architecture so that as data moved through the Databricks platform, the catalog was populated as a side effect of the pipeline running, not as a separate curation activity. The behavioral health data DHCS needed to track outcomes went from undiscoverable to searchable, lineage-tracked, and access-controlled.

The governance overhead didn't disappear. But it shifted from "people maintaining documentation" to "engineers designing systems that capture documentation automatically." That is a dramatically more sustainable model. The first depends on humans doing unglamorous work consistently over time. The second depends on engineering discipline at the architecture level, which is something engineering teams are already structured to deliver.

## The Frame That Stuck

What made the active metadata shift durable isn't the technology. Multiple vendors built active metadata capabilities: Atlan, Alation, Collibra all moved in this direction through 2022-2024. What made it durable is the reframe on what governance is trying to accomplish.

Governance framed as control is adversarial by design. The data team feels friction. The governance team feels resistance. Both readings are correct from inside their frames.

Governance framed as enablement changes that dynamic. The question is no longer "how do we stop people from doing the wrong thing." The goal is making the right thing the easy thing. When those two teams share that goal, the program actually gets data team support.

Gartner's 2027 failure prediction (that 80% of governance initiatives will fail) is rooted in this exact distinction. Programs that run as compliance exercises fail. Programs tied to enabling specific business outcomes have a fighting chance. The active metadata shift was, at its core, the industry beginning to internalize that lesson.

---

*Sources: Gartner Market Guide for Active Metadata Management (July 27, 2021; Guido De Simoni, Alan Dayley, Mark Beyer); Alation "Active vs. Passive Data Governance" blog; Gartner Predicts 2024; Improving/DHCS Data Platform case study.*
