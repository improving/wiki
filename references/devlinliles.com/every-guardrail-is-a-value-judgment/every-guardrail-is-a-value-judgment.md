---
type: Reference
title: "Every Guardrail Is a Value Judgment"
resource: "https://www.devlinliles.com/every-guardrail-is-a-value-judgment/"
author: "Devlin Liles"
published: '2026-08-06'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Someone decided you shouldn't be able to ask an AI system how certain household chemicals combine. Someone decided you should be able to ask about historical atrocities. Someone decided the line between those two sits where it does. These are philosophical decisions, specifically about epistemic paternalism, not engineering ones, and most organizations deploying AI haven't recognized them as such.

Epistemic paternalism is restricting someone's access to information or knowledge on the grounds that having it would harm them. The classic medical example: a doctor who withholds a terminal diagnosis to protect the patient's emotional wellbeing is being epistemically paternalistic. So is a platform that hides certain news stories to prevent distress. So is an AI system that refuses to discuss topics the developers decided were dangerous.

The philosophical problem with epistemic paternalism isn't that it's always wrong. It's that it's in direct tension with epistemic autonomy: the right of individuals to form their own beliefs based on their own access to information. Restricting information to protect people from themselves presupposes that you know better than they do what they should know. That presupposition is sometimes true and sometimes deeply presumptuous, and the line between the two is contested.

The core tradeoff is concrete. Moving from minimal to maximal guardrail restrictiveness buys more protection against harmful outputs but spends user epistemic autonomy. Neither extreme is defensible. A completely unrestricted system provides information that enables serious harm. A maximally restricted system is less useful than a library and treats every user as a potential bad actor. Every content policy sits somewhere on this curve, whether the people who designed it knew they were making a philosophical choice or not.

A November 2025 Springer Nature paper titled "AI deskilling is a structural problem" makes the stakes concrete. It introduces the concept of "capacity-hostile environments" to describe how AI systems that pre-filter information impede humans from developing the judgment they need to evaluate that information independently. Excessive restriction doesn't just fail to deliver information. It actively degrades users' capacity to reason independently. The protection creates the harm it was designed to prevent.

Scholarship on content moderation and AI governance identifies three recurring failure modes. Misplaced authority: the platform or system assumes epistemic authority it hasn't earned, reflecting the commercial priorities of a handful of developers rather than a principled assessment of harm. Bias amplification: the criteria for what's "harmful" encode the beliefs and sensitivities of the content policy authors, producing asymmetric restrictions across topics and communities. Autonomy harm: the aggregate effect of consistent restriction is a population less capable of forming independent views.

The practical implications for enterprise AI deployments are significant. Content policies that hold up require explicit philosophical justification for each category of restriction. "We won't discuss X because it's harmful" is a position statement dressed as a policy, not a real policy. The actual policy requires answering: harmful to whom, under what circumstances, compared to the harm of not having the information?

The right calibration question isn't "what's the safest default?" It's "what's the right tradeoff for this user population in this context?" A legal research tool deployed for attorneys should have different guardrails than a general-purpose assistant deployed for consumer support. "Maximize safety" treats the autonomy cost as zero. It isn't zero. Every restriction has a cost.

Guardrail decisions require review, not just initial configuration. Information environments change. What was harmful three years ago may be widely available and unremarkable today. A content policy that isn't reviewed annually is a policy calibrated for a world that no longer exists.

And guardrails require audit mechanisms. Organizations that have decided certain content is restricted need to know whether the restriction is holding in practice. An organization that built a content policy, deployed it, and never tested it is performing epistemic paternalism, not actually enforcing it. The difference matters when something goes wrong.

Mill wrote in On Liberty that the only legitimate reason to restrict individual action is to prevent harm to others. He meant physical and social harm. Epistemic paternalism extends this to informational harm: preventing people from knowing things that might lead them to harm themselves or others. The extension is philosophically contested. But the contest isn't going to be resolved before your next AI deployment.

Every guardrail is a tradeoff between protection and autonomy. Making that tradeoff deliberately, documenting it, calibrating it for the specific context, and reviewing it over time — that's what separates a content policy from a default someone else's engineers set and deployed.
