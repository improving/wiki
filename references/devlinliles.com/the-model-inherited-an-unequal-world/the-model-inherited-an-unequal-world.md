---
type: Reference
title: "The Model Inherited an Unequal World"
resource: "https://www.devlinliles.com/the-model-inherited-an-unequal-world/"
author: "Devlin Liles"
published: '2026-08-06'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Bias in AI is usually framed as a content problem: the model says biased things, and you fix it with content filters or fine-tuning. That framing misses where the problem actually lives. By the time a model is producing output, the bias is already encoded in the probability distributions. The filter is patching symptoms. The cause is structural, and a philosopher named Miranda Fricker named the underlying mechanism in 2007.

Fricker's concept of epistemic injustice describes ways in which people are wronged specifically in their capacity as knowers. Her central case is testimonial injustice: a speaker's credibility is systematically deflated, their testimony weighted less, their expertise discounted, because of prejudice attached to their identity. The wronged person has knowledge. They offer it. The listener doesn't receive it at full value, not because of its content, but because of who's offering it. The injustice isn't violence or exclusion. It's a systematic distortion of the epistemic record.

Internet-scale training data encodes exactly this hierarchy.

The language composition of Common Crawl, one of the largest training data sources, is stark: English at roughly 44%, followed distantly by Russian, German, Spanish, and French, with the remaining share distributed across hundreds of other languages. This isn't just a representation gap for speakers of other languages. It's a signal about whose knowledge was published, archived, digitized, and indexed at scale. The model inherits the epistemic hierarchy of its training corpus. And the actual training-data skew is often more extreme than the crawl data suggests — Llama 2's training mix was reported as 89.7% English after preprocessing.

Research published in 2024 through the ACM Conference on Fairness, Accountability, and Transparency found that LLMs reproduce testimonial injustice at scale. Models systematically downrank, mistranslate, or fail to recognize contributions from non-dominant linguistic communities. They exhibit hermeneutical injustice: gaps in the interpretive frameworks available to make sense of experiences specific to communities that weren't well-represented in training data.

The numbers on demographic bias are consistent. Kotek et al. (ACM FAccT 2023) found that LLMs are 3 to 6 times more likely to select a gender-stereotypically aligned occupation in pronoun-resolution tasks, more extreme than the actual occupation statistics from the US Bureau of Labor Statistics. Models also exhibit geographic bias, with substantially weaker performance on tasks related to regions underrepresented in internet content.

None of this is a content filter problem. The content filter operates after the model generates output. The bias is already upstream, in the probability distributions that shape which tokens the model treats as plausible in which contexts. You cannot post-process your way out of a prior that was built on unequal data.

The most dangerous deployment contexts for this kind of bias are ones where the model's outputs influence decisions about people — hiring, lending, medical triage, legal analysis, performance evaluation — and where the model's training data underrepresents the populations those decisions affect. A model trained primarily on English-language, Western-origin professional content making decisions about a globally distributed workforce is not operating in a neutral way. It's applying the epistemic hierarchy it was trained on to populations that weren't adequately represented in building that hierarchy.

The mitigation is not zero-tolerance for AI in these contexts. It's honest exposure assessment and proportionate controls. Before deploying a model in a high-stakes decision context, characterize what populations are affected and how well-represented those populations are in the model's training data. If there's a significant gap, that gap is a risk factor that requires either stronger human review, domain-specific fine-tuning on representative data, or both.

For organizations building products that serve diverse global populations, the responsible question to model vendors is not "what content moderation does the model have?" It's "what is the demographic and linguistic composition of your training data, and how does that composition map onto this user base?" Most vendors can't answer this precisely. That's itself important information.

Naming the problem correctly is the first step to designing around it rather than patching its outputs. Epistemic injustice is not a side effect. It's a structural property of models trained on structurally unequal data. Treating it as such changes what the responsible engineering response looks like.
