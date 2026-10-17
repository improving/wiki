---
type: Reference
title: "The Compounding Tax: Why Small Model Errors Become Large System Failures"
resource: "https://www.devlinliles.com/the-compounding-tax-why-small-model-errors-become-large-system-failures/"
author: "Devlin Liles"
published: '2026-07-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A model that is right 99% of the time sounds like a solved problem. Run that same model across a hundred sequential steps and it succeeds end to end about 37% of the time. The error rate did not change. The horizon did. This is the compounding problem, and it is the single most underappreciated failure mode in the systems we are building on top of large models today.

The reason it gets missed is that we evaluate models the way we evaluate functions: one input, one output, one judgment of correctness. Most production deployments no longer work that way. We chain calls. We feed a model its own previous output. We let it take an action, observe the result, and decide the next action. The moment a model's output becomes its own future input, per-step accuracy stops being the metric that matters. Trajectory reliability does. And trajectory reliability degrades faster than almost anyone's intuition expects.

This piece is about why that happens, where it bites hardest, and what actually works to contain it.

## The arithmetic is unforgiving

Start with the cleanest version of the problem. Suppose each step in a process has an independent probability `p` of being correct, and the whole task only succeeds if every step is correct. The probability of an error-free run is `p^N` for `N` steps.

Plug in numbers and the curve is brutal. At `p = 0.99`, ten steps gives you 90% end-to-end reliability, fifty steps gives 61%, and a hundred steps drops you to 37%. Push per-step accuracy to a genuinely excellent 99.9% and a hundred steps still leaves you at 90%, while a thousand steps collapses back to 37%. The horizon eats your accuracy gains alive. Every order-of-magnitude improvement in per-step reliability buys you only one order of magnitude more horizon at the same end-to-end success rate.

The independence assumption is a simplification, and in practice it usually makes things worse rather than better. Errors in these systems are correlated. A model that misreads the task in step three tends to keep misreading it through steps four, five, and six. One confidently wrong premise poisons every inference downstream of it. So `p^N` is the optimistic bound. The realistic curve has fatter tails, because once a trajectory leaves the rails it rarely climbs back on by chance.

Two distinct mechanisms drive this, and they are worth separating because they call for different fixes.

## Mechanism one: autoregressive error accumulation

Generative models produce sequences one token at a time, and each token is conditioned on every token that came before it. During training the model is fed ground-truth prefixes. It learns to predict token `t+1` given a perfect, human-written sequence up to token `t`. During inference the model is fed its own generated prefix instead. It predicts token `t+1` given whatever it actually produced up to token `t`, mistakes included.

This gap between training conditions and inference conditions is exposure bias. The model was never trained on the distribution of slightly-wrong prefixes it generates at runtime, so each small deviation pushes the context a little further from anything it saw during training, which makes the next token a little more likely to deviate, which pushes the context further still. The technical name is distribution shift, and the felt experience is a model that starts coherent and slowly drifts: a summary that subtly changes the subject by paragraph four, a code generation that compiles at the top and hallucinates an API by the bottom, a chain of reasoning whose early arithmetic slip becomes the load-bearing assumption for everything after.

The insidious part is confidence. The model has no internal signal that says "I am now operating outside my training distribution." It generates the wrong continuation with exactly the same fluent certainty as the right one. Token-level probabilities are calibrated to the next token, not to whether the trajectory as a whole is still grounded in reality.

## Mechanism two: agentic loop drift

The second mechanism shows up in agents, the systems that plan, act, observe, and repeat. Here the feedback loop runs through the world itself, with every action altering the state the next decision depends on. The model decides on an action. The action changes some state: a file gets written, an API gets called, a row gets updated. The model observes the new state and decides the next action based on it.

When an action is slightly wrong, the agent does not just record a wrong token. It mutates the environment into a state that no longer matches the agent's mental model of where it is. Now every subsequent decision is made against a corrupted picture. The agent that deleted the wrong file keeps reasoning as though the right file is gone. The agent that misparsed an API response builds its next three calls on a value that was never real. The state and the model's belief about the state diverge, and absent a correction mechanism, that divergence only grows.

Long-horizon agentic tasks combine both mechanisms. The token-level drift degrades the quality of each individual decision, and the action-level drift compounds those decisions into a world state that wanders progressively further from the goal. This is why agents can look spectacular in five-step demos and fall apart on fifty-step real work. The demo never ran long enough to pay the compounding tax.

## Why benchmarks hide it

