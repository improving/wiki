---
type: Reference
title: "When Your Model Fails on New Data, That&#x27;s Hume&#x27;s Fault"
resource: "https://www.devlinliles.com/when-your-model-fails-on-new-data-thats-humes-fault/"
author: "Devlin Liles"
published: '2026-08-11'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most common explanation for AI failure in production is some version of "the model saw different data." That explanation is technically accurate and almost entirely useless, because it frames a structural problem as an operational one. You don't fix Hume's problem of induction by adding more training data.

David Hume posed the problem in 1748: why should patterns observed in the past hold in the future? We watch the sun rise every day for a thousand days and conclude it will rise tomorrow. But we have no logical justification for that conclusion. We've observed a correlation. We've inferred a law. The inference itself has no foundation in deductive logic. Every scientific generalization, every empirical prediction, rests on this unresolved gap.

Hume's answer was pragmatic: we can't justify induction logically, but we can't stop doing it. The mind is built to generalize. The question is not whether to generalize but how to fail gracefully when the generalization breaks.

Machine learning is industrial-scale induction. Training a model is the act of observing patterns in a finite dataset and learning weights that encode those patterns in a way that generalizes to unseen inputs. The entire enterprise rests on the assumption that the unseen data resembles the training data in the ways that matter. That assumption is called the i.i.d. assumption (independently and identically distributed). Training data and deployment data are assumed to be drawn from the same distribution.

They rarely are.

Research on out-of-distribution generalization shows the degradation pattern is steep and consistent. A model that performs well on its held-out test set — which was drawn from the same distribution as training — can lose 20 to 50 percentage points of accuracy when evaluated on data representing a moderate-to-large distribution shift. Under severe shifts, such as a change in domain, language, or jargon, performance can degrade abruptly. These aren't edge cases — they're the normal operating condition of AI deployed into a world that keeps changing.

The technical vocabulary for this is "out-of-distribution generalization." The philosophical vocabulary is "the problem of induction at scale." When a model was trained on enterprise support tickets from 2022 through 2024 and deployed in 2025, every new support ticket is an inductive leap. The model is betting that the patterns it learned from past tickets hold for future ones. That bet is usually pretty good. Until it isn't.

What makes it worse is that the failure is invisible until you measure it. A model doesn't know it's operating outside its training distribution. It generates tokens with the same surface confidence whether it's answering a question it's seen a thousand variants of or extrapolating wildly into new territory. The calibration problem amplifies this: the model's expressed certainty tells you nothing reliable about whether it's actually in-distribution.

The practitioners who handle this best are the ones who've absorbed the Humean lesson: don't ask "did the model learn correctly?" Ask "what's the distribution shift exposure in production, and how do I monitor it?"

In practice that means several things. First, your evaluation set should include data that you've specifically collected to probe distribution boundaries — the edge cases where your training data thins out, the topics your corpus underrepresents, the kinds of inputs that started appearing in production after training finished. Evaluating only on a held-out sample of your training distribution tells you how well the model learned the training distribution. It tells you almost nothing about how it will behave on real deployment traffic.

Second, drift monitoring is not optional. You need to track the statistical properties of your production inputs over time and alert when they diverge from your training distribution's characteristics. This is the observability layer for inductive risk. The sun has risen reliably, but you still want a weather forecast.

Third, and this is the one most organizations skip: you need a defined response to out-of-distribution detection. What happens when the monitor fires? Who reviews it? When does it trigger a retraining cycle versus a fallback to a human? The Humean answer to inductive uncertainty isn't paralysis. It's humble confidence with a circuit breaker.

There's a deeper implication for enterprise AI buyers that I want to make explicit. When a vendor shows you benchmark accuracy numbers, they are showing you in-distribution performance. They are showing you how well the model generalizes within the distribution it was trained and tested on. Those numbers say almost nothing about how the model will perform on your specific tasks, on your specific data, in your specific operational context.

The gap between vendor benchmarks and production performance is Hume's gap, made concrete. The responsible way to close it is evaluation on your real data before you commit, followed by continuous monitoring after you deploy. Buying on benchmarks and hoping for the best is trusting that the distribution of "AI benchmark problems" closely resembles the distribution of your actual business problems. That assumption is usually wrong.

Statistical learning theory has formal tools for quantifying inductive risk: PAC learning, VC dimension, generalization bounds. These frameworks can tell you, given a training set size and a model class, what the theoretical limit of generalization error looks like. They formalize the gap but don't close it. The Humean problem is still there underneath. All the math does is tell you how large the leap is.

The sun will probably rise tomorrow. Your model will probably handle tomorrow's inputs fine. Probably is the operative word, and the operational discipline of AI deployment is designing systems that fail gracefully when probably isn't good enough.
