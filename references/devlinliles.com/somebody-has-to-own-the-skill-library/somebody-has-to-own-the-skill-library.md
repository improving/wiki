---
type: Reference
title: "Somebody Has to Own the Skill Library"
resource: "https://www.devlinliles.com/somebody-has-to-own-the-skill-library/"
author: "Devlin Liles"
published: '2026-09-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Gartner projects that 40% of enterprise applications will embed task-specific AI agents by the end of 2026, up from under 5% a year earlier. Most of the organizations already in that number are sitting at what the Cloud Security Alliance describes as level 100 to 200: agents genuinely in production, doing real work, with minimal controls and governance that's informal at best. The gap isn't adoption. Adoption is running ahead of everything else. The gap is that nobody has been assigned the job of deciding who gets to publish a skill, who reviews it, and who has the authority to pull one that's causing problems.

That's an ownership question before it's a tooling question, and it's the exact question this series raised two pieces back at the retrieval and governance level: an operating model isn't a single governance philosophy stamped uniformly across an organization. It's a stage-by-stage answer to who decides, applied consistently at each stage rather than centralized or federated by default because one of those is easier to put on a slide. Skill libraries need the identical discipline, applied to a narrower set of stages: who can author a skill, who reviews it, who owns it once it's live, and who has standing to deprecate it.

## Three shapes, and why picking one uniformly is the mistake

A centralized model routes every skill through one team, typically the same group running an AI center of excellence, before anything reaches production. That earns its overhead exactly where the Cloud Security Alliance's research says the risk concentrates: skills touching regulated data, financial transactions, or anything with organization-wide blast radius if it goes wrong. A federated model lets domain experts, finance, legal, recruiting, author skills for their own function without routing through a central bottleneck. Anthropic's own product data points at why this matters in practice: the skills getting the most attention internally are increasingly being built by people who aren't engineers at all, domain experts in finance, recruiting, accounting, and legal, who understand a workflow's actual shape better than a platform team ever will secondhand.

Picking one of these models uniformly recreates a failure this series has already named twice. Centralize everything, and the domain expert who best understands how the recruiting team actually screens candidates has to convince a platform team of something they already know, which slows the exact skills that carry the least organization-wide risk. Federate everything, and a skill with reach into regulated financial data ships with no more scrutiny than a formatting helper, because nobody assigned differentiated review to differentiated risk. The right answer, consistent with how this series has treated centralized-versus-federated decisions at every layer so far, is neither uniformly. It's hybrid: domain experts author, a platform team scopes and reviews, and the review's rigor scales with what the skill can touch, not with how the skill was categorized on day one.

Ninety-one percent of organizations have already deployed AI agents. Ten percent have a governance strategy covering them. That gap, documented by Obsidian Security's research on agentic deployment, is the same adoption-outrunning-governance pattern this series keeps running into, restated at the organizational level instead of the technical one. It isn't a sign that governance is hard to build. It's a sign that almost nobody has assigned the job yet.

## What the structure actually looks like

The Cloud Security Alliance's research on this gap converges on a specific shape worth naming directly: a cross-functional governance board with real authority to approve, pause, or reject a deployment, spanning product, legal, security, risk, and data operations, rather than a single owner trying to hold all of that judgment alone. Accountability splits along lines that mirror where the expertise actually sits. Data governance owns the policies for what a skill is allowed to reach. AI and platform teams own the evaluation pipeline that decides whether a skill is good enough to ship. Security and compliance own the audit trail proving the first two happened. Domain teams own whether the skill actually reflects how the work gets done, because that's the one piece of judgment no amount of centralized process can substitute for.

Anthropic's own rollout of enterprise plugin management, announced in February 2026, is a live instance of this structure rather than a theoretical one. Organization-wide provisioning lets an admin default-enable a skill across the company or scope it to a single role. Anthropic shipped its own stock plugins for finance, legal, and HR the same month, and the pattern underneath the feature is telling: an owner distributes plugins through a marketplace, employees can't edit what's centrally managed, and the marketplace itself is functioning as the governance layer, not a convenience feature bolted on next to one. Matt Piccolella, who works on the product, described the trajectory plainly: organizations building not dozens but hundreds or thousands of these, distributed internally the way departments distribute any other internal tool.

That's the goal state for the ownership question stated as plainly as it can be: a structure where authorship, review, and enforcement each sit with whoever is actually positioned to do that job well, connected by a shared registry that makes the division of labor visible. That registry eventually has to cover more than one organization's own skills. It has to reach skills and capabilities crossing organizational boundaries entirely, which is where this series lands next, and it's the same question the earlier retrieval pieces already answered for documents, arriving at the same conclusion from a different direction.

---

*Sources: Cloud Security Alliance, "The AI Agent Governance Gap: What CISOs Need Now" (2026); Obsidian Security, agentic AI deployment research (2026); IBM, "The 2026 Guide to AI Agents"; TechCrunch and Anthropic enterprise plugin announcements (February 2026); "What Is an AI Operating Model? How to Structure Your Enterprise for Scalable AI" (Devlin Liles, 2026).*
