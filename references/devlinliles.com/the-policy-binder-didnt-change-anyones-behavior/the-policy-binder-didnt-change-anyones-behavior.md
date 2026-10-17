---
type: Reference
title: "The Policy Binder Didn&#x27;t Change Anyone&#x27;s Behavior"
resource: "https://www.devlinliles.com/the-policy-binder-didnt-change-anyones-behavior/"
author: "Devlin Liles"
published: '2026-07-24'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Policy Binder Didn't Change Anyone's Behavior

In 2020, only 8% of organizations rated their data governance program "highly successful." Not 8% of bad organizations. 8% of the ones that had formal programs, named stewards, and documented policies.

TDWI surveyed data professionals that year and found something more revealing than the headline number. The top two barriers to governance success weren't budget or technology. They were "convincing employees to adhere to governance policies" (46%) and "creating policies that are clear and usable" (43%). The frameworks were ready. The organizations weren't. More precisely: the organizations had the frameworks and still couldn't make them stick.

This is the governance gap that defined the 2019–2021 era, and it explains most of what happened in the years since.

The reference frameworks were mature. DAMA-DMBOK 2 had been out since 2017, defining eleven knowledge areas anchored by a central governance hub. The EDM Council's DCAM gave organizations a scoring model. TDWI had a maturity framework. The consulting industry had built entire practices around standing up data governance offices, appointing chief data officers, and producing policy documentation.

None of it solved the behavioral problem. Organizations had governance councils that met monthly. They had policies that nobody read. They had data quality standards that the engineering team had never seen. The gap between what was written and what was practiced was the entire problem.

I saw this pattern up close working with clients who had invested heavily in governance frameworks: detailed documentation of who owned what data, what the standards were, what the processes should look like. What they didn't have was any mechanism to make those policies real. When data engineers were building pipelines, the governance document was not in the room.

The downstream cost was measurable. Gartner pegged poor data quality at an average of $12.9 million per year for a typical organization, drawn from a 2020 survey of 154 data quality tool customers. Whether your number is higher or lower, the direction is unambiguous: the gap between governance policy and governance practice has a price.

## What Actually Went Wrong

The bolt-on architecture was the structural root of the problem. The dominant pattern in this era was governance-as-separate-product. You ran your data through Informatica or stored it in Snowflake or built pipelines in whatever your stack was, and then separately, you had a Collibra or Alation catalog where someone was supposed to document what existed. Two systems, two workflows, two sets of people who didn't necessarily talk to each other.

Catalog curation was a manual, human-effort activity. Which meant it depended on someone remembering to do it, having time to do it, and caring enough about the governance outcome to prioritize it over shipping features. Most organizations found that the last condition was rarely met.

This isn't a criticism of the people. It's a description of the incentive structure. An engineer who builds a pipeline and ships it to production has done their job. Documenting that pipeline in the governance catalog is extra work with no direct feedback loop: no automated check, no broken build, no audit trail that anyone is watching. The behavior that gets reinforced is the one that ships the feature.

The result: catalogs full of stale metadata, data dictionaries that described systems as they existed eighteen months ago, data stewards maintaining documentation that nobody was using to make decisions.

## The DHCS Wake-Up Call

California's Department of Healthcare Services had a vivid version of this problem when we partnered with them on their data platform modernization. DHCS's behavioral health data was fragmented across Excel spreadsheets, Microsoft Access databases, and a legacy Teradata warehouse that had accumulated a decade of undocumented assumptions. There was no shortage of governance intent. HIPAA compliance alone mandates formal data handling. But the reality was a patchwork of systems where data quality and timeliness were chronic problems.

The problem wasn't that DHCS lacked governance awareness. They operated in one of the most regulated data environments in the country. The problem was that governance had never been embedded in the places where data actually moved. The policy existed. The pipeline didn't know about it.

When we rebuilt their data platform on Databricks, governance wasn't a documentation exercise we added at the end. Data privacy controls, access management, and compliance requirements were engineered into the pipeline architecture from the start. Collibra wasn't deployed as a separate layer for someone to manually update; it was integrated into the data cataloging workflow so metadata traveled with the data.

That's the move. Governance as part of the engineering process, not adjacent to it.

## What This Sets Up

The 2019–2021 period established the size of the gap clearly enough that the industry had to respond. And it did, just not by writing better policy documents.

The response was architectural. Analysts, vendors, and practitioners started asking a different question: what if governance didn't require human effort to maintain? What if the policies ran automatically, at the point where data moved, embedded in the systems engineers were already using?

That question is what drove the next five years. Active metadata, data contracts, platform-native governance, observability tooling: all of it is an attempt to answer the behavioral problem with a mechanical solution. Make compliance the default. Make violation detectable. Make the policy part of the build.

The 8% number is a useful benchmark. It tells you what governance looked like when the primary implementation mechanism was a policy document. What comes next is what happens when governance becomes code.

---

*Sources: TDWI Modern Data Governance (Philip Russom, Ph.D., December 18, 2020); Gartner Magic Quadrant for Data Quality Solutions (July 27, 2020; Melody Chien & Ankush Jain); Gartner "How to Improve Your Data Quality" (July 14, 2021); Improving/DHCS Data Platform case study.*
