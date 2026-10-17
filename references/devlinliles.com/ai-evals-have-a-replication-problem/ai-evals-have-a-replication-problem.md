---
type: Reference
title: "AI Evals Have a Replication Problem"
resource: "https://www.devlinliles.com/ai-evals-have-a-replication-problem/"
author: "Devlin Liles"
published: '2026-08-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2011, a social psychologist published a study showing that people who primed their minds with words related to the elderly walked more slowly afterward than a control group. The finding spread fast. It was cited in Malcolm Gladwell's "Blink," used in corporate training, and became one of the most-taught examples in behavioral economics. Then other labs tried to replicate it. They couldn't. Not once, not consistently. The effect wasn't real. Or if it was real, the conditions required to produce it were so specific and underspecified that no one outside the original lab could reproduce them.

That was the opening shot of the psychology replication crisis. The AI evaluation field is in an earlier version of the same crisis. The mechanism is identical. The implications are severe.

The numbers from recent research are stark. A November 2025 empirical study analyzing 640 LLM software engineering papers published between 2017 and 2025 found persistent, systematic gaps in artifact availability, environment specification, versioning rigor, and documentation clarity. Papers carrying "artifact available" badges were found not to consistently guarantee execution fidelity or long-term reproducibility. A separate 2025 paper on commercial LLM performance in empirical software engineering studies found that "same model, same prompt" reproduces reliably, but any variation in prompt framing, evaluation setup, or research group produces substantially lower consistency. The capability claim doesn't travel.

The specific failure mode here is prompt engineering as hidden methodology. When a lab publishes that their model achieves 90% on a reasoning task, the score is real and the methodology section describes the benchmark used. What it rarely describes is the exact prompt, the sampling parameters, the few-shot examples selected, the retry logic applied when outputs didn't parse correctly, or the decisions made about which test items to include. These details are not incidental to the score. They are the score. A different prompt on the same model against the same benchmark can move performance by 20 percentage points or more. That's not a quirk of sensitive tasks. It's a documented pattern across most evaluation setups.

Popper would recognize this immediately: an evaluation methodology that isn't specified precisely enough to reproduce isn't producing scientific evidence. It's producing a data point that only exists in the context of undisclosed conditions. The "90% on reasoning benchmark" claim is unfalsifiable in the same way bad social science was unfalsifiable: the conditions required to produce the result are private.

The parallel to psychology's p-hacking problem is direct. In psychology, researchers found that if you analyze data enough ways, you can usually find a significant result somewhere. In AI evals, if you try enough prompts, few-shot configurations, and output parsers, you can usually find a number that sounds good. Publication bias ensures the good number gets published. The conditions that produced it don't.

There's an additional factor in AI that didn't exist in psychology: model drift. Even if you publish the prompt alongside the score, the model at the endpoint might not be identical six months later. The replication window closes as soon as the provider silently updates weights. A score from Q1 describes a model that may not exist in Q3. The Ship of Theseus problem compounds the replication problem.

For organizations that use published AI evaluations as decision inputs — procurement, deployment authorization, compliance documentation — the practical response is straightforward but requires investment. First, don't treat published benchmark scores as external validation of what a model will do in your environment. Treat them as one signal about relative performance on the researcher's specific implementation. Second, run your own evaluations with fully specified methodology: exact prompts, exact parameters, version-pinned model identifiers, and explicit test set selection criteria. Document enough that a colleague could run the same eval three months from now and get a comparable result. Third, re-run evaluations when the model version changes. The prior evaluation result doesn't automatically transfer to the new weights.

The more structurally important response is building evaluation infrastructure rather than running evaluations ad hoc. A persistent eval suite that runs against pinned model versions and logs results over time gives you a reproducibility record. You can see when behavior shifts, when a new prompt framing changes performance, and when a model upgrade breaks capabilities you depended on. This is not exotic infrastructure. It's the same discipline applied to software regression testing. AI evaluation has been slower to adopt it because the field has been moving fast and because the tooling for version-pinned, automated AI evaluation is relatively immature. The tooling is catching up. The discipline needs to follow.

The deeper point is epistemic. When the psychology replication crisis broke, it forced a reckoning with what "we know X" actually means in behavioral science. AI is approaching a similar reckoning. The capability claims made by researchers and vendors over the last several years are more qualified than they appear. The scores are real. The conditions that produced them are frequently not documented well enough to reproduce. What that means for any specific claimed capability in any specific deployment context is often genuinely unknown.

Reproduce your evals or treat them as weak evidence. There's no third option.