Most evaluation hides compounding by construction. Single-turn benchmarks measure `p`, not `p^N`. A model that posts state-of-the-art numbers on isolated tasks tells you nothing reliable about how a fifty-step chain built from those tasks will behave, because the benchmark never multiplied the per-step rate across a horizon.

This produces a specific and recurring disappointment. A team prototypes an agent, sees it nail a handful of representative tasks, and ships it. In production the task distribution includes longer horizons, messier states, and inputs that sit slightly off the training distribution. The per-step accuracy that looked like 98% in the demo behaves like 94% in the wild, and at fifty steps the difference between those two numbers is the difference between a 36% and a 5% end-to-end success rate. The model did not regress. The horizon and the input distribution revealed a fragility the benchmark was structurally unable to show.

If you take one measurement discipline from this piece, make it this: evaluate on trajectories, not steps. Measure end-to-end task completion across the horizon lengths you actually run in production, and track how that number decays as the horizon grows. The decay curve is the real spec.

## What actually contains it

You cannot eliminate compounding. You can bend the curve, and the techniques that work all do one of three things: they raise per-step reliability, they shorten the effective horizon, or they inject correction so errors stop propagating. The strongest systems do all three.

**Shorten the horizon through decomposition.** A single hundred-step trajectory is fragile in a way that ten independent ten-step trajectories are not, because errors cannot propagate across a boundary the architecture refuses to let them cross. Break long tasks into subtasks with clean, verifiable interfaces between them. Each subtask starts from a known-good state rather than inheriting the accumulated drift of everything before it. This is the single highest-leverage move available, and it is mostly an architecture decision rather than a model decision.

**Ground every step against an external source of truth.** Retrieval-augmented generation, tool calls that return real data, and reads against the actual system state all serve the same purpose: they replace the model's drifting internal belief with a fresh observation from outside itself. An agent that re-reads the current file before deciding what to change to it cannot stay corrupted by a stale mental model for long. Grounding is how you stop the model from compounding its own fiction. The more often a trajectory touches ground truth, the shorter the window in which any single error can compound.

**Verify before you propagate.** Insert checks between steps so a wrong output gets caught before it becomes the next step's input. Verification takes many forms: a unit test the generated code must pass, a schema the output must validate against, a separate model asked to critique the first model's work, self-consistency across multiple samples where you keep the answer the majority agree on. The common principle is that catching an error at step three is cheap and catching it at step fifty is not, because by step fifty it has contaminated forty-seven downstream decisions. Verification converts silent compounding into a loud, local failure you can actually handle.

**Checkpoint so you can recover.** When a trajectory does derail, the cost of the failure depends entirely on whether you can roll back to a known-good state or have to start over. Persist intermediate state at meaningful boundaries. Make subtasks idempotent and re-runnable. Design actions so they can be undone. A system that checkpoints turns a catastrophic full-run failure into a cheap retry of a single segment.

**Constrain the output space.** The less freedom the model has to deviate, the less room error has to accumulate. Constrained decoding that forces valid JSON, grammars that restrict output to a legal structure, and tight tool schemas all narrow the space of possible mistakes. You are trading expressiveness for reliability, and on long horizons that is usually the right trade.

**Keep a human on the high-consequence steps.** Not every step deserves the same scrutiny, and not every step should be autonomous. Identify the decisions where an error is expensive or irreversible and route those through human review, while letting the cheap and reversible steps run unattended. The art is placing the human where the compounding curve is steepest and the blast radius is largest, rather than everywhere or nowhere.

**Instrument the trajectory.** You cannot manage what you cannot see. Log every step, every state transition, and every intermediate output, so that when a run fails you can find the step where it left the rails. Observability on trajectories is what turns "the agent sometimes does the wrong thing" into "the agent fails at the state-merge step 8% of the time, here is the pattern." The first is a vibe. The second is a fixable bug.

## The mental model worth keeping

Treat per-step accuracy as a budget you spend over a horizon, not a property you possess. The question is never "how accurate is the model." The question is "how long a chain can this model carry before the compounding tax bankrupts the result, and what is my horizon." Once you hold the problem that way, the design priorities reorganize themselves. You stop chasing marginal gains in single-step benchmark scores and start attacking horizon length, grounding frequency, and verification coverage, because those are the levers that move the curve you actually care about.

The systems that succeed with long-horizon model work are not the ones with the best model. They are the ones that engineered the compounding out: short subtasks, frequent grounding, verification between steps, cheap recovery, and humans placed exactly where the errors are most expensive. The model is one input to reliability. The architecture around it is the rest.
