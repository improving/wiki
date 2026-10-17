---
type: Reference
title: "Policy Doc or Teams Message: Measuring Authority in a Knowledge Base"
resource: "https://www.devlinliles.com/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base/"
author: "Devlin Liles"
published: '2026-08-22'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Six retrieval vectors and a reranker will get you the passages most relevant to a question. They won't tell you which of those passages you should actually believe. A knowledge base doesn't just retrieve facts, it retrieves claims, and an enterprise corpus is full of the same claim stated with wildly different authority behind it: the official policy document, the wiki page paraphrasing it, and the Teams message where someone typed out their memory of what the policy says three months ago. Relevance scoring treats all three the same if the wording is close enough. Authority is what tells you they're not.

## Authority is a property of the source, and it's mostly free to capture

The highest-leverage fix here isn't exotic. Tag every document at ingestion with structured metadata: which system it came from, its governance or approval status, whether it's been signed off by someone with the authority to do so, and its valid-from and valid-until dates. Bake that into the ranker so an audited, approved record outranks a draft by default. This is the single biggest lever available for this problem, ahead of anything more sophisticated, and it's cheap precisely because most enterprise content platforms already carry this information as metadata. SharePoint approval workflows, Confluence spaces marked official versus working, document management systems with version and sign-off status. The work is surfacing authority that already exists in the metadata and wiring it into the ranker, instead of leaving it to sit unused.

A second, nearly free source of authority comes from a system you're probably already building for a different reason: the graph vector. Authority research treats trust the way PageRank treated web links, importance propagates from how connected and referenced something is. If forty documents and Teams threads all cite the official pricing policy, and nothing cites a single offhand comment making a similar claim, that's a centrality score you can compute from the graph you already built for multi-hop retrieval. You don't need a separate authority pipeline. You need a second output from the graph you have.

A third layer, distinct from both of the above, is corroboration. A claim repeated independently across a policy document, a wiki page, and three unrelated Teams threads carries more evidential weight than a claim from one source that happens to get cited often. Structural authority and corroboration measure different things, one is about how connected a source is, the other is about how many independent witnesses agree, and a mature system should track both rather than assuming a strong score on one implies the other.

## The case where authority alone gets you in trouble

The layer that matters most in practice is what happens when sources actually disagree, and the harder failure case is a stale policy doc outranking a Teams message that happens to be right, the opposite of what most people picture when they imagine this going wrong. Authority-tier weighting on its own will occasionally suppress the correct answer with total confidence, because a static trust score has no mechanism for noticing that the high-authority source is the one that's wrong this time.

I built explicit contradiction detection into a document-processing system for exactly this reason, on a project reconstructing medical record timelines from thousands of pages of scanned documents. The system doesn't just flag when it can't read something. It flags when two entries in the same case say different things, the injury date recorded two different ways in two different documents being the case that comes up constantly. The point of surfacing that contradiction isn't to pick a winner algorithmically and move on. It's to put the disagreement in front of the person whose judgment is actually equipped to resolve it. Automatic suppression by authority tier would have quietly chosen one date and never told anyone there was a second one on record. That's a worse outcome than an unresolved flag, because the flag at least tells you where to look.

The equivalent lesson showed up on the healthcare documentation side of my work, in a smaller but telling way: an early version of a document-synthesis pipeline came back "vanilla," technical detail stripped out, when a comparable general-purpose assistant preserved it. The fix was building the prompt layer to explicitly distinguish editorial content from peer-reviewed or authoritative source material, so the system knows which register it's synthesizing from and doesn't flatten a rigorously sourced claim to the same confidence level as a casual summary. Authority has to travel with the content through every stage of processing, not just at retrieval time, or it gets lost exactly where it matters most.

## Where authority belongs in the pipeline

Permissions are a hard filter. Tags are a soft filter with a classification cost. Authority is neither. It's a reranker feature: a weight the cross-encoder applies during scoring, to candidates that are already in play. You don't want to hard-exclude the Teams message. Sometimes the Teams message is the only place anyone wrote down that the policy changed last week and the document hasn't caught up yet. You want the reranker to discount it by default, and to let corroboration or explicit contradiction detection override that default when the evidence calls for it.

That's a meaningfully different design decision than a static trust score, and it's the one worth building toward. Authority should inform ranking. Contradiction should surface where the person using the system can see it and weigh in. The moment a system starts silently picking winners between disagreeing sources based on tier alone, it has traded a transparent uncertainty for a confident wrong answer, and confident wrong answers are the ones that do the most damage, because nothing about them looks like it needs checking.
