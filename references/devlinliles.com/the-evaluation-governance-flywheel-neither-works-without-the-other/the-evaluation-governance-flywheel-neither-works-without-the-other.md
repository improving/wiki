---
type: Reference
title: "The Evaluation-Governance Flywheel: Neither Works Without the Other"
resource: "https://www.devlinliles.com/the-evaluation-governance-flywheel-neither-works-without-the-other/"
author: "Devlin Liles"
published: '2026-07-23'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The four-layer AI governance model I've written about in this series is technically sound. Layer one defines policy. Layer two discovers the AI surface area you're governing. Layer three monitors models in production for drift. Layer four enforces policy at runtime, intercepting wrong actions before they execute. Done in sequence, with each layer feeding the next, you get a complete governance stack.

The thing most organizations miss is that none of the four layers actually work without a fifth input that isn't in the model: evaluation data. Specifically, task-level evaluation of how your models actually perform on your actual work, measured against criteria your compliance environment specifies.

Layer three monitors for drift. Drift from what? If you don't have a pre-deployment measurement of model behavior, there is no baseline to drift from. Layer four enforces policy. Which policy? If you've never measured what acceptable looks like in practice, the policy is a document describing an aspiration, not a control.

Evaluation data is what turns a governance framework into a governance system.

## The METR finding that makes this concrete

METR's March 2026 PR study blind-reviewed 296 AI-generated pull requests that had already passed automated grading. Active maintainers from scikit-learn, Sphinx, and pytest evaluated them. Roughly half would not have been merged by those maintainers. The grader-versus-maintainer gap averaged about 24 percentage points across the full model set.

Claude Sonnet 4.5 demonstrated a time horizon of about 50 minutes according to the automated grader, and about 8 minutes when scored by maintainers — a 7x overstatement. That gap did not change materially as models improved over the 18-month study window. Horizons grew; the grader-versus-maintainer gap held roughly constant.

What that means for governance: automated grading is not a proxy for human-level quality judgment. Treating it as one produces a governance system that is confident in the wrong direction.

## Building evaluation into the governance loop

The evaluation harness that actually feeds governance has a specific structure: a task-representative test set, built from the actual work the system will perform, scored against criteria that reflect the compliance requirements in scope. A vendor benchmark is not that.

For a development agent operating under SOC 2 Type II, that means the test set includes tasks that exercise data handling, access control, and logging behavior, and the scoring criteria include whether the generated code would pass a security review. For a system with EU AI Act high-risk obligations, the test set covers the risk categories Annex III specifies, and the scoring criteria generate the documentation the audit requires.

That test set runs before the model goes to production. It establishes the baseline: the actual, measured behavior of the model on your actual task distribution, against your actual compliance criteria. That baseline is what layer three monitors against.

## The scaffolding finding changes what you invest in

The research shows that harness quality accounts for 17 to 21 points of variance in task completion rate, which is more variance than swapping between frontier models produces. The same model, run under a careful scaffold with proper context retrieval, tool design, and prompt caching, routinely outperforms a frontier model run naively.

Most AI governance investments today focus on the model. The scaffold, which has more effect on actual output quality, gets treated as implementation detail. A complete governance system governs the scaffold at least as carefully as it governs the model: the system prompt, the context retrieval pipeline, the tool definitions, the output parsing are all in scope for evaluation and monitoring.

## What keeps the flywheel turning

The loop has four stations: evaluation generates the baseline, the baseline informs model and scaffold selection, the deployed system is governed against that baseline, and production drift triggers re-evaluation. Each station depends on the previous one.

What keeps the loop turning is compliance obligation. An organization with SOC 2 Type II obligations can't skip layer three monitoring — the annual audit will ask for evidence of ongoing control effectiveness. An organization subject to EU AI Act Annex III can't skip the evaluation baseline — the documentation requirement specifically covers model performance on the use cases in scope. Compliance is the forcing function that keeps the governance flywheel turning when organizational inertia would rather stop it.

Compliance-aware AI development from day one builds the feedback loops that make continuous improvement possible. Each evaluation cycle tightens the baseline. Each production monitoring cycle generates data that improves the next evaluation. The systems get more reliable as the data accumulates, and the governance documentation is a byproduct of the measurement, not a separate exercise.

## The practical starting point

If you are building an AI-assisted development capability and governance feels like a later-phase problem, the sequence is backwards. The evaluation harness is cheaper to build before the model is in production than after, because you haven't accumulated the technical debt of unmeasured behavior yet.

Start with a task-representative test set. Build it from fifty real examples of the work the system will perform. Instrument it for the failure modes your compliance environment specifies. Run your candidate models against it before you select one. Publish the baseline. Wire layer three monitoring to it. When you have that, you have a governance system.

The flywheel doesn't start turning until the evaluation is running. Governance and evaluation are not sequential problems where you do one and then the other. They are concurrent and mutually dependent. The evaluation makes governance real. The governance obligation keeps the evaluation honest. Neither works without the other.

---

*Sources: METR, "PR Mergability Study" (March 2026), 296 AI-generated PRs reviewed by maintainers from scikit-learn, Sphinx, and pytest. Faros AI, "Acceleration Whiplash" (2026). EU AI Act Annex III (effective August 2, 2026). NIST AI RMF, MAP and GOVERN functions.*
