---
type: Reference
title: "One Backward Pass Is Enough to Prune Better"
resource: "https://www.devlinliles.com/one-backward-pass-is-enough-to-prune-better/"
author: "Devlin Liles"
published: '2026-09-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

WANDA prunes a large language model by multiplying a weight's magnitude by the norm of the activation feeding it, then cutting the smallest scores until half the weights are gone. One forward pass, no gradients, no fine-tuning. It works because it's cheap: that's the entire design goal. Every output neuron in a layer gets the same pruning budget whether it's carrying a fact the model actually needs or something that's safe to throw away.

Magnitude times activation is a proxy. It tells you how loud a weight is. Whether removing that weight actually moves the loss is a separate question, and WANDA never asks it. A weight can produce a large activation and still be redundant, because another neuron computes nearly the same thing downstream. A weight can look small and unremarkable and still be load-bearing, because it's the only path carrying a signal the rest of the network depends on. WANDA can't see that difference. It was never given the information to see it.

F-WANDA gets that information by asking a sharper question: how much would the loss move if this particular weight disappeared. One backward pass gives you a Fisher-style estimate of exactly that, a read on how sensitive the output actually is to each weight, built straight from the loss instead of from raw activation. Fold that into the pruning score, and neurons that looked identically prunable under WANDA stop looking identical. Some earn more of the sparsity budget. Some earn less. The budget stops being handed out evenly and starts being handed out where the model can afford it.

What makes this worth writing about is the arithmetic behind that one backward pass. WANDA's entire pitch was skipping the loss function altogether: no gradient, no optimizer state, no repeated calibration cycles hunting for the right mask. That's what let it prune a 70B model without a training cluster behind it. Fine-tuning-based recovery methods pay for their accuracy with dozens or hundreds of passes over calibration data, the exact cost post-training pruning exists to avoid. F-WANDA spends one pass, which costs something compared to zero. Measured against everything else on the table, that cost is close enough to free that the comparison stops being interesting, and the whole method name is a bet that most of what a gradient can tell you shows up the first time you ask.

The "sustainable deployment" language in the title earns its place. Post-training pruning exists because someone wants a smaller model in production without paying to train one from scratch, and every point of accuracy a smarter pruning score preserves is a point nobody has to buy back later with a bigger model or a longer recovery run. The cost that matters is the inference cost saved for the entire life of the deployed model, paid out over every request it ever serves. One backward pass at pruning time barely registers against that.

WANDA's "no gradients at all" purity reads like a snapshot of a moment when even one backward pass over a large model felt too expensive to justify. F-WANDA is what happens when someone goes back and checks whether that constraint was still buying anything. What nobody had re-priced was the assumption that a backward pass wasn't worth the cost. The gradient itself stayed cheap the whole time.
