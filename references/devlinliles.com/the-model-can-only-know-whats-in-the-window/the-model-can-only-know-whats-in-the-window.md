---
type: Reference
title: "The Model Can Only Know What&#x27;s in the Window"
resource: "https://www.devlinliles.com/the-model-can-only-know-whats-in-the-window/"
author: "Devlin Liles"
published: '2026-08-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Longer context windows were supposed to solve the problem. Give the model a million tokens of context and it can reason over your entire codebase, your whole document library, your complete customer history. The marketing pitch was that context constraints were an engineering problem being engineered away. The reality is more interesting, and a basic logical principle explains why the problem doesn't disappear when the window gets bigger.

Epistemic closure is a principle in logic and epistemology: if you know P, and you know that P implies Q, then you know Q. Knowledge is closed under known entailment. Your ability to draw valid conclusions is bounded by what you can access at the moment you're reasoning. You can't chain inferences across information you can't see.

A language model's context window is the full set of what the model can access during a given inference pass. The model's epistemic closure holds only within the window. Information outside it simply isn't there for the model to reason over.

The obvious response is to make the window bigger. The problem is that a larger window doesn't mean the model uses it uniformly. Research on what's been called the "lost in the middle" effect has documented this consistently since 2023.

The U-curve is reliable. Information placed at the beginning of the context window is attended to well. Information at the end is attended to well. Information in the middle, particularly in long contexts, is systematically underweighted. Liu et al. (2023, "Lost in the Middle," TACL 2024) measured accuracy drops of more than 30 percentage points on multi-document question answering when the answer document moved from position 1 to position 10 in a 20-document context. The pattern held across models and task types.

The architectural explanation involves how transformer attention is computed. The RoPE positional encoding creates a long-term decay property: tokens farther away in the sequence get reduced dot-product similarity. Softmax normalization amplifies this by concentrating attention on the highest-scoring tokens, which tend to cluster at the primacy and recency positions. The model doesn't forget the middle. It just attends to it less, and in long contexts "less" becomes "much less."

This has direct implications for how inputs to large context models are structured. Critical instructions, key constraints, and the specific passages the model needs to reason over accurately belong at the beginning or end. The middle of a long context is not reliably accessible for reasoning, regardless of what the context window limit says.

For document processing, dumping an entire knowledge base into context and expecting coherent reasoning over all of it is a category error. RAG pipelines exist for this reason. Retrieving the relevant chunks, positioning them where the model attends to them well, and being explicit about prioritization is what actually enables the epistemic closure the context window advertises.

There's a second closure implication beyond positional effects. Epistemic closure depends not just on having information in the window but on having the right information. A million-token context filled with loosely relevant documents is not the same as a ten-thousand-token context with precisely the documents needed. Retrieval quality, not just retrieval quantity, determines whether the model can close the reasoning chain.

This is where enterprise deployments routinely underinvest. Teams spend significant effort selecting and tuning the base model. They spend much less effort on what goes into the context window — retrieval quality, document chunking strategy, context construction logic. But the epistemic closure of the model's reasoning is primarily a function of context construction. The model can only reason over what's there, in a usable position, with appropriate framing.

The operational lesson is to engineer for the constraint rather than waiting for it to be engineered away. Context construction that places critical information where the model can access it, retrieval pipelines that prioritize relevance over volume, and evaluation that tests performance specifically on multi-hop reasoning across long contexts — these are where the closure failures concentrate. Epistemic closure breaks at scale. The right response is to design with the limit in mind.
