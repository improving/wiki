---
type: Reference
title: "Your Model&#x27;s Confidence Is Not What You Think It Is"
resource: "https://www.devlinliles.com/your-models-confidence-is-not-what-you-think-it-is/"
author: "Devlin Liles"
published: '2026-08-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

If I told you a system was right 70% of the time and wrong 30%, you'd adjust your trust accordingly. What you'd actually want to know is whether the system's own confidence tracks that split. Does it say "I'm confident" only when it's in the 70%, and flag uncertainty when it's in the 30%? That's calibration. Most production AI systems fail this test badly, and the failure is not incidental. It's baked in.

Philosophers have a word for the intellectual virtue of holding beliefs with the appropriate degree of confidence: epistemic humility. The well-calibrated person updates beliefs proportional to evidence, doesn't overclaim certainty they don't have, and distinguishes what they know from what they suspect. It's empirically measurable when the agent in question is a language model.

A perfectly calibrated model is one where, when it says it's 70% confident, it's right 70% of the time. When it says 90%, it's right 90% of the time. The expressed confidence is a reliable probability estimate. You can use it to make decisions. It means something.

Current large models are not calibrated in this sense.

The calibration story tells an interesting arc. A base model (before instruction tuning) tends to track fairly close to perfect calibration. It's roughly as confident as it should be. Then RLHF happens — reinforcement learning from human feedback, the training phase that makes models actually useful and safe to deploy. RLHF skews the model toward overconfidence. The RLHF-tuned model expresses 70% confidence and is right at a lower rate than that would imply. Confidence and accuracy decouple.

The mechanism isn't mysterious. RLHF trains models on human preferences. Human raters tend to prefer confident-sounding responses. Hedging language reads as less helpful, less authoritative, less useful. Over thousands of preference comparisons, the model learns that confident-sounding responses get better ratings. The training signal rewards the register of confidence independent of whether the underlying content is actually correct.

Research published in 2025 found that in GPT-4o, 15% of responses containing strong epistemic markers — phrases like "certainly," "definitely," "without a doubt" — were incorrect. The model isn't flagging these as uncertain. It's presenting them with the same verbal posture as its correct high-confidence answers. A downstream system, or a human reader, has no way to distinguish them.

The practical consequences stack up. An AI assistant that is confidently wrong in high-stakes language creates legal exposure. A model that can't flag its own uncertainty in a medical triage tool is a liability. An AI coding assistant that confidently generates incorrect code, with no expressed uncertainty, wastes more engineering time than it saves when the code fails in ways that aren't immediately obvious.

There are technical approaches to calibration. Temperature scaling adjusts the model's confidence numerically after training. Adaptive temperature scaling applies per-input adjustments rather than a global scalar, which improves calibration meaningfully. These are real improvements. They don't fully solve the problem. Calibration varies by domain, by question type, by the distribution of training data. A model that's well-calibrated on general knowledge questions may be systematically overconfident in specialized domains.

The operational response for enterprise deployments has two parts. First, expressed model confidence is a signal that requires its own evaluation, not a ground truth. Calibration metrics (Expected Calibration Error is the standard) belong alongside accuracy in any eval suite. Second, review workflows and human-in-the-loop checkpoints should be triggered by output type and risk level, not by model confidence. Relying on the model to flag its own uncertainty is delegating calibration to the system that's most likely to be miscalibrated in exactly that situation.

What you want from a production AI system is not a system that sounds confident. You want a system whose confidence you can use. Those are different things, and the difference matters at scale.
