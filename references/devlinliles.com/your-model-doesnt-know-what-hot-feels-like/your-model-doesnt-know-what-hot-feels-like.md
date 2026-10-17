---
type: Reference
title: "Your Model Doesn&#x27;t Know What &#x27;Hot&#x27; Feels Like"
resource: "https://www.devlinliles.com/your-model-doesnt-know-what-hot-feels-like/"
author: "Devlin Liles"
published: '2026-08-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

When a language model generates the word "hot," it has no access to heat. It has access to the statistical neighborhood of the token "hot": every context in which that word appeared across its training corpus. The word and the sensation are not connected. They never were.

This is the symbol grounding problem, formulated by cognitive scientist Stevan Harnad in 1990. Symbols (words, tokens, representations) need to be grounded in something outside themselves to carry meaning. For humans, that grounding happens through sensorimotor experience. You know what "hot" means because you've touched hot things, pulled your hand back, felt the sensation. The word is anchored to a physical reality. For a language model, the token exists in a self-referential web of other tokens. Meaning is relational, not perceptual. The system is a dictionary defining words with other words, all the way down.

Harnad called this the symbol grounding problem. Researchers have started calling the LLM version the vector grounding problem, because the units aren't classical symbols — they're high-dimensional vectors. The substrate is different. The problem is structurally the same.

Grounded representations behave differently under pressure. When you know what "hot" means from physical experience, you can handle novel combinations like "hot silence," "a hot negotiation," or "hot with embarrassment," because you're applying a concept with real-world anchoring, extended by analogy. A model handling those same phrases is doing something different: it's interpolating from co-occurrence patterns in text. Most of the time, that interpolation is good enough to seem identical. In edge cases and novel configurations, it isn't.

The practical gap shows up in sensory and causal language. A perspective in Frontiers in Systems Neuroscience examining whether multimodal LLMs can achieve deep world understanding found that vision-language models pick up on pictorial features but diverge from human grounding on how objects can be physically manipulated or used. That's grounding failure. The model has learned to associate visual features with labels without building the kind of grounded concept that supports reliable generalization.

Multimodal training is the most commercially scaled attempt to ground tokens in perceptual experience. Connect images to text, connect audio to text, connect video to text. Each modality adds a dimension of perceptual grounding that pure language training lacks. The improvement in sensory and spatial reasoning tasks is measurable. But the ceiling doesn't approach human grounding. Some work argues that LLMs may circumvent the symbol grounding problem through a different mechanism: not grounding in world experience but by exploiting pre-grounded human content already encoded in the training corpus. That's an interesting theoretical claim. It doesn't change the practical reliability picture.

The grounding gap shows up most sharply in three deployment contexts. Physical-world reasoning is the highest-risk category. Any task that requires the model to reason about how things behave in space — structural engineering, supply chain logistics, materials selection, safety analysis — puts the model in the domain where its grounding is weakest. Useful output is possible, but the validation layer has to be staffed by people who have the sensorimotor grounding the model lacks.

Sensory and experiential data is the subtler one. Customer sentiment, user experience research, ergonomics, physical product design: these domains have a perceptual component that text-based models handle through proxy patterns. The model learns that users who say X tend to also say Y, and Y is associated with dissatisfaction. That's a useful signal. It's not the same as understanding the user experience, and the gaps show up when AI-assisted UX research consistently misses problems that only emerge in physical use.

Novel domain transfer is where the absence of grounding is hardest to predict in advance. Grounded concepts generalize through analogy to physical reality. Statistically approximated concepts generalize through pattern similarity. Those produce different results at the edges, and the edges are exactly where the interesting problems live.

The response isn't to avoid these contexts entirely. It's to staff the validation layer correctly. Humans with genuine domain grounding — physicists, clinicians, operators, craftspeople — reviewing outputs in the domains where the model's token-level approximations are most likely to drift from physical reality. This isn't a technology limitation waiting for a model update to fix. It's a structural feature of how language models are built, and the architecture needs to account for it.

Harnad's problem hasn't been solved. In some formulations it may not be solvable with the current approach. What's been built is a set of increasingly sophisticated partial workarounds. Understanding which workaround is in use, and what it still misses, is the competence that separates teams that deploy AI reliably from teams that are surprised by the failures.
