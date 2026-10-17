---
type: Reference
title: "Time Is Not a Timestamp: Fixing Temporal and Graph Retrieval"
resource: "https://www.devlinliles.com/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval/"
author: "Devlin Liles"
published: '2026-08-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Two of the six retrieval vectors in a hybrid knowledge system don't behave like the other four, and treating them the same way is where I've seen the most expensive mistakes happen. Semantic and keyword search score how well text matches text. Temporal and graph retrieval score something the text itself doesn't fully contain: when a fact stopped being true, and how a fact connects to other facts nowhere near it in the document.

## A document's date is a proxy, not the answer

Most temporal retrieval implementations do the obvious thing: sort by document date, decay older results, done. That works until it doesn't, and it doesn't in a specific, predictable way. A regulation published in 2018 can state a requirement that stayed valid until a 2022 amendment superseded it. A report filed in 2023 can describe an incident that happened in 2020, with a 2020 effective date buried in paragraph four. If your system scores relevance off the document's publish date, it will confidently retrieve the 2018 document for a question about current requirements and be wrong in a way that looks completely reasonable.

The fix that actually holds up is treating validity as a property of the fact, not the document. That means capturing, at ingestion, when a specific claim became true and when it stopped being true, independent of when the container document was published or last touched. On the compliance side of my work this shows up as effective dates and grandfathering clauses attached to individual requirements, not to the filing that contains them. A requirements database that only knows document dates will merge a superseded rule and its replacement into one undifferentiated blob the moment they're both semantically similar enough to retrieve together. A database that knows fact-level valid-from and valid-until can tell you which one applies to the date in the question, which is usually the actual question being asked.

The practical version of this, once you've done the work to extract it, is a reranking step that hard-removes expired facts before they ever reach the model, boosts anything explicitly time-bounded to the query's date, and only falls back to a general recency decay when nothing more specific is available. Recency decay is the fallback, not the strategy.

## Where graph retrieval actually pays for itself

I've been on record for a while that knowledge graphs are reasoning substrates, not storage mechanisms, and that the dominant RAG pattern, chunk documents, embed them, retrieve by similarity, is fundamentally a read-only pattern. It finds you the nearest thing to what you asked. It doesn't help you connect two facts that never appear near each other in any single document, and a meaningful share of the questions that actually matter in an enterprise knowledge system are exactly that kind of question. "Is this contractor's certification equivalent to what a different, larger operator requires under a different regulatory framework" gets answered by walking a relationship between two entities that live in entirely different documents. A single similar passage, however well matched, won't have that answer sitting inside it.

That's what a graph layer is for, and it's also exactly why it's the vector most often reached for when it isn't needed. The honest read of where graph retrieval earns its cost: multi-hop questions, entity relationships across documents, sensemaking across a large corpus where the answer is a synthesis rather than a lookup. The honest read of where it doesn't: single-fact lookups, where a well-built hybrid vector and keyword search already outperforms a graph traversal, and narrow, well-structured domains where the extraction step needed to build the graph introduces more noise than the graph removes. There's also a scale ceiling worth knowing about before you commit to the investment: graph traversal gets less discriminative as the corpus grows, and the performance gains from adding a graph layer tend to plateau once a corpus crosses somewhere in the range of five to fifteen million tokens. Past that point you're paying graph-construction cost for returns that are flattening out.

On a contract-analysis tool I built, the graph is what makes the answers defensible rather than just plausible. The system extracts entities and obligations out of every contract, builds a knowledge graph from them, and the retrieval agents query the graph rather than the raw source text. The part that matters is what that architecture preserves: every node in the graph carries a reference back to the exact clause it came from, so an answer that traversed three hops through the graph can still be traced, clause by clause, to the source documents that produced it. The graph gives you reach across documents. The reference back to source is what keeps that reach honest.

There's a cheaper way to get some of graph retrieval's multi-hop benefit than the full Microsoft GraphRAG pattern most vendors default to, and it's worth knowing about before you scope a build around the expensive version. Build a lighter open knowledge graph with entity extraction, then run personalized PageRank seeded from the entities in the query to traverse multi-hop associations, mapping the resulting scores back to passages. That approach lands roughly ten to thirty times cheaper than full community-detection-based GraphRAG on multi-hop question answering, and it's strongest on exactly the multi-hop factoid questions that justify reaching for a graph in the first place. If the business case for graph retrieval is multi-hop reasoning, that's the version to prototype first, not the heaviest one.

## The two vectors that need each other

Temporal and graph retrieval look unrelated until you hit the case where they collide, and enterprise knowledge systems hit that case constantly: an authoritative document that's gone stale, sitting next to a graph relationship that's current. A superseded rule still has strong connections in the graph to everything it used to govern. Those edges don't disappear when the rule does. This is exactly why fact-level validity has to run before graph traversal gets to use its results, not after. A graph that traverses through an expired fact and treats it as live will produce an answer that's structurally sound and factually wrong, which is a worse failure than an answer that's obviously incomplete, because nothing about it looks broken.

Get the temporal layer right first. The graph is only as trustworthy as the facts sitting on its nodes.
