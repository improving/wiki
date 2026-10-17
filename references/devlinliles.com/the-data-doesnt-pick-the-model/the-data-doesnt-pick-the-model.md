---
type: Reference
title: "The Data Doesn&#x27;t Pick the Model"
resource: "https://www.devlinliles.com/the-data-doesnt-pick-the-model/"
author: "Devlin Liles"
published: '2026-08-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Willard Van Orman Quine and Pierre Duhem arrived at the same uncomfortable conclusion from different directions: the empirical evidence underdetermines the theoretical choice. Multiple, mutually incompatible theories can fit the same set of observations equally well. The data doesn't tell you which theory is correct. You choose based on non-empirical criteria — simplicity, elegance, prior commitments, theoretical tradition — and then you build a world that validates your choice.

This is not a failure of science. It's a structural feature of how theory-building works. And it maps exactly onto one of the least-discussed problems in applied AI: the arbitrary assumptions baked into architectural choices that your training data can never adjudicate.

Start with the benchmark reality. A standard transformer, a sparse mixture-of-experts transformer, a state space model like Mamba, and a hybrid SSM-attention architecture can achieve comparable scores on standard benchmarks at equivalent parameter counts. The evaluation data doesn't strongly discriminate between them. You could train any of these on the same corpus and get roughly similar aggregate performance. If you were a Quinean empiricist about architecture selection, you'd say: the evidence doesn't pick a winner. The architectures are empirically equivalent, at least at the resolution benchmarks currently offer.

But architects pick anyway. They pick based on computational efficiency at inference time, theoretical priors about what attention mechanisms are actually doing, hardware characteristics of the deployment target, team expertise, and sometimes just the momentum of prior successful work. These are all legitimate reasons. The problem is that the non-empirical grounds of the choice bake in assumptions the training data can't correct.

Here's where the Quine-Duhem problem becomes concrete for practitioners. Every architectural decision is simultaneously an implicit claim about what matters. The transformer's attention mechanism assumes that the relevant structure in language is pairwise token relationships across arbitrary distances. The tokenizer choice assumes a particular granularity of linguistic unit. The context window size assumes something about how much history is relevant to any given prediction. The positional encoding scheme assumes something about the geometry of sequence information. None of these are assumptions the training data validates directly. They're prior theoretical commitments. The training process tunes the parameters within the architecture. It doesn't adjudicate whether the architecture's implicit assumptions are right.

This has two practical consequences that matter directly for organizations deploying AI.

The first is failure mode specificity. Because different architectures encode different assumptions, they fail differently. A model that assumes long-range pairwise attention captures certain dependencies well but pays a quadratic compute cost that limits context length. A state space model that assumes sequence structure is Markovian handles long documents cheaply but may miss non-local patterns that attention would catch. When your deployed model fails on a task that another architecture handles well, the root cause isn't the training data. It's the architectural assumption that the training data couldn't surface as wrong. This matters for debugging. If you're trying to understand why your model fails at certain document analysis tasks, the answer may not be in the training set or the fine-tuning. It may be in an assumption the architecture made before training began.

The second consequence is portability risk. Organizations that build workflows around a specific model often implicitly build around the architectural assumptions of that model. A document understanding pipeline tuned to a transformer's attention patterns may not translate cleanly to a state space model with different long-range dependency behavior. An agentic system optimized for a model with a specific context window assumption may behave differently when the architecture changes, even if aggregate benchmark scores are equivalent.

The Quine-Duhem problem also applies to training data itself. Multiple models trained on the same corpus make different predictions on distribution. They've converged on different regions of the hypothesis space that are each compatible with the training signal. The "best model" selected from this set is chosen on non-empirical grounds: inference cost, safety evaluations, human preference data, output formatting. All of these are legitimate selection criteria. But they're not empirical claims about which model learned the correct representation of the training data, because that question doesn't have a unique answer.

For enterprise buyers and deployers, the practical implication is this: the benchmark score tells you what the model can do on the evaluation tasks, not whether the model's underlying assumptions are well-matched to your problem domain. Evaluating a model for your use case requires constructing tasks that stress the specific assumptions your workflow depends on. Does the failure mode of this architecture align with your risk tolerance? Does the architecture's implicit context model match your document structure? Does the tokenizer handle your domain vocabulary appropriately? These questions don't appear on standard benchmarks. They appear when you build evaluation tasks that are specific enough to fail on assumptions, not just overall performance.

The data doesn't pick the model. You pick it. Knowing what you're actually choosing, and what non-empirical commitments come with that choice, is the beginning of making the decision well.
