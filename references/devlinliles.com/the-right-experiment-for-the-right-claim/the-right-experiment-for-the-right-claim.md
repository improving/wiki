---
type: Reference
title: "The Right Experiment for the Right Claim"
resource: "https://www.devlinliles.com/the-right-experiment-for-the-right-claim/"
author: "Devlin Liles"
published: '2026-07-22'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most ROI cases for enterprise AI are pre/post analyses. A pre/post analysis can prove a metric moved. It cannot prove the model moved it. Get it wrong, and you're signing a number you can't defend.

The previous post in this series established that value attribution requires a counterfactual — a structured answer to "what would have happened without the model?" — and that counterfactuals don't appear in your data unless you build them in before deployment. This post is the navigation guide for doing that. Eight experimental designs exist in common use, each supporting a different level of causal claim. Choosing the right one depends on what constraints your deployment actually gives you.

## The designs that randomize

A randomized controlled trial is the gold standard because it eliminates selection bias by construction. You randomize which units receive the model's treatment at the decision level: the customer, the claim, the transaction. The untreated group becomes your counterfactual. The key word is decision level. Randomizing by batch, by day, or by region measures the rollout, not the model.

Holdback testing is an RCT running in production. A random fraction of eligible units continues on the prior baseline while production acts on the new model's output. The gap between the two groups is the lift. This is the standard design for recommender systems, search ranking, fraud scoring, and dynamic pricing, because those domains learned early that pre/post analysis is nearly worthless in an environment that changes weekly. Holdback size is a power calculation, not a gut call. You need enough holdback volume to detect the minimum effect size that matters economically.

The stepped-wedge design is less well-known in technology circles but is exactly what most enterprise AI deployments actually need. You randomize not who gets the model but the sequence in which clusters receive it: sites, teams, regions, business units. Each cluster crosses over from control to treatment on a schedule determined by a random draw. Every cluster is its own control before it crosses. By the end of the rollout, everyone has the model, and you have a valid causal estimate from the crossing sequence. The trap is allowing rollout sequence to be driven by readiness or business urgency. The moment that happens, the sequence is no longer random, and the design degrades to observational.

## When you cannot randomize

Regression discontinuity exploits a hard threshold in the assignment rule: approve/deny, route/don't route, intervene/don't intervene. Units just above and below the threshold are, in expectation, identical on everything except which side of the line they fell on. For any AI system that drives a decisioning threshold, this is often the cleanest option available after the fact.

Difference-in-differences compares the change in outcomes over time for treated units against untreated units that were trending similarly before treatment. The key assumption is parallel pre-treatment trends. Test it in the pre-period data. It is almost always at least partially violated in practice, which means DiD estimates are best read as lower bounds on the true effect when treatment is positive.

Synthetic control is the method to reach for when you have one treated unit and many potential controls with long pre-treatment histories. You construct a weighted combination of control units whose pre-treatment trajectory matches the treated unit's, then use the post-treatment divergence as your estimate.

Interrupted time series, which compares before and after while holding nothing else constant, is the weakest design in the toolkit. It belongs in an honest analysis when nothing better is available, labeled clearly as descriptive, and paired with explicit caveats about what it cannot rule out. It should not anchor a business case.

## The design is a commitment

The strongest designs (RCT, holdback, stepped-wedge) require choices made before any data is collected. If the measurement plan shows up after the model is in production, randomization is already impossible, the baseline is already contaminated, and you are left with the weaker end of the toolkit.

The corollary is that the measurement design conversation belongs in the discovery phase, before architecture, before training, before vendor selection. The team that asks "what experiment will we run?" in week two is playing a fundamentally different game than the team that asks it at go-live.

One question settles most of the design choice: can you randomize? If yes, do it. If the rollout must be phased, randomize the sequence. If neither is possible, work down the observational ladder, match the design to the data you actually have, and state the assumption you're making in place of randomization. Then put a confidence interval on the result.

---

*Sources: Hussey & Hughes, "Design and analysis of stepped wedge trials," Contemporary Clinical Trials, 2007; Abadie, Diamond, Hainmueller, "Synthetic Control Methods for Comparative Case Studies," JASA, 2010; Pearl & Mackenzie, The Book of Why, 2018.*
