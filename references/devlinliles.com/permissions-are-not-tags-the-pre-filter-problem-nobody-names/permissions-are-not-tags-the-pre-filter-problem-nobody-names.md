---
type: Reference
title: "Permissions Are Not Tags: The Pre-Filter Problem Nobody Names"
resource: "https://www.devlinliles.com/permissions-are-not-tags-the-pre-filter-problem-nobody-names/"
author: "Devlin Liles"
published: '2026-08-22'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every hybrid retrieval architecture has a stage before the six search vectors get to do anything: narrowing the candidate pool down to the documents a given query is even allowed to consider. Access permissions and metadata tags both live at that stage, and because they both look like "filters" in an architecture diagram, they get designed the same way more often than they should. They're not the same mechanism, and conflating them is where I've seen systems either leak information or quietly drop the right answer without anyone noticing.

## Why permissions have to be a hard filter

Access control is a lookup. A user's identity and a document's access control list determine eligibility, independent of what the query says. There's no ambiguity to resolve: either this person can see this document, or they can't, and that answer doesn't change based on how the question is phrased.

Which means permissions have to run as a hard exclude, every time, with no soft version. A semantically perfect match that the requesting user isn't authorized to see isn't a ranking problem to be weighed against other signals. It's a wrong answer, full stop, and the cost of getting it wrong runs one direction: a document that should have been excluded and wasn't is a real incident. A document that was excluded and shouldn't have been costs you a worse search result, nothing more. That asymmetry is the whole reason permissions get gated before relevance scoring even starts, not folded into it. You build this once, correctly, as a boring deterministic filter against identity and ACL, and you don't touch it again except when the org chart or the document's classification changes.

## Why tags are a different problem wearing the same clothes

Metadata and tag filtering looks identical in an architecture diagram: narrow the candidate pool before search runs. The mechanism underneath is completely different, because nobody hands the system a clean tag. A user asks "what's our standard process for X" in plain language, and something, a rule, a classifier, an LLM, has to decide which tags that question implies before the tag filter can do anything. That's an inference, and every inference carries an error rate that a permissions lookup never does.

The standard pattern now is what's sometimes called a self-query approach: an LLM reads the natural-language query against a schema describing the available metadata fields, business area, content type, document category, and extracts which filters apply before the search runs. It works well and it's the right default. It's still a classifier, and classifiers are wrong some fraction of the time in ways a fixed permissions lookup never is.

This is exactly the distinction I built explicit intake categorization around on a healthcare documentation project. The system separates SOPs from contracts from case studies from RFP responses at ingestion, and when a question comes in, it uses that categorization to know which track of content the question is actually about, standard operating procedure content, not RFP language, before running any deeper search. That categorization step is doing real work precisely because it's inferring intent from a question, and the entire value of the architecture is in getting that inference right consistently rather than leaving it to whatever the base retrieval model happens to prioritize.

## The choice that actually matters: hard exclude or soft boost

Here's the operational decision that determines whether a misclassified tag is a minor inconvenience or a silent failure: does a wrong filter guess exclude candidates outright, or does it just deprioritize them?

A misclassified permission has no acceptable soft version, for the reason above. A misclassified tag should almost never hard-exclude. If the system infers "SOP" from a question that was actually about a contract clause, and that inference hard-filters out every contract document before search runs, the user gets a confidently wrong answer built entirely from the wrong category of content, and there's no signal anywhere in the response that tells them something went wrong. The system looks like it worked, and nothing in the response tells anyone otherwise.

Soft-boost the tag instead: rank documents matching the inferred filter higher, but leave the rest of the candidate pool in play for the retrieval and reranking stages to sort out on their own merits. A wrong tag inference under this design costs you some ranking precision, a slightly noisier candidate pool that the reranker has to work a little harder to clean up. A wrong tag inference under a hard-exclude design costs you the correct answer entirely, with no visible symptom.

I learned the cost of skipping this distinction on an internal platform search project, in a less dramatic but equally instructive way. The plan was a single search bar with weighted match types and category filters, employees, courses, skills, structured the way a CRM search works. The architecture was sound and the demo worked. What actually gated the rollout was that only about ten percent of employee profiles had usable data behind them. A filtering and ranking system is only as good as the population it's filtering over, and no amount of clever query classification fixes a candidate pool that's mostly empty. It's the same lesson from the other direction: get the eligibility layer wrong, whether that's bad data behind your tags or an overconfident hard filter on top of them, and everything built on top of it inherits the failure.

## The rule worth keeping

Same mechanism, opposite risk posture, depending on what's being filtered. Permissions are a deterministic gate with one acceptable failure direction. Tags are a probabilistic filter with a classifier's error rate baked in, and they deserve a design that assumes that classifier will sometimes be wrong, because it will be. Build the first one once and leave it alone. Build the second one expecting to be wrong occasionally, and design so that being wrong costs you precision instead of costing you the answer.
