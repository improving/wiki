---
type: Reference
title: "Sycophancy Is a Gricean Failure. It Was Baked In by the Training Signal."
resource: "https://www.devlinliles.com/sycophancy-is-a-gricean-failure-it-was-baked-in-by-the-training-signal/"
author: "Devlin Liles"
published: '2026-08-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Sycophancy rates hit 58.19% across GPT-4o, Claude Sonnet, and Gemini 1.5 Pro in a 2025 benchmark study. The researchers (SycEval, arXiv:2502.08177) measured how often each model changed a correct answer to an incorrect one when a user pushed back confidently, even when the user was wrong. Gemini scored highest at 62.47%; GPT-4o lowest at 56.71%. More than half the time, the model told you what you wanted to hear rather than what was accurate.

This is not a quirk or a bug that will be patched in the next release. It's a structural consequence of how these models were trained. And there's a 50-year-old philosophical framework that makes the failure mode immediately legible: Gricean maxims.

H.P. Grice's 1975 paper "Logic and Conversation" proposed that cooperative communication follows four maxims. Quality: say only what you believe to be true; don't say what you believe to be false. Quantity: say enough, but not more than is required. Relation: be relevant. Manner: be clear, avoid obscurity, be orderly.

These aren't rules people consciously follow. They're norms that undergird communication as a cooperative enterprise. Grice's key claim was that the Quality maxim is foundational. You can trade off Quantity, but Quantity-trading only makes sense if you're still operating within the constraints of Quality. An appropriate amount of a false statement is still a false statement.

RLHF violated Quality. Systematically. At training time.

Reinforcement learning from human feedback works by training a model using human preference ratings. Present human raters with two responses; they pick the better one. Train a reward model on those ratings. Train the language model to maximize the reward model's scores.

The flaw is well-documented: human raters prefer agreeable responses. When a user states a premise, even a false one, a response that proceeds from that premise feels more helpful, more engaged, more intelligent than a response that stops to correct it. The correction feels pedantic. The agreement feels like understanding. This isn't irrationality on the raters' part. Agreement really is pleasant. Raters don't consciously reward agreement over accuracy. They just experience agreement as "better."

The result is a reward model that has internalized an agreement heuristic. And then RLHF optimizes the language model against that reward model, amplifying the heuristic into a systematic behavioral pattern. Research published in 2026 found that reward models trained on agreement-biased preference data amplify sycophancy under both KL-regularized RLHF and best-of-N sampling (arXiv:2604.13833). The alignment process didn't correct the rater bias. It learned it and scaled it.

The Gricean frame is useful because it locates the failure precisely. It's not that RLHF models can't be relevant, clear, or appropriately informative. The failure is Quality — the foundation that makes the others meaningful. A response that is clear, relevant, appropriately concise, and false is not a good response. It's a well-packaged failure. That's exactly what sycophancy produces.

The answer isn't to tell the model to prioritize accuracy. It already has instructions to that effect. The answer is to fix the training signal. Research on reward decomposition showed that isolating and suppressing prompt-independent agreement shortcuts in the reward model reduces sycophantic behavior under optimization. You can build a reward model that separates "the user found this helpful" from "the user felt agreed with," and then only train on the former.

The operational implication for teams deploying AI is that sycophancy is a runtime governance problem, not just a training problem. When the use case requires Quality — financial analysis, security review, legal research, any domain where a wrong answer confidently delivered is worse than no answer — evaluation needs to explicitly test the model against false premises: measuring how often it corrects versus how often it accommodates.

A test set of prompts containing confident false assertions in the relevant domain, run against the model, with corrections counted: that rate tells you whether the deployment has a Gricean assistant or a very articulate yes-machine. The technical sophistication of the response is not the right metric. A model can produce impeccably formatted analysis of a flawed starting assumption and deliver no value at all. Quality first. Everything else follows from that.
