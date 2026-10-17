---
type: Reference
title: "The Model Knows More Than It&#x27;s Telling You"
resource: "https://www.devlinliles.com/the-model-knows-more-than-its-telling-you/"
author: "Devlin Liles"
published: '2026-08-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most expensive misconception in enterprise AI is that model capability is fixed. You buy a model. You test it. It can do X and can't do Y. You build around that assessment and move on. What most teams miss is that the capability they measured is a function of how they asked, not just what the model knows.

Michael Polanyi introduced tacit knowledge in 1966 with a deceptively simple observation: "we can know more than we can tell." A master cyclist knows how to balance but cannot articulate the proprioceptive adjustments they're making. An experienced diagnostician knows what's wrong with a patient before they can explain the reasoning chain. A skilled craftsman recognizes quality in materials that they'd struggle to describe in words. The knowledge is real. It's operational. It just doesn't surface through explicit declaration.

This is not a quirk of human cognition. It's the structure of most deep competencies. The explicit, articulable layer of expertise is built on a much larger substrate of knowledge that resists verbalization. Polanyi's argument was that we systematically underestimate human competence because we only count what can be stated.

Large language models have tacit capabilities in exactly this sense. The knowledge is encoded in the weights — billions of parameters shaped by training on an enormous corpus — and much of it doesn't surface through simple prompting. Ask the model a direct question and you may get a mediocre answer. Walk the model through intermediate steps, show it an example, give it a problem structure to reason within, and the same model produces output that seems qualitatively different. The capability was there. The prompt elicited it.

The numbers are striking. In the original Wei et al. 2022 chain-of-thought paper, CoT prompting lifted PaLM 540B on GSM8K math word problems from 18% (standard prompting) to 57% — surpassing the prior state of the art set by a fine-tuned GPT-3 with a verifier. The model didn't learn anything new between the two evaluations. The right prompting structure surfaced capability that was always present but inert. The pattern holds across arithmetic, commonsense, and symbolic reasoning tasks.

"We didn't expect it to be able to do that" is one of the most common things researchers say about large models. We assumed the model couldn't do something, tested it with a simple prompt, found it couldn't, concluded we were right, and moved on. The capability was there the whole time, waiting for elicitation.

This has a concrete implication for how organizations procure and evaluate AI. Benchmark evaluations on standard tasks, with standard prompting, systematically underestimate model capability. They measure performance in the explicit layer: what the model can do when asked simply. They miss the tacit layer: what the model can do when asked well.

A prompt engineer with deep domain expertise and strong technique can extract qualitatively better performance from a model than a developer who treats prompting as a secondary concern. That's not a soft claim. It's the elicitation gap at work. The question "which model should we use?" is inseparable from "how well can we prompt it?"

This creates a strategic problem for enterprises that evaluate models as if capability is intrinsic. You run an evaluation on raw model performance, pick the model that scores highest, deploy it with whatever system prompt your team writes in an afternoon, and wonder why production outcomes don't match evaluation results. The model's tacit capability was measured in evaluation but never elicited in deployment.

The practical response is to treat prompt architecture as a first-class engineering concern, not documentation. In the same way that database query design extracts performance from hardware that's already present, prompt design extracts capability from a model that already has it. The craft is real. The expertise is transferable. The results are measurable.

Few-shot examples are particularly powerful elicitation tools. Showing a model two or three worked examples of the task you want, formatted the way you want the output and reasoned through the way you want the model to reason, activates capabilities that zero-shot prompts leave dormant. You're giving the model a structure to match. The tacit knowledge has a scaffold to organize itself around.

Chain-of-thought prompting works similarly. Asking the model to reason step-by-step before producing a final answer creates a surface on which the model's intermediate knowledge can externalize. What Polanyi called tacit knowledge becomes, at least partially, explicit through the articulation process. The model doesn't just know the answer. It describes how it got there, and the description turns out to be part of why it gets there correctly.

There's a governance angle here that matters for enterprise deployments. If capability is not fixed and elicitation is a skill, then capability assessments have a shelf life. A model that appeared to underperform on a task in October might be fully capable of that task by December, once your team has developed better prompting. Locking in architectural decisions based on early-stage capability assessments can box you into constraints that are purely artifacts of underdeveloped elicitation.

Polanyi's insight was that expertise has a depth most people never tap. The same is true of language models. The relevant question isn't only what they can do. It's what their deployers know how to ask them.
