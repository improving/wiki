---
type: Reference
title: "Getting the Right Answer for the Wrong Reason"
resource: "https://www.devlinliles.com/getting-the-right-answer-for-the-wrong-reason/"
author: "Devlin Liles"
published: '2026-08-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

You cannot trust an AI system because it got the last ten answers right. That statement will feel counterintuitive to anyone who spent time in traditional software, where a function that returns the correct output is, by definition, working correctly. AI is not that. The philosophical argument for why has been sitting in epistemology journals since 1963.

Edmund Gettier published a three-page paper that year, one of the most influential papers in twentieth-century philosophy, demolishing the classical definition of knowledge. Plato's definition held that knowledge is justified true belief: you know something if you believe it, it's true, and you have a good reason for believing it. Gettier showed this definition was wrong with counterexamples.

His classic case: Smith believes Jones will get the job, because the manager said so. Smith also counts the coins in Jones's pocket and sees ten coins. He concludes: "the man who will get the job has ten coins in his pocket." But Jones doesn't get the job — Smith does. And by coincidence, Smith also has ten coins in his pocket. Smith's belief is justified, it's true, but Smith got lucky. He doesn't actually know it. He got the right answer for the wrong reason.

LLMs do this continuously, and the problem is structural, not a matter of model quality.

Studies show models produce high-confidence responses that are correct most of the time in general domains. But in high-stakes specialized domains the numbers are worse. A 2024 JMIR study on medical reference generation found hallucination rates of roughly 28-40% depending on the model, and a meaningful fraction of those hallucinations are delivered with the same confident register as the correct answers. The issue is not just that models are wrong sometimes. The issue is that correctness and confidence are weakly coupled, and a model can produce high-confidence outputs that are right for reasons completely unrelated to understanding.

Here's how the Gettier structure plays out in LLM inference. The model is asked about a medication interaction. It produces a confident, correctly-formatted answer that happens to be accurate. But trace the reasoning path and you find the model assembled that answer from statistical patterns across millions of documents, none of which necessarily contained the specific causal mechanism the question was about. The answer is right. The justification is a mess of pattern-matching that coincidentally pointed at the correct output. That's not knowledge. That's a Gettier case at inference time.

The reason this matters for enterprise deployment is that standard evaluation methods don't catch it. You run an accuracy eval: model gets 85% correct. You ship. What you missed is the structure of the 85%: how many of those correct answers were Gettier cases where the model got lucky, and what happens to those cases when you change the question slightly, when you add noise, when the real-world context shifts the problem's framing.

The Gettier structure suggests three directions for evaluation practice. First, calibration-aware evaluation, not just accuracy measurement — evals that probe the reasoning path, vary the framing, ask follow-up questions, and check whether confidence tracks actual accuracy. Second, human review checkpoints oriented toward confident outputs rather than uncertain ones, since high confidence is where the interesting failure modes live. A model that hedges is at least signaling uncertainty. A model that answers confidently and wrong is the Gettier trap. Third, appropriate skepticism toward track record as a reliability signal. A model that has answered 10,000 questions correctly has not necessarily understood any of them. It has found outputs that matched the correct answer across its distribution. Stepping outside that distribution is where the Gettier cases are waiting.

The difference between real understanding and a Gettier case is reproducibility under adversarial conditions. That's what evals are for. That's what red-teaming is for. The philosophical problem doesn't go away, but disciplined evaluation practice is the closest operational equivalent to demanding that the justification actually explains the truth, rather than coinciding with it.
