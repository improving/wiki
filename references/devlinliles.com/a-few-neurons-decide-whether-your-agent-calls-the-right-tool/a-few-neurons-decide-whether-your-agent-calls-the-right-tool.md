---
type: Reference
title: "A Few Neurons Decide Whether Your Agent Calls the Right Tool"
resource: "https://www.devlinliles.com/a-few-neurons-decide-whether-your-agent-calls-the-right-tool/"
author: "Devlin Liles"
published: '2026-09-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I have spent enough hours staring at agent traces to have a physical reaction to the phrase "let's add another eval." An agent calls a tool it doesn't need, skips one it does, or fills the arguments with something almost right. The fix everyone reaches for first is more scaffolding: a bigger eval harness, another few hundred test cases, a prompt rewritten for the fourth time to add "only call this tool when necessary." I have written that sentence into a system prompt myself, more than once, with the quiet hope that better phrasing would fix something structural, when all it does is nudge probabilities at the surface.

A recent interpretability paper went looking inside the model instead of around it. The researchers traced the specific decision of whether to call a tool, and which one, back to a narrow set of neurons carrying most of that decision: a small, locatable piece of the network doing the deciding, identified well enough to point at.

That is a different kind of claim than anything an eval harness or a prompt can address. An eval tells you the tool call was wrong after the fact. A prompt tries to bias the decision before it happens, through instructions the model may or may not weight heavily on a given pass. Neither one touches the part of the network actually making the call. Both are working on the outside of a problem the paper locates on the inside.

I think this is why prompt tweaks plateau the way they do. If the circuit responsible for tool selection is intact, a clearer instruction helps, because there is something underneath capable of using it. If that circuit is thin or miscalibrated for a particular tool or argument pattern, no phrasing reaches it. I was rewriting the sentence outside the room where the decision actually got made.

That reframes what a chunk of agent failure actually is. A representational limitation, sitting in specific weights, that behaves the same way no matter how many test cases you throw at it, because the test cases were never the thing doing the deciding.

If this holds up outside one paper's benchmark, the lever for a real share of tool-calling failure sits inside the model. That points toward targeted fine-tuning on the specific circuit, activation steering at inference time, or choosing a base model partly on this property, ahead of another round of prompt iteration.

None of that is available yet to most teams building agents on top of someone else's model. Fine-tuning at the level of a single circuit still lives in research labs, and activation steering is further still from anything an API exposes. Teams keep reaching for evals and prompts because those are the only levers within reach, even after learning that a meaningful share of the failure sits somewhere those levers cannot go.

The eval harness still earns its keep. It catches the failures a clearer prompt can actually fix, and it tells you which ones are left over. What it cannot do is pretend the leftover pile is a coverage problem, when a few neurons already decided the answer before your prompt ever got read.
