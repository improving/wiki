---
type: Reference
title: "There Is No Right Threshold"
resource: "https://www.devlinliles.com/there-is-no-right-threshold/"
author: "Devlin Liles"
published: '2026-08-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

At what probability score does a transaction become fraud? At what toxicity score does a message become hate speech? At what confidence does a radiology scan become a positive finding? The answer, in every deployed classifier I've seen in production, is: someone picked a number.

That decision looks like an engineering choice. It is actually a philosophical one that has never been resolved. A 2,400-year-old paradox explains exactly why.

The Sorites Paradox comes from ancient Greece. "Sorites" is Greek for heap. The argument: one grain of sand is not a heap. Adding one grain to a non-heap doesn't create a heap. Therefore no number of grains ever makes a heap. The paradox runs in reverse too: a heap of 10,000 grains minus one grain is still a heap, so you can remove grains indefinitely without reaching a non-heap. Yet obviously, 1 grain is not a heap and 10,000 is. There must be a heap somewhere. We just can't say where.

This isn't a quirk of ancient thinking. Philosophers have been working on it ever since because it strikes at something real: many of the categories we use are genuinely vague. They don't have sharp edges by nature. The vagueness is in the world, not just our descriptions of it.

Every binary classifier is a sorites machine.

What happens when you move the classification threshold on a spam filter from 0.1 to 0.9? Precision goes up dramatically. Recall drops dramatically. Neither extreme is correct. There is no threshold at which you can say you've "solved" the classification problem. You've made a choice about which kind of error you'd rather make. That choice is a value judgment, not a technical finding.

A 2024 NeurIPS paper on out-of-distribution detection made this explicit. The researchers studying marginal OOD samples — the ones near the decision boundary — found exactly a sorites problem: there is no principled way to determine when something is sufficiently different from in-distribution to be flagged. They built a benchmark called IS-OOD that divides test samples by how far they sit from the distribution center, making the gradient structure visible. The harder you look at the boundary, the more arbitrary any line drawn there appears.

The standard engineering response is to tune the threshold using a validation set. But that just moves the sorites problem: at what validation metric level is the threshold acceptable? You can add another layer of criteria, but eventually you're standing on a grain of sand and calling it a heap.

This matters for how we govern AI systems.

First, threshold decisions carry moral character and require explicit ownership by someone who understands that. A fraud model's threshold at 0.6 versus 0.7 isn't a number someone optimized and forgot. It's a live policy choice about how many false accusations are acceptable versus how much fraud is tolerable. The compliance team owns that tradeoff. The model team surfaces it. When nobody has been formally handed ownership of each production threshold, there's a governance gap.

Second, thresholds are parameters to monitor, not constants to set once. The distribution of inputs drifts. A threshold calibrated on last year's fraud patterns may be misclassifying a different distribution this year. The sorites problem doesn't disappear when the world changes; it gets worse, because the shape of the vague region shifts. Threshold monitoring belongs in the MLOps pipeline alongside data drift monitoring.

Third, the appropriate threshold is often context-dependent in ways a single model can't resolve. A fraud model sitting between a business banking product and a consumer credit product might need different thresholds even if the underlying scores are identical. The severity of the consequences differs. The cost of a false positive differs. Deploying a single threshold across contexts is making an implicit philosophical claim that the contexts are equivalent. They usually aren't.

When there's no fact of the matter about the right threshold, pragmatism is the only defensible position — being explicit about what the threshold is optimizing for, making the tradeoff visible, and monitoring whether it's still working.

There is no heap. There is no correct threshold. There is only the choice that was made, documented or undocumented, owned or unowned. The governance question is which of those it is.
