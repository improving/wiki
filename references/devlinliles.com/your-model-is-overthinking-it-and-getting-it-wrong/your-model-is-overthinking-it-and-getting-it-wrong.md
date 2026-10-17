---
type: Reference
title: "Your Model Is Overthinking It — And Getting It Wrong"
resource: "https://www.devlinliles.com/your-model-is-overthinking-it-and-getting-it-wrong/"
author: "Devlin Liles"
published: '2026-08-04'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

More reasoning tokens do not produce more correct answers. That sentence makes executives uncomfortable, because they've been sold on "extended thinking" as a premium capability that justifies premium pricing. The discomfort is worth sitting with.

In 1974, Daniel Kahneman and Amos Tversky published their work on cognitive heuristics and biases, which eventually became the dual-process theory formalized in Kahneman's *Thinking, Fast and Slow*. The core idea: humans have two cognitive systems. System 1 is fast, automatic, low-effort. It pattern-matches and produces an answer before you've consciously decided to think. System 2 is slow, deliberate, resource-expensive. It's what you engage when you're doing long division, diagnosing a complex system failure, or writing a contract. System 1 handles most of daily life. System 2 handles hard problems. The key insight is that System 2 doesn't override System 1 by default. It has to be deliberately invoked, and it costs something to run.

Standard LLM token generation is System 1. A single forward pass through the network, conditioned on everything in context, producing the highest-probability next token. It's extraordinarily fast, extraordinarily cheap, and extraordinarily good at pattern-matched tasks.

Extended thinking (chain-of-thought, scratchpad reasoning, explicit "think step by step" prompting) is the model's approximation of System 2. It generates intermediate reasoning tokens before producing a final answer. Tokens cost money and add latency. The promise is that the intermediate reasoning produces better answers on hard problems. That promise is partially true, and the partial truth is the trap.

Multiple papers published in 2025 and 2026 found something Kahneman would have recognized immediately: wrong answers in extended thinking modes consistently accumulate more reasoning tokens than correct ones. One study on challenging benchmarks (AIME, HMMT, GPQA) found incorrect outputs averaged roughly 27,700 tokens versus substantially fewer for correct outputs. The model that gets the answer right tends to find its footing quickly. The model that gets it wrong keeps going, generating more tokens in what the paper's authors called "overthinking" — a term that maps precisely to the human experience of ruminating in circles when genuinely lost. (See: "Think Deep, Not Just Long," arXiv:2602.13517; "When More Thinking Hurts," arXiv:2604.10739.)

The accuracy curve peaks and then declines. There's an optimal thinking length for any given problem, and it scales roughly with problem difficulty. Past that peak, additional reasoning tokens don't improve the answer. They indicate the model has lost the thread. The cost curve, meanwhile, grows without bound.

I see this in production constantly. An organization enables extended thinking across every API call because it "should make things better." Latency triples, inference costs double, and accuracy on simple tasks actually degrades because the model second-guesses high-confidence completions it would have gotten right with a single pass. They've turned System 2 on for tasks that needed System 1.

Kahneman's framework gives you the right mental model for fixing this. System 2 should be invoked selectively, on genuinely hard tasks where sequential deliberation adds value. For LLMs, that means task routing. Classify your requests by complexity before you route them to a reasoning model with extended thinking enabled. High-frequency, low-complexity tasks belong on fast, cheap inference with no chain-of-thought. Multi-step analysis, evaluation tasks, and tasks where error is expensive are where reasoning mode earns its cost.

The evaluation question that matters isn't "did we turn on extended thinking?" It's "for which tasks does extended thinking improve the measured outcome, and by how much?" That's an empirical question that requires evals — testing the reasoning path against the direct path and measuring accuracy per token spent.

One more thing Kahneman would add: humans are bad at knowing when to invoke System 2. We use it when we're anxious, not when the problem actually requires it. Models have the same failure mode, encoded differently. The model that overthinks wrong answers is responding to difficulty signals that don't always correlate with correct-answer difficulty. It fires System 2 when it's confused, not necessarily when confusion is warranted.

A model that's thinking hard and taking a long time is not necessarily thinking well. It might just be lost. Treating longer reasoning chains as a proxy for quality is exactly the kind of System 1 shortcut that gets humans into trouble. The same shortcut, applied to AI deployment, scales the mistake.
