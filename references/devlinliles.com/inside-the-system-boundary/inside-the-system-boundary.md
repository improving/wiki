---
type: Reference
title: "Inside the System Boundary"
resource: "https://www.devlinliles.com/inside-the-system-boundary/"
author: "Devlin Liles"
published: '2026-07-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In early 2024 the Berkeley AI Research group made a point that practitioners had been circling for a while: state-of-the-art results now come from compound systems, not individual models. A production RAG pipeline is a retriever, a reranker, a generator, and a prompt chain. An enterprise agent is an orchestrator, a set of specialist models, a critic, and a routing layer. A fraud detection stack is a feature pipeline, an anomaly model, a gradient-boosted scorer, and a rules engine sitting on top.

That shift changes the measurement problem fundamentally. A system-level A/B test tells you whether the compound system beats the baseline. It doesn't tell you which component is doing the work, which components are deadweight, and which components are actively harming results while appearing fine on their own metrics.

## Three kinds of lift, three kinds of value

Any compound system producing a measurable business outcome is generating three types of lift simultaneously. Component lift is what each model contributes independently. Composition lift is what the orchestration layer adds — the value created by routing the right inputs to the right components. Interaction lift is what emerges from the composition itself, outcomes that no single component could have produced in isolation.

Component lift typically drives more of the measured outcome. But composition lift and interaction lift are substantially more defensible at renewal. Component lift travels with the foundation model vendor. Composition lift is your engineering. Interaction lift is your proprietary architecture. When you cannot distinguish the three, you cannot make the case that your system is worth more than a commodity API call.

## Designs that go inside

**Ablation lift** replaces one component with a credible baseline and runs the two versions in parallel. The baseline should be a genuine prior-state counterfactual (the rule the model replaced, the small default model it upgraded). The gap between the production component and the baseline is that component's lift. The critical constraint: when a supervisor and its specialists are trained together on the same objective, ablation cannot cleanly separate their contributions.

**Shadow routing** isolates the router's contribution without disrupting production. Run the production router and a baseline router in parallel on the same traffic, act on the production router's choice, and measure outcome differences on the subset of cases where the two routers disagreed. There is a trap worth noting: when the same router decides which component acts and which observations get logged, your per-component sample is router-biased.

**Specialist-isolation A/B** holds the supervisor and orchestration protocol constant while swapping a specialist. This is the right design when evaluating foundation model vendor changes, specialist fine-tunes, or retrieval strategy updates. Watch for cascade contamination: in a confidence cascade where a first-tier model handles high-confidence cases and passes the rest downstream, the second-tier model only ever sees the hard cases. Comparing tiers on their assigned samples measures sample composition, not model quality.

**Critic-gated evaluation** addresses the observer effect critics introduce. When a critic gates model outputs before they reach the user, apparent output quality partly reflects the critic's rejection rate, not the generator's capability. Critic-on and critic-off experiments on the same inputs isolate how much of the quality signal belongs to the critic.

## Goodhart compounds faster here

In a compound system, the proxy metric sits upstream of multiple interacting components. A router optimized on routing accuracy can subtly shift which specialist receives which cases in ways that look correct at the routing layer but break specialist performance at the outcome layer. The divergence compounds because each component is adapting to the upstream proxy signal, and none can see the causal chain from proxy to goal clearly enough to self-correct.

The mitigation is structural: pair every leading metric with a lagging outcome metric. Recalibrate quarterly at minimum. Refuse to auto-tune any component on a proxy metric alone.

## What belongs in the value claim

The right response to a component that adds no ablation lift is to retire it, not to defend it on Layer 1 metrics. Routing accuracy is a Layer 1 property. Router value is the Layer 2 lift the router's choices produce on the business outcome. Both belong in the operational report. Only the second belongs in the value claim.

---

*Sources: Zaharia, Khattab et al., "The Shift from Models to Compound AI Systems," Berkeley AI Research, 2024; arXiv formalizations of Goodhart's law: 2505.23445, 2410.09638; "Evaluating Compound AI Systems through Behaviors, Not Benchmarks," EMNLP Findings, 2025.*
