---
type: Reference
title: "Lies, Lies, and Statistics: The Five Ways AI Gets Things Wrong"
resource: "https://www.devlinliles.com/lies-lies-and-statistics-the-five-ways-ai-gets-things-wrong/"
author: "Devlin Liles"
published: '2026-06-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The phrase "lies, damned lies, and statistics" entered popular use through Mark Twain, who credited it to Benjamin Disraeli. No record of Disraeli saying it has ever been found. The most famous line about misleading claims is itself misattributed, which is a fitting place to start. A claim can be fluent, confident, widely repeated, and wrong at the source.

The phrase endures because it names something real. Numbers can be technically accurate and deeply misleading at the same time, through selection, through framing, or through the omission of context that would change the conclusion. Darrell Huff catalogued the techniques in *How to Lie with Statistics* in 1954, and the book has stayed in print because the techniques never stopped working.

AI output has the same problem at scale, delivered with the fluency of someone who has read everything. Most advice about AI reliability focuses on hallucination: the model invents facts and states them confidently. Hallucination is real and important. It is also one of five categories of AI mistruth, and a defense built only against fabrication leaves the other four open.

## The Five Categories

**1. Commission: Fabrication**

The model states something false. It invents a citation, gets a fact wrong, or confabulates a detail it does not actually know. This is hallucination in its classic form.

The defense is verification. Check specific claims, especially citations, statistics, and named facts, against authoritative sources. Do not trust any claim from an AI system that you would not trust from a colleague who stated it confidently without citing a source.

Commission failures are the most visible category because they are the easiest to detect. The AI says something demonstrably wrong, and when you check, the error is obvious.

**2. Omission: The Incomplete Picture**

The model gives you true facts and leaves out the facts that would change your conclusion. The output is accurate as far as it goes. The problem is what it does not say.

The defense is to treat AI-generated analysis as a starting point and ask explicitly: "What are the strongest arguments against this conclusion?" or "What context am I missing?" An AI that omits contrary evidence is selecting, and selection can mislead as effectively as fabrication.

Omission failures are harder to detect than commission failures precisely because what is missing is invisible. You would have to know what was left out to notice it.

**3. Perspective: True Data, Misleading Synthesis**

Individual facts are true. The synthesis produces a false picture. The classic example: "the average salary for software engineers at this company is $180,000." True statement. If 10% of the company are senior executives earning $2M+ and 90% are engineers earning $130,000, the average tells you something true and misleading simultaneously. Statisticians have known this failure mode for generations. Simpson's paradox, where a trend holds in every subgroup and reverses in the aggregate, was formally described in 1951.

The defense is to ask for the distribution behind every average. Ask "what does this look like across different segments?" when an aggregate might be masking the variation that matters. Ask the AI to show its work, and read the work.

Perspective failures are common in competitive analysis, market sizing, and any context where a single number is presented as representative while the underlying distribution carries the real story.

**4. Bias: Training Data Limits**

The model has never seen your situation, your industry, your customer base, or your specific context. It has seen whatever was in its training data. If that data was not representative of your world, its advice is calibrated to a world that is not yours.

The defense is explicit context. The more you give the model about your specific situation, the less it has to rely on base rates from its training data. Be skeptical of highly confident advice about niche domains, recent events, or contexts likely underrepresented in training.

Bias failures are systematic. The model gives consistently wrong advice about a category of situation because that category was underrepresented or misrepresented in what it learned from. This is harder to detect than commission because the errors do not look like errors. They look like confident advice that happens to be miscalibrated.

**5. Frame of Reference: Anchoring and Interpretation**

The model lacks the experiential context to interpret data correctly for your situation. It gives you information that is technically accurate, interpreted through a frame that does not match your reality.

Example: asking an AI for benchmarks on developer productivity after adopting AI tools and receiving numbers from studies conducted on different team sizes, tech stacks, or workflow contexts, then comparing your team against those benchmarks as if they transfer. The numbers are real. The comparison misleads because the frame of reference does not carry over.

The defense is to ask where the comparative data comes from and whether its context matches yours. "What are the assumptions behind this benchmark?" is a useful prompt.

## Using the Taxonomy

The value of five categories over the single word "hallucination" is that each category requires a different defense. Commission failures are caught by verification. Omission failures are caught by asking for counterarguments. Perspective failures are caught by asking for distributions. Bias failures are caught by providing explicit context. Frame of reference failures are caught by asking about source conditions.

## Where the Argument Could Break

Two objections deserve an answer. The first is that this taxonomy collapses into one word, unreliability, and one defense, verification. The trouble is that verification only catches commission. An omission passes every fact check, because every fact present is true. A perspective failure passes too; the average really is $180,000. The categories matter because four of the five survive the one defense most people deploy.

The second objection is that models are improving fast enough to make the taxonomy obsolete. Fabrication rates are falling, and I expect that to continue. The other four categories are not model defects. They are properties of any system that summarizes, selects, and synthesizes, which is why Huff's catalog of statistical misdirection is still in print seventy years after publication. Humans commit all five as well. The difference is that we have a lifetime of calibration cues for human speakers, hesitation, hedging, reputation, and AI output strips those cues away and replaces them with uniform confidence.

A practitioner who knows these five categories approaches AI output the way an auditor approaches a financial statement: assume good faith, verify anyway, and know which line items tend to hide the problems. That posture is what makes AI trustworthy enough for business decisions, and unlike model quality, it is entirely within your control.
