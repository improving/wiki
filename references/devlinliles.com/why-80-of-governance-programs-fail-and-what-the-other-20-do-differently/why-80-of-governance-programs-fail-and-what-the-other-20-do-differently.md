---
type: Reference
title: "Why 80% of Governance Programs Fail (And What the Other 20% Do Differently)"
resource: "https://www.devlinliles.com/why-80-of-governance-programs-fail-and-what-the-other-20-do-differently/"
author: "Devlin Liles"
published: '2026-08-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Gartner's prediction from February 2024 is the one that should be on the wall of every data leadership team: 80% of data and analytics governance initiatives will fail by 2027. The prediction comes from a specific analyst (Saul Judah, VP Analyst at Gartner), and the diagnosis is more important than the number.

Programs fail, Judah says, "due to a lack of a real or manufactured crisis." The root cause is governance run as "data hygiene and control" rather than tied to business outcomes. The prescription: "CDAOs should stop taking a center-out, command-and-control approach to D&A governance, and instead, rescope their governance to target tangible business outcomes."

That is a precise diagnosis, and it maps directly to the patterns we see in organizations that have invested in governance programs that aren't producing returns.

## The Three Failure Patterns

The first is the compliance trap. The governance program was stood up because of a regulatory requirement or an audit finding. The implicit framing becomes: governance is what keeps us out of trouble. Teams experience it as friction. The program generates documentation, policies, and committee structures that consume resources without producing capability. When the audit passes, momentum dies.

This isn't cynicism about compliance. Compliance requirements are legitimate forcing functions, the "manufactured crisis" Gartner references. The trap is treating compliance as the endpoint rather than the starting point. A governance program that exists to satisfy an auditor will never invest in the operational capabilities that make data actually trustworthy and useful. It stops at documentation.

The second is the accountability gap. Governance structures exist on paper that cannot compel action. There's a Data Governance Council that meets monthly. There are data stewards assigned to domains. There is a policy manual. But when a data quality incident occurs, there's no enforcement path. The steward can flag it. The council can discuss it. Nobody has the authority to require the engineering team to fix it in a defined timeframe or face a defined consequence.

This is the governance equivalent of a code review process where the reviewer can leave comments but the author decides whether to implement any of them. The ceremony exists. The accountability doesn't.

The third is the tool-first failure. The organization invests in a catalog, an observability platform, or a metadata management suite without the organizational infrastructure to use it effectively. The catalog gets deployed. Nobody is assigned to curate it. The observability alerts fire and route to a shared inbox that nobody monitors. The tool is live. The capability is not.

## What the Wavestone Data Actually Shows

The Wavestone/NewVantage surveys of Fortune 1000 data and AI leaders are some of the most honest benchmarks in the field. Their 2024 edition has several numbers worth sitting with.

Only 42.3% of organizations have well-established data and AI ethics policies, and that number has been essentially flat across three consecutive surveys. Not declining, but not improving. The organizations that don't have these policies aren't getting closer to having them.

Only 15.9% of survey respondents believe their sector is doing enough on data and AI ethics. This is industry insiders assessing their own sector. The 42.3% who have policies apparently don't believe the policies are sufficient.

The 2024 survey also recorded that the share of organizations claiming to have "created a data-driven organization" roughly doubled to approximately 43%, compared to figures in the low-to-mid twenties in prior years. The researchers attributed this to GenAI's catalyzing effect: AI urgency drove data infrastructure investment that the data quality case alone hadn't motivated.

That last finding is the manufactured crisis Gartner references. AI created pressure to fix data problems that governance programs had been trying and failing to fix for years. The crisis worked. The data governance investment followed the AI investment.

## What the Successful Programs Have in Common

The pattern among the organizations that have built durable governance programs isn't unique tooling or framework selection. It's three things.

They picked a specific outcome first. Not "improve data governance" but "reduce the time from data availability to decision in our monthly financial close by 40%" or "eliminate the regulatory reporting errors that cost us $X per quarter in remediation." When the program has a number attached to a business outcome, two things happen: the business sponsor stays engaged, and the program team knows what to optimize for. Governance that can't name its business case will be deprioritized the next time budgets get tight, which is always.

They embedded governance into existing engineering workflows rather than building separate governance workflows. The teams that made this work did it by treating governance controls as engineering deliverables: data contracts go into the same PRs as the pipeline code, Unity Catalog access controls are part of the infrastructure-as-code, observability thresholds are part of the data product specification. When governance is done inside the engineering process, it gets done at engineering cadence. When it's done separately, it gets done when someone has time, which is always later.

They established clear ownership with real consequences. Not "assigned to a steward" but "this domain's data products are the engineering responsibility of this team, with the same SLA expectations we have for production services." Meaning: when a data quality incident occurs, there's an on-call rotation. There's a mean time to resolution target. There's a postmortem process. The governance commitment is operationalized, not aspirational.

## The Improving Pattern

Across our data platform engagements, the work that sticks has these properties. At BCBSM, every governance artifact (the risk assessment framework, the AI governance intake process, the HIPAA enablement procedure) was built alongside the platform, not after it. The governance process wasn't retrofitted onto an existing capability. It was designed as part of the capability from the start.

At DHCS, the business outcome was specific: the Behavioral Health Transformation program needed to be able to track health outcomes across California's mental health services. That outcome gave the platform work a direction. Data governance choices (Collibra integration, access controls, data quality standards) were evaluated against whether they advanced that outcome, not against whether they satisfied an abstract governance checklist.

At Ascend, ownership came first. Before any platform work started, there was a conversation about which data was whose, who was accountable for its quality, and what the expectations were. The technical work encoded those decisions into the platform architecture. The governance didn't follow the technology. The technology encoded the governance.

The 80% failure number is real. The diagnosis is accurate. The remedy is not a new tool or a better framework. It's a different conversation: start with the business outcome, build ownership into the structure, and make compliance the default rather than the exception. That's the program design that makes governance work.

---

*Sources: Gartner press release "Gartner Predicts 80% of D&A Governance Initiatives Will Fail by 2027" (February 28, 2024; Saul Judah, VP Analyst); Wavestone/NewVantage Data & AI Leadership Executive Survey 2024 (Randy Bean & Thomas H. Davenport, ~100+ Fortune 1000 leaders, published January 2, 2024); Collibra/IDC Data Intelligence Index (>1,200 senior professionals, August 2022); Improving/BCBSM, DHCS, and Ascend case studies.*
