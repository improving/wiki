---
type: Reference
title: "Keyword Search Knows the Word, Not the Meaning"
resource: "https://www.devlinliles.com/keyword-search-knows-the-word-not-the-meaning/"
author: "Devlin Liles"
published: '2026-09-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Type "CVE-2025-32711" into a search box and there's exactly one acceptable answer: the document containing that exact string. Type "how do I cancel my membership" and the acceptable answer is something that satisfies the question, whether or not the word "cancel" or "membership" appears anywhere in it. Those are two different problems wearing the same search box, and for the better part of two decades, the entire enterprise search industry solved both of them with one tool built for the first.

BM25 is that tool, and it's older and more capable than most people give it credit for. The mechanics are simple to state and hard to improve on for what they're good at: score a document higher when it contains a query term more often, discount terms that appear in almost every document anyway (the word "the" carries no signal, "reciprocating engine" carries plenty), and slightly penalize very long documents so they don't win purely by containing more words. No embeddings, no neural network, no GPU. A well-tuned BM25 index answers in single-digit milliseconds at a scale that makes vector search look expensive, and every step of its scoring is inspectable. When it ranks a document first, the reason is right there to check.

That's precisely why it's still the right tool for part numbers, error codes, statute citations, and proper nouns. A part number isn't a concept with shades of meaning nearby. It's a string, and the document containing that string is either the right answer or it isn't. Nothing about "conceptual similarity" improves on exact match here, and a system that tries to be clever about it usually gets it wrong in a way that's hard to debug, because the failure doesn't look like a bug, it looks like a slightly-off ranking.

## Where it runs out of road

The failure mode is just as mechanical as the success. BM25 has no concept of meaning at all. It sees "cancel my membership" and "terminate subscription" as two sentences sharing zero words in common, because as far as the scoring function is concerned, they share zero words in common. A person asking the first question and a policy document written with the second phrasing will never meet, no matter how good the index is, because the index is doing exactly what it was built to do: match strings, not intent.

This is the vocabulary-mismatch problem from earlier in this series, showing up again at the retrieval layer instead of the tagging layer. Tags fail when the person tagging and the person searching don't use the same word. Keyword search fails for the identical reason, one level deeper in the stack, because the document's author and the person asking the question chose different words for the same idea, and a scoring function that only counts shared words has no way to know they meant the same thing.

The instinctive fix, more synonyms, a bigger thesaurus mapped onto the index, buys some ground and hits diminishing returns fast. Language doesn't fail in the tidy way a synonym list assumes. "Terminate" and "cancel" are close enough that a synonym map catches them. "I don't want this anymore" and "cancel my membership" are the same intent expressed with no shared vocabulary at all, and no synonym list scales to cover every way a person might phrase a question they've never had to phrase formally before.

## The gap that created an entire industry

That gap, real intent expressed in whatever words a person happens to reach for, is exactly what semantic search was built to close, and it's why every serious enterprise retrieval build over the last three years has added embeddings on top of keyword search rather than replacing it. The instinct to treat this as an upgrade, retire BM25, move everything to vectors, gets the relationship backwards. The two methods aren't competing for the same job. One finds the string. One finds the idea near the string. An organization that's just gotten its keyword search working well is about to discover that "working well" and "sufficient" are different claims, and the reason why is the next thing worth understanding clearly, because it comes with its own blind spot that's just as mechanical and just as easy to miss until it delivers a wrong answer with total confidence.

---

*Sources: ParadeDB, "Hybrid Search in PostgreSQL: The Missing Manual"; "BM25 vs. Vector Search: Choosing the Right Retrieval Strategy for Production Systems" (dev.to, 2026); Trelis Research, "Why use keyword versus Vector Search?"*
