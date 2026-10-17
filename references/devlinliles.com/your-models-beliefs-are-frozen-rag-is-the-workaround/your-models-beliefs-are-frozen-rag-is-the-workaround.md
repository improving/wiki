---
type: Reference
title: "Your Model&#x27;s Beliefs Are Frozen. RAG Is the Workaround."
resource: "https://www.devlinliles.com/your-models-beliefs-are-frozen-rag-is-the-workaround/"
author: "Devlin Liles"
published: '2026-07-31'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A model trained in early 2024 confidently tells you about the current regulatory environment, the latest product version, or a person's current role. And it's wrong. The model isn't bad. Its beliefs are frozen, and the world moved on.

Bayesian epistemology offers a clean framework for understanding what's happening. The core idea: rational agents update their beliefs proportional to new evidence. You have a prior (your current probability estimate for some proposition). New evidence arrives. You apply Bayes' theorem and compute a posterior, your updated estimate after integrating the evidence. Good epistemic practice means your beliefs are always a function of both your prior and the evidence you've accumulated.

Language models have priors. Billions of parameters encode probability distributions shaped by training data. Ask the model something and it generates a response that reflects those priors: what was true, and commonly stated, in the data the model saw during training. The priors are often very good. But they are frozen at the training cutoff.

At inference time, the model processes your input and generates output. It does not update its weights. The priors don't change. New evidence in the conversation (a news article, a policy update, a user telling the model it got something wrong) can shift the model's response within that session through in-context processing, but it does not revise the underlying prior. The next conversation starts from the same frozen weights.

The data on time-sensitive queries makes the cost visible. A model operating on frozen priors performs substantially worse on questions that concern information that has changed since training. RAG — retrieval-augmented generation, where current documents are injected into context before the model responds — consistently recovers much of that accuracy gap. Fine-tuning with updated information can push further, but at vastly greater cost and complexity. The exact improvement varies by domain, retrieval quality, and how much the world has moved since training cutoff. The directional finding is consistent across the literature: grounding through retrieval is substantially better than relying on frozen priors for time-sensitive queries.

RAG is the Bayesian workaround. You can't update the model's weights at inference time. But you can inject evidence into the context window, and the model can process that evidence and generate a response that reflects it. Within the session, the model is reasoning from current priors plus retrieved evidence. The posterior is better than the prior alone. This is not full Bayesian updating (the weights don't change) but it's a reasonable approximation for most production use cases.

The architectural implication is that the right mental model for a RAG system is not "a chatbot that searches." It's an inference engine operating on a frozen prior, with an evidence pipeline attached to reduce the gap between what the prior knows and what's currently true. The quality of the RAG system depends on the quality of the retrieval, the relevance of what gets injected, and the model's ability to weight injected evidence appropriately against its prior.

That last point is subtle. Models don't always handle the tension between their priors and retrieved evidence well. When retrieved evidence contradicts a strongly encoded prior, models sometimes ignore the evidence in favor of the prior. This is exactly the failure mode you'd expect from a Bayesian reasoner with miscalibrated confidence: it weights the prior too heavily relative to the new evidence. The cure is better retrieval (make the evidence more obviously relevant), better prompting (make explicit that retrieved context should take precedence), and better evaluation (test specifically for cases where the model ignores contradictory evidence).

Fine-tuning is actual belief revision. When you fine-tune a model on updated data, you're changing the weights (the priors), not just injecting evidence at inference time. This is the real Bayesian update. It's also expensive: compute costs, risk of catastrophic forgetting, model stability concerns, and the need to manage the fine-tuned model as a distinct artifact in your deployment pipeline. For knowledge that changes rapidly, fine-tuning is too slow to keep up. For domain adaptation that's relatively stable, fine-tuning can produce better results than RAG.

The practical decision is: how dynamic is the knowledge you need, and how much does correctness on time-sensitive queries matter? Highly dynamic, high-stakes: prioritize RAG with a well-maintained index and strong retrieval quality. Stable domain knowledge, high-volume, performance-sensitive: consider fine-tuning once and refreshing periodically. Most enterprise deployments end up using both in layers: a fine-tuned base for domain adaptation plus RAG for current information.

There's a governance dimension that Bayesian epistemology makes explicit. A model's priors are not neutral. They reflect the distribution of content in training data: what was written, what was published, what was indexed, what was included. Topics underrepresented in training data get weaker priors. The model is more uncertain, more likely to hallucinate, more susceptible to being steered by injected evidence in domains where its prior is thin. Knowing your model's prior quality by domain (where it's confident and accurate versus where it's generating from thin coverage) is important context for designing retrieval pipelines.

The frozen-prior problem doesn't go away with bigger models or longer context windows. It's structural. Training is expensive, infrequent, and can't keep up with a world that changes daily. The Bayesian frame gives a clear vocabulary for thinking about it: priors plus evidence equals posterior. Managing the quality of the evidence pipeline is where the engineering work lives.
