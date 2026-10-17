---
type: Reference
title: "Embeddings Find the Meaning and Lose the Noun"
resource: "https://www.devlinliles.com/embeddings-find-the-meaning-and-lose-the-noun/"
author: "Devlin Liles"
published: '2026-09-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

An embedding model reads "cancel my membership" and "terminate subscription" and places them near each other in a space with hundreds of dimensions, close enough that a search for one finds the other without either sentence sharing a single word. That's the entire promise of semantic search: distance in that space approximates similarity in meaning, and a retrieval system built on it stops caring whether the query and the document happen to use the same vocabulary. For the exact problem keyword search couldn't solve, this works, and it works well enough that by 2024 it looked, briefly, like the whole retrieval problem had been solved in one move.

It hadn't, and the place it falls short is the mirror image of where keyword search excels.

An embedding model learns meaning from patterns in language, which means it's genuinely good at concepts and genuinely bad at anything that doesn't have a concept behind it. Ask it about gravity, orbital mechanics, or contract termination, and it places the query near the right cluster of ideas because those ideas have rich, well-represented meaning in whatever it was trained on. Ask it to distinguish part number 4471-B from part number 4471-C, or to find the one document containing statute citation 26 U.S.C. § 501(c)(3), and it has nothing to work with. Two part numbers that differ by one character aren't semantically different at all. They're identical in meaning and different only in the specific string, and a model built to find meaning has no mechanism for caring about a difference that carries no meaning.

Proper nouns fail the same way, for a related reason. A model trained broadly has seen the word "gravity" far more often than it's seen a specific internal product codename or a client's non-public entity name, so its representation of the common word is rich and its representation of the rare, specific one is thin, sometimes barely distinguishable from noise. Ask a semantic search system to find every document mentioning a particular vendor's internal project codename, and it may return documents about vaguely related vendors, vaguely related projects, anything conceptually adjacent, because "vaguely related" is exactly the kind of match a similarity score rewards and exact-string match doesn't.

## The mistake is calling this a bug

None of this is a flaw to be patched with a bigger model or more training data, not in the sense that would actually close the gap. It's the direct consequence of what an embedding is built to do. A vector is a compression of meaning, and meaning is exactly the thing that doesn't exist for a SKU, a citation, or a codename. Compressing something that has no semantic content just produces a less useful compression, not a wrong one that a bigger model eventually fixes.

I've written in more technical detail elsewhere about what this looks like in a production retrieval pipeline, where the actual numbers make the gap concrete. Keyword search alone, on mixed enterprise content, lands around 65% recall at ten results. Dense embeddings alone land around 75 to 80%. Neither gets an organization to a retrieval system it can trust, and the reason isn't that one method is more advanced than the other. It's that they're covering different failure surfaces, and a system tuned to close one gap has done nothing to close the other.

## Where this leaves an organization mid-journey

By this point in most organizations' actual history, someone has stood up a vector database, pointed it at the document store, and declared the search problem solved, right up until the first person asks it to find a specific contract clause number and gets back five conceptually related but factually wrong documents, ranked with total confidence. That's the predictable output of a single-method system asked to do a two-method job, not a deployment mistake. The fix is accepting that neither one, alone, was ever going to be the finish line, not picking the better of the two approaches, which is exactly the realization that pushes every serious retrieval build toward combining them, and toward the harder discipline of knowing when combining stops helping and starts getting in the way.

---

*Sources: dev.to, "BM25 vs. Vector Search: Choosing the Right Retrieval Strategy for Production Systems"; BSWEN, "BM25 vs Vector Embeddings: Which is Better for RAG Retrieval?"; "The Architecture of Enterprise AI Retrieval" (Devlin Liles, 2026).*
