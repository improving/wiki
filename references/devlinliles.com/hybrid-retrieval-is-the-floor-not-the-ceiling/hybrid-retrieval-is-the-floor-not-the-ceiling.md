---
type: Reference
title: "Hybrid Retrieval Is the Floor, Not the Ceiling"
resource: "https://www.devlinliles.com/hybrid-retrieval-is-the-floor-not-the-ceiling/"
author: "Devlin Liles"
published: '2026-09-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Neither method gets there alone, and the numbers are consistent enough across mixed enterprise corpora that they're worth treating as a baseline rather than a benchmark from one project. Keyword search by itself lands around 65% recall at ten results. Dense embeddings by themselves land around 75 to 80%. Run both against the same query and combine what they each find, and recall climbs to 88 to 92%. Neither approach was the answer. Running them together, and taking the union of what each one catches, was.

That's not a surprising result once each method's actual strength is visible. Keyword search catches the part number and the statute citation that a similarity score treats as noise. Semantic search catches the paraphrase and the conceptual match that a string comparison can't see at all. They fail in almost perfectly complementary places, which is exactly the condition under which combining two imperfect systems produces something meaningfully better than either, rather than just an average of two mediocre scores.

Getting the combination right is its own engineering problem, and the naive version of it, average the two scores and rank by the result, doesn't work, because BM25 scores and cosine similarity scores live on different scales that don't compare meaningfully. The fix that's become close to standard is reciprocal rank fusion: instead of comparing raw scores, look at where each method ranked a document and combine based on rank position. A document that both methods place in their top five gets weighted accordingly, without either method's raw scoring quirks distorting the outcome. This is table stakes now, not a differentiator. Any serious enterprise retrieval build in 2026 starts here.

## The differentiator moved downstream

What actually separates systems that hold up under real use from ones that quietly disappoint is what happens after retrieval returns its fifty or so candidates and before any of them reach a model. Every method discussed so far, keyword and embedding both, scores how similar a query is to a document without ever letting the two look at each other directly. A cross-encoder reranker breaks that constraint: it reads the query and each candidate together, in full, and scores relevance the way a person would if handed both side by side.

Anthropic's own published research on contextual retrieval puts a number on how much this matters. Starting from a baseline embedding search, adding context-aware chunking cuts top-20 retrieval failures by 35%. Adding keyword search fused with the embeddings takes that to 49%. Adding a cross-encoder reranker on top of both takes it to 67%. The reranker isn't a nice-to-have layered onto an already-good system. It's the single largest contributor in that stack, and it comes after the hybrid combination, not instead of it.

## More signals isn't automatically better, and this is where it gets counterintuitive

Given that keyword plus embeddings plus reranking outperforms any one method alone, the obvious next move looks like adding a third or fourth retrieval signal: metadata filters, a knowledge graph, behavioral click data. That instinct is where a lot of otherwise well-built systems start losing ground instead of gaining it, and the mechanism behind why is worth naming precisely, because it isn't "diminishing returns" in the vague sense. Language models handling long retrieved context show a documented effect where information landing in the middle of a long context degrades by more than thirty percent compared to the same information at the start or end. Every additional retrieval method that adds another chunk to what gets passed to the model has a real chance of burying the passage that actually answers the question underneath passages that don't, even when every one of them is nominally relevant.

A signal being conceptually correct isn't the same as a signal being discriminative in the specific cases where a system is currently getting things wrong. A new retrieval method has to earn its place by resolving something the existing ones miss, not by adding another accurate-but-redundant vote to a pile that's already accurate. Past the point where a corpus has been tuned against, every additional method adds noise for the reranker to sort through rather than coverage the reranker needed, and the corpus gets harder to filter to relevance exactly as it grows large enough to need filtering most. I've laid out the full failure taxonomy behind this, permissions, authority, temporal validity, and graph structure included, in a longer piece on enterprise retrieval architecture. That piece is the one to read for building this. This one is for understanding why the naive version breaks.

## The pivot this series is about to make

Everything up to this point has assumed the thing being retrieved is a document. That assumption holds for exactly as long as the only asset an organization is trying to find is something a person reads. The moment an organization starts building AI agents, prompts, and tools of its own, the same discovery problem reappears, in the same shape, for a different kind of object, and the same mistakes that took years to work out for documents are available to make all over again, faster, because nobody yet recognizes it as the same problem.

---

*Sources: "The Architecture of Enterprise AI Retrieval" (Devlin Liles, 2026); Anthropic, "Introducing Contextual Retrieval"; dev.to and BSWEN BM25/vector benchmark analyses (2026).*
