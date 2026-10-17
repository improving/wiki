---
type: Reference
title: "Software Craftsmanship Is Not a Job Title"
resource: "https://www.devlinliles.com/software-craftsmanship-is-not-a-job-title/"
author: "Devlin Liles"
published: '2026-07-11'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I have been asking the same question since 2013: *What does it mean to be a Software Craftsman? What do they do? How is that different?*

Most people answer with a list of tools. They name their testing framework, their CI pipeline, their linter configuration. Those are fine answers to a different question. A craftsman is defined by the standards they refuse to abandon.

The word carries more history than the software industry usually remembers. Medieval guilds certified a craftsman by the masterpiece, the proof that a journeyman could be trusted with work no one would inspect. Richard Sennett, in "The Craftsman," defines craftsmanship as the desire to do a job well for its own sake, an impulse older than any profession. The Software Craftsmanship Manifesto of 2009 imported that tradition into our field, and the import worked because the problem it addresses, quality under pressure, never went away.

## The Moral Dimension of Technical Standards

Professional integrity is not a soft skill. It is the foundation of every technical decision you make.

When you know that a module should have tests and you ship it without them because the deadline moved, you have made a moral choice. You chose to deliver something you know is below your standard, and you called it pragmatism to make the choice feel neutral. It is not neutral. It has a cost, and that cost compounds.

The frame I have used since 2013 is simple: *Be professional and unflinching. Have a minimum level of quality that is acceptable. Be prepared to say no to people who can fire you.*

That last sentence is the hard part. It is easy to have standards when no one is pushing on them. The craftsman's commitment is tested precisely when someone with authority tells you that standards are negotiable this sprint. The answer is still no. Robert Martin devoted a full chapter of "The Clean Coder" to the professional's no, and the older professions are built on the same refusal: a structural engineer who signs off on a beam they know is undersized has stopped being an engineer, whatever their title says.

## Identity Before Resume

I introduce myself in the same order I have used since 2013: Christian, Husband, Father, Developer, Passionate Geek.

The professional credentials come last. The ordering is deliberate, a statement about what I believe makes someone good at this work.

A developer who is defined by their craft, who builds things because they care about the quality of what they build, behaves differently than a developer who is defined by their job title. The craftsman asks "is this right?" before asking "is this done?" Those are different questions, and teams that get the order right produce different outcomes.

This is what I mean when I say craftsmanship is an identity. You do not become a craftsman by being hired as a senior developer. You become one by choosing, repeatedly and under pressure, to hold to your standards.

## Friends Don't Let Friends Skip the Basics

A frame from 2013 that still makes me smile: *friends don't let friends code without tests. Friends don't let friends code without requirements. Friends don't let friends code without acceptance criteria.*

The joke lands because everyone already knows they should write tests. The peer-responsibility framing changes the dynamic. When you watch a colleague cut corners, you have a choice: say something or let it slide. The craftsman's position is that letting it slide is a failure of professional friendship, on top of being a lapse of personal discipline.

This is a design for team culture. A team where people call each other out, with care and without contempt, on quality shortcuts builds a different kind of accountability than a team where each person manages their own standards in isolation. The former is a culture of craftsmanship. The latter is a collection of individuals who happen to share a codebase.

## Automation Is Craft, Not Convenience

One more commitment from 2013 that still shapes everything I do: automation is a professional obligation.

"Deploy Early, Deploy Often, then Deploy some more. When you are done with that, use Robots to Deploy for you while you sleep."

A craftsman who manually builds and deploys their software, when the tools to automate that process exist, is choosing to spend skilled human attention on work that machines do better. That is waste that happens to be done well.

The craftsman's obligation to automation is the same as their obligation to tests. The question was never whether there is time to set it up. Skipping it is a technical and professional failure. You build the automation, or you accumulate a debt that charges interest until you do.

## Where the Argument Could Break

The craftsmanship framing has earned real criticism, and two objections deserve answers.

The first arrived almost as soon as the manifesto did. Dan North argued in 2011 that programming is a means to customer outcomes, and that craft language risks turning developers into artisans admiring their own joinery while the user waits. The critique lands on the movement's worst behavior, the gatekeeping and the fetishized practices, and misses its core. The standards I am describing are economic, beyond any aesthetic preference: untested code and manual deployment pipelines produce slower delivery and higher defect rates for the customer. Craftsmanship done right is the customer's interest, held firmly on the days the customer cannot see far enough to hold it themselves.

The second objection says the say-no posture is a luxury, and that plenty of developers cannot afford to stand on principle with the person who controls their paycheck. True, and it is exactly why craftsmanship has to become a community norm and a team culture. A standard held by one developer is a career risk. A standard held by the whole team is just how the work gets done, and it is much harder to fire. The commitment is also a minimum, set where you can defend it and raised as your leverage grows.

## What This Has to Do with 2026

I am still writing about something I first argued in 2013 because everything I believe about AI adoption, organizational readiness, and the Intelligence Operating System is downstream of it. A team without professional standards will not build trustworthy autonomous systems. A culture that negotiates quality away under deadline pressure will not produce the governance infrastructure that agentic AI requires. The woodshop-to-factory transition I describe in the AI context is the same transition I was describing in 2013: from an environment where an individual's personal commitment to quality is the primary safeguard, to an environment where quality is encoded in the system.

The craftsman's question, *is this right?*, does not change when the tools do. It gets more important.
