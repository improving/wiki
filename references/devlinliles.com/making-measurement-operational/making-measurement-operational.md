---
type: Reference
title: "Making Measurement Operational"
resource: "https://www.devlinliles.com/making-measurement-operational/"
author: "Devlin Liles"
published: '2026-07-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every technique in this series (holdbacks, stepped-wedge designs, ablation studies, causal lineage maps, Shapley decomposition) requires one thing you cannot retrofit: structure built before deployment. That's not a one-time project. It's a capability.

Most organizations treat AI measurement as a project task — something you do at launch to prove the initiative worked, then hand off to whoever runs the dashboard. The organizations that actually capture and sustain AI value treat measurement differently. It is an operational function with its own tooling, cadence, ownership, and governance. It runs continuously alongside the AI portfolio.

## Five stages of measurement maturity

Most AI programs stall at stage two.

**Stage one: Instrumentation.** The telemetry that captures model inputs, outputs, decisions, and downstream actions at the granularity required for causal analysis. This is different from model monitoring. Model monitoring tracks drift and accuracy — layer-1 properties. Instrumentation for causal analysis captures the decision chain: what the model recommended, what the human or downstream system did with it, and what the outcome was.

**Stage two: Holdback design.** Randomizing a control group into every production deployment as a matter of policy. The power calculation (how large the holdback needs to be to detect a meaningful effect) should be run at design time, before deployment.

**Stage three: Active causal lift.** Running the designs from this series inside each initiative, measuring component-level contributions in compound systems, and producing layer-2 estimates with honest confidence intervals. This is where a dedicated measurement function earns its keep, because the design judgment required is not casual work.

**Stage four: Portfolio attribution.** Causal lineage maps maintained as living documents. Portfolio methods (CausalImpact, MMM, Shapley) run on a quarterly cadence. The output is a measurement report that finance co-signs, not merely tolerates.

**Stage five: Operational.** Measurement embedded in the deployment process itself, so that every new initiative enters the portfolio with a measurement plan already designed, a holdback already running, and a lineage already mapped. At this stage, measurement is not a check that happens after deployment. It is part of what deployment means.

## The tools that make it tractable

For causal inference, the PyWhy project (Microsoft's open-source DoWhy and EconML) is the standard starting point. DoWhy provides the four-step pipeline: model the problem as a causal graph, identify the estimand, estimate using a chosen method, refute through sensitivity tests. EconML provides the heterogeneous treatment effect estimators: double machine learning, causal forests, instrumental variable methods, and doubly robust estimators. Double ML deserves special attention: it uses cross-fitting to remove the confounding contribution of high-dimensional control variables before estimating the treatment effect.

For time-series portfolio attribution, Google's CausalImpact implements Bayesian structural time series in both R and Python. For large-scale MMM, the PyMC-Marketing library provides the Bayesian MMM implementation with proper uncertainty quantification.

For experiment management, Statsig and Eppo are the purpose-built options that separate the concerns traditional A/B platforms conflate: the engineering problem of safely splitting traffic and the statistical problem of interpreting results.

For model observability, Arize AI and Fiddler both provide SHAP-native feature attribution alongside drift detection and performance monitoring.

## The governance question nobody asks early enough

Tooling is the easy part. The harder part is ownership. A measurement program that lives inside the ML team will optimize for layer-1 metrics. One that lives inside finance will optimize for layer-3 attribution. The measurement capability that produces defensible causal estimates lives at the intersection of both.

The practical structure is a measurement review cadence with three participants: the ML team providing layer-1 evidence, the data science or applied analytics team providing layer-2 causal estimates, and finance providing the layer-3 context. The meeting's job is to distinguish what the evidence says from what the stakeholders would prefer it to say.

The other governance question is publication standards: what level of causal evidence is required before an initiative is credited with business impact. Setting those standards before anyone needs to use them — writing down what kind of evidence earns what kind of claim — is the single highest-leverage investment a measurement program can make.

## What this series has argued

The through-line is consistent. Accuracy is not value. A model that performs well on its evaluation metrics creates zero value if it doesn't change an action that produces a business outcome. Value is the increment: the gap between what happened and what would have happened without the model. That increment doesn't appear in your data unless you design it in before deployment.

The market mostly asserts AI ROI and calls it done. Measuring what others assert is slower and occasionally produces a number smaller than the one on the pitch deck. It is the only number that survives an audit. The only one that earns the right to be called evidence.

---

*Sources: PyWhy project: pywhy.org; EconML: github.com/py-why/EconML; CausalML (Uber): pypi.org/project/causalml; CausalImpact: google.github.io/CausalImpact; PyMC-Marketing: github.com/pymc-labs/pymc-marketing; Chernozhukov et al., "Double/debiased machine learning," Econometrics Journal, 2018.*
