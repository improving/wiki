---
type: Reference
title: "A Skill Is Just Another Thing to Find"
resource: "https://www.devlinliles.com/a-skill-is-just-another-thing-to-find/"
author: "Devlin Liles"
published: '2026-09-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Anthropic published Agent Skills in October 2025 and open-sourced the specification two months later. Strip away the framing and the format is almost defiantly plain: a folder containing a markdown file with some frontmatter, plus whatever scripts and reference material the task needs. Barry Zhang, who co-created the format, described the design intent directly: skills are organized collections of files that package procedural knowledge for agents, and the simplicity is deliberate, because anyone, human or agent, should be able to create one with nothing more than a computer.

That plainness is the whole point, and it's also the reason this series has to pivot here. A SKILL.md file describing how a finance team closes the books is, structurally, the same object as a policy document describing the same process: a piece of written knowledge that someone has to find at the moment they need it. The difference is who's doing the finding. A person searching a wiki and an agent resolving which skill to invoke mid-task are asking the identical question, just on two different clocks. I've written about that distinction in more depth elsewhere: a person doing this exploratory work reads results and decides, forgiving of an imperfect match. An agent resolving a skill mid-pipeline has no one in the loop to catch a wrong answer before it executes. Same underlying operation. Radically different tolerance for being wrong.

## The mechanism that makes this tractable at all

The reason an organization can plausibly hand an agent hundreds of these files without drowning its context window is a design choice called progressive disclosure, and it's the direct descendant of the retrieval lesson from earlier in this series. A skill loads in three stages. At startup, only the name and description load, a few dozen tokens each, which is what the agent uses to decide whether a given skill is even relevant to the task in front of it. Only when something matches does the full instruction body load. Bundled scripts and reference files load last, on demand, only if the matched skill actually needs them.

That's the metadata-first retrieval pattern from the first half of this series, rebuilt for a different kind of object. The name and description are doing exactly what a well-maintained tag or a catalog entry does for a document: letting a system narrow the field before it pays the cost of reading everything in full. Zhang put the alternative plainly: tools with poorly written, ambiguous instructions leave a model stuck with a cold start problem, permanently living in the context window whether they're relevant to the current task or not. Skills solve that the same way a good catalog solves it for documents, by making the summary cheap and the full content lazy.

## Where the parallel gets uncomfortable

Here's where the comparison stops being reassuring. Every failure mode this series has already walked through for documents is available to repeat at the skill layer, and the evidence that it's already happening is concrete rather than hypothetical. SkillsBench, the first peer-reviewed benchmark of agent skills, built by researchers from Stanford, CMU, Berkeley, and Oxford, analyzed 47,150 publicly available skills and found an average quality score of 6.2 out of 12. The researchers had to restrict their own performance testing to the top quartile, because most of what's actually published isn't good enough to move the needle either way.

The upside case for a well-built skill is real and large. Curated, reviewed skills raised agent pass rates by an average of 16.2 percentage points across the benchmark's 84 tasks, and in healthcare, the domain requiring the most specific organizational expertise, the gain was 51.9 points, the largest of any domain tested. That's not a marginal improvement. That's the difference between a general-purpose agent that's intelligent and one that's actually useful for a specific, expert task, which is exactly the gap Zhang named when he opened his own talk on the subject: agents have intelligence and capability, but not always the expertise a specific job requires. A skill is how an organization transfers that expertise, and the size of the gain tracks almost exactly with how much specialized knowledge the task demands.

## What this means for where the series goes next

Everything this series has built up to this point, the folder-tree problem, the tagging problem, the vocabulary-mismatch problem that keyword search runs into, the semantic blind spot that embeddings run into, applies again here, at the layer of skills instead of documents. The good news is that none of it has to be relearned from scratch. The bad news is that most organizations building skill libraries right now are relearning it from scratch anyway, because it doesn't yet feel like the same problem they already solved once for their document estate. The next piece in this series is about exactly where that relearning is already going wrong, in ways that are specific, documented, and avoidable.

---

*Sources: agentskills.io, Agent Skills open specification (December 18, 2025); Barry Zhang, AI Engineer Conference remarks on Agent Skills design; Atlan, "Enterprise Skills 2026: A Governance Guide for AI Teams"; SkillsBench (2026); "The Architecture of Enterprise AI Retrieval" (Devlin Liles, 2026).*
