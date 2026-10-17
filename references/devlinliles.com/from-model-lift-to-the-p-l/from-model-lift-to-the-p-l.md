---
type: Reference
title: "From Model Lift to the P&amp;L"
resource: "https://www.devlinliles.com/from-model-lift-to-the-p-l/"
author: "Devlin Liles"
published: '2026-07-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# From Model Lift to the P&L

You ran the holdback. You measured the lift. You have a clean $2M incremental-value number. Then someone from finance asks how it shows up in EBITDA, and the number gets complicated.

That question is not pedantry. It is the real test of a measurement program. Individual causal lifts don't roll up to a P&L number by themselves. The gap between those two things is a discipline of its own, and most firms never close it. They either stop at the model-level estimate and call it done, or they read favorable movement in a Layer 3 metric and work backwards to credit AI. Neither survives a thoughtful CFO, an auditor, or a vendor renewal negotiation where someone asks you to prove the value you've been claiming.

## The problem with adding up lifts

Four AI initiatives shipped this year. Each has a holdback-backed lift estimate. The temptation is to sum them and present a total. The sum will be wrong. Three things eat the difference: cannibalization (two models partly targeting the same conversions), intermediate capture (some lift is captured in an operational metric before it reaches the financial statement), and measurement-window misalignment (windows don't coincide and non-AI drivers push on the metric differently). Stack those three sources of error and the naive sum can overstate portfolio impact by 30% or more.

The honest version requires a causal lineage map: a directed graph from model outputs through decisions through operational metrics to the reported outcome. Build it with your client before you attribute anything. The map surfaces overlapping causal paths so you can see the cannibalization structure before you accidentally credit it twice. A whiteboard drawing with the right stakeholders in the room is often enough to prevent the errors that sink ROI claims six months later.

## Match the portfolio method to the data you have

With less than six months of post-deployment history, Bayesian structural time series (Google's CausalImpact library) constructs a counterfactual trajectory from pre-period behavior and correlated control series. It produces a probability distribution over impact, not a point estimate. That distribution is honest: it shows you how uncertain the estimate is, which is information you need before you publish a number.

With six to eighteen months of history and multiple concurrent initiatives, difference-in-differences and BSTS in combination triangulate an estimate that is more robust than either alone.

At eighteen-plus months of history, marketing mix modeling becomes viable. MMM decomposes the top-line metric into contributions from each driver (AI initiatives, pricing moves, market conditions, seasonality) using a Bayesian regression over time-series data. The estimates it produces tend to survive board-level scrutiny because they account for non-AI drivers explicitly.

When you have one treated unit and many potential controls with long pre-treatment histories, synthetic control is the right fit. It constructs a weighted combination of control units that matched the treated unit's pre-treatment trajectory, then measures post-treatment divergence as the effect.

## Allocating credit when multiple initiatives share an outcome

When multiple AI initiatives jointly moved a metric, Shapley value decomposition allocates credit fairly. Each initiative gets its average marginal contribution across all possible orderings of initiative combinations. The result satisfies four axioms: efficiency (all credit is allocated), symmetry (identical contributors get equal credit), dummy (zero-contribution initiatives get zero credit), and additivity (the allocations sum to the total).

The same mathematics power SHAP in model explainability. Using Shapley consistently across both model-level and portfolio-level attribution gives you one vocabulary for attribution questions at every layer of the analysis.

## Show the intervals

Every portfolio attribution estimate carries error from three sources: the individual causal estimates, the additivity assumption you made when combining them, and the non-AI factors you estimated or excluded. Show the interval. A number presented without a confidence interval is a presentation artifact, not an analysis.

The width of the interval is information. A tight interval says your measurement program is well-designed. A wide interval says the data history is short, the lineage is noisy, or the initiatives are heavily entangled. Both belong in the report. Pretending the interval is tight when it isn't is how measurement programs lose credibility.

The firms that build credible AI measurement programs do not pretend to certainty they don't have. They show the interval, explain what it would take to narrow it, and use that explanation to make the case for better measurement design on the next initiative. That is a harder conversation than presenting a single impressive number. It is the only conversation that survives the follow-up.

---

*Sources: Brodersen et al., "Inferring causal impact using Bayesian structural time-series models," Annals of Applied Statistics, 2015; Abadie, Diamond, Hainmueller, "Synthetic Control Methods," JASA, 2010; Shapley, "A Value for n-Person Games," 1953; Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions" (SHAP), NeurIPS 2017.*
