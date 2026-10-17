---
type: Reference
title: "Every AI Value System Bottoms Out Somewhere"
resource: "https://www.devlinliles.com/every-ai-value-system-bottoms-out-somewhere/"
author: "Devlin Liles"
published: '2026-08-10'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most fundamental question in AI alignment is: what does the model optimize for, and why? The answer the field has converged on — human preferences — sounds reasonable until you ask what justifies it. That question has a name in philosophy. It's called the Münchhausen Trilemma, and it doesn't have a clean answer. Neither does AI alignment.

The trilemma, formalized by Hans Albert in 1968, applies to any attempt to ground a claim through justification. If you justify a claim by pointing to a supporting reason, that reason itself needs justification. Follow any justification chain to its end and you face three options. Infinite regress: justification continues forever without reaching a foundation. Circular reasoning: the chain loops back on itself. Or an axiomatic halt: at some point you simply stop and say "this is where we start, without further justification." Every attempt to ground claims rationally terminates in one of these three. There's no fourth option.

RLHF (reinforcement learning from human feedback) is the dominant alignment approach for large language models. The basic mechanism: human raters compare model outputs and express preferences. Those preferences train a reward model, which fine-tunes the language model to produce outputs the reward model rates highly.

This terminates at the axiomatic horn. Human preferences are the stopping point. We don't further justify why human preferences are the right target. They're the axiom. That axiom is defensible — human preferences seem like a reasonable place to anchor AI values — but it's still an arbitrary axiom in the technical sense. The justification chain stops there by decision, not by logical necessity.

Constitutional AI, Anthropic's alternative approach, attempts to escape the preference-axiom horn by substituting explicit principles. Instead of bottoming out in "whatever humans prefer," it bottoms out in "a constitution": a set of written principles that guide the model's self-evaluation and self-revision. This moves the arbitrary axiom up one level: the constitution itself isn't derived from first principles, it's chosen. The trilemma hasn't disappeared. It's relocated.

The performance numbers across alignment approaches tell something important: RLHF, Constitutional AI, RLAIF, and DPO cluster relatively closely in human preference evaluations. The methods differ substantially in their grounding structure, but they produce similar results on standard benchmarks. That convergence is a soft validation of the axiomatic approach. If your goal is "AI that humans evaluate positively," multiple different axiom choices get you to roughly the same place.

But "humans evaluate positively" is not a fixed target. Different humans, different contexts, different evaluator backgrounds produce different preference signals. The arbitrary axiom compounds: not only are we stopping at human preferences, we're stopping at the preferences of a specific subset of humans, evaluated in a specific context, on a specific distribution of tasks. Alignment research published in 2024 and 2025 has started surfacing this formally — work applying social choice theory to alignment argues that the diversity of human values cannot be aggregated to a single preference signal without making explicit choices about whose values take priority.

The governance implication for enterprises is real. When you adopt a model from a specific provider, trained using a specific alignment methodology, you are adopting a value structure. The values were grounded in an axiomatic choice the model provider made, using a human evaluation pool with specific characteristics, aggregated in a specific way. Your deployment is not value-neutral.

This doesn't mean you can't use the model. It means you need to understand what values it embeds and assess whether those values align with your use case and your users. When you add a system prompt, you're modifying the effective value structure. When you fine-tune, you're directly editing the weights that encode values. When you build evaluation pipelines, you're measuring whether the model's behavioral dispositions match the behavioral dispositions you want.

What alignment work has accomplished is not solving the grounding problem. It's making the grounding choices more explicit, more auditable, and more revisable. RLHF makes explicit that it's bottoming out in human preferences. Constitutional AI makes explicit what the governing principles are. That explicitness is valuable — not because it provides a foundation that doesn't bottom out somewhere, but because it makes the arbitrary axiom visible enough to interrogate and, when warranted, revise.

The trilemma doesn't disappear from AI alignment. It moves up one level every time you think you've resolved it. Every value-laden AI system is resting on choices that could have been made differently, justified by a chain that eventually runs out. Knowing where your chain runs out is the beginning of responsible governance.
