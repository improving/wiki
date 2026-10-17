---
type: Reference
title: "LLMs Don&#x27;t Reason — They Hypothesize"
resource: "https://www.devlinliles.com/llms-dont-reason-they-hypothesize/"
author: "Devlin Liles"
published: '2026-07-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A language model that confidently gives a wrong answer isn't broken. It's doing exactly what it was built to do. That's the issue.

Charles Sanders Peirce, the American logician writing in the late 1800s, drew a clean line between three modes of inference. Deduction takes premises and derives necessary conclusions. Given all mammals have a spine, and a dog is a mammal, the dog has a spine. Induction accumulates instances into patterns: I've seen a thousand dogs with spines, so dogs probably have spines. Abduction works backward from observation to the most plausible explanation: there's a dog-sized hole in my fence and muddy paw prints in the yard, probably my dog got out. Abduction is the logic of hypotheses, not proofs.

LLMs are abduction engines. That sentence reframes a lot of confused thinking about these systems.

When a model generates a completion, it isn't executing a proof. It also wasn't trained through induction from labeled examples — that's a common misconception worth naming directly. LLMs learn via self-supervised next-token prediction on unlabeled text: no human-annotated categories, no labeled instances to generalize from, just unsupervised statistical pattern discovery applied at enormous scale across most of the written world. The training process doesn't map cleanly onto any of Peirce's three logics. What emerges at inference time does. When the model generates a completion, it's producing the most plausible continuation given the evidence in the context window plus everything compressed into its weights — inference to the best explanation. That's abduction. The result is a system that is often strikingly right, and wrong in a specific, structurally predictable way.

A hypothesis can be wrong while still being reasonable. You find muddy paw prints and conclude the dog escaped; it was actually your neighbor's dog. The abduction was valid given the evidence. The conclusion was wrong. This is exactly the character of LLM errors: not random noise, but confident, coherent, plausible-sounding completions that don't match reality. We call it hallucination. Peirce would call it a defeated hypothesis.

The research confirms this structure. Work benchmarking models on Peirce's three inference types consistently finds that GPT-4-class models perform substantially better on abductive tasks than on multi-hop deductive chains. Simple deduction scores well; chain deduction requiring five or more sequential steps degrades significantly; abductive explanation tasks recover to a middle range. They're better at "what's the most likely explanation?" than at "derive the necessary conclusion across five steps." The architecture favors abduction. The training amplifies it.

This has concrete implications for how we use these systems.

The first is about prompting. If the model is generating hypotheses, the best way to use it isn't as an oracle you consult once. It's as a hypothesis generator you triangulate. Ask for multiple competing explanations. Ask what would falsify each. Prompt for the evidence that would change the answer. This isn't a workaround; it's using abductive reasoning the way it's supposed to be used. Scientists don't take the first hypothesis and move on. They construct competing accounts and design tests.

The second is about verification architecture. If abduction is the inference mode, then deductive verification needs to be a separate step. LLMs will generate plausible answers to math problems. They will not reliably prove them. When the downstream stakes require proof rather than plausibility (a legal argument, a financial calculation, a security configuration), you need a verification layer that uses a different mechanism. Code execution, formal checkers, human review of the specific claim. You don't verify a hypothesis by asking the hypothesis-generator if it's right.

The third is about where these systems break. Multi-hop deduction, the kind that requires holding multiple premises in a chain and deriving their joint consequence, is structurally hard for systems built on abductive inference. This shows up as the model "losing the thread" in complex reasoning, contradicting itself across a long chain, or confidently asserting the wrong answer when the correct one requires five sequential steps. The failure isn't intelligence or effort. It's a paradigm mismatch: abduction isn't the right tool for deductive chains.

Peirce's three logics were never meant to be evaluated in isolation. Good reasoning requires all three, deployed at the right moment. The same is true of AI systems. The power of LLMs comes from their abductive capability: the speed with which they generate plausible, useful hypotheses across virtually any domain. The risk is in treating those hypotheses as proven conclusions.

The inference type a task actually requires determines whether a model is the right tool for it, and in what configuration. Abductive tasks (generating options, exploring scenarios, drafting explanations, surfacing plausible interpretations) sit squarely in the model's native mode. Tasks requiring inductive generalization over specific organizational data require training on that data. Tasks requiring deductive proof require verification in the pipeline. The model isn't making mistakes. It's answering a different question than the one it appears to be asked.
