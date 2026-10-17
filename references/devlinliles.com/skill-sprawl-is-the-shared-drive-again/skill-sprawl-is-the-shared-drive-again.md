---
type: Reference
title: "Skill Sprawl Is the Shared Drive Again"
resource: "https://www.devlinliles.com/skill-sprawl-is-the-shared-drive-again/"
author: "Devlin Liles"
published: '2026-09-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Elvis Sun, a former software engineer at Google, documented the moment his agent needed to read an image off his desktop, in what he called a nine-hour deep dive into his own agent setup. It tried a browser-read skill. Nothing. It tried a vision skill. Nothing. So it wrote a third skill from scratch, a read-local-image skill, and added that to the collection. Three skills, all adjacent to the same underlying job, none of them aware the other two existed. He named the pattern precisely: the skill count grows and becomes mutually non-exclusive very quickly, and that's the long-tail failure mode.

That's the folder tree from the first piece in this series, rebuilt one layer up. Nobody decided to create three overlapping skills for the same task. Each one got written by whoever hit the gap first, the same way "final v3 (2).docx" gets created by whoever hit the missing-file problem first, and neither failure traces back to any single bad decision. Both are the predictable output of letting a system accumulate without anyone responsible for noticing when two things already do the same job.

## The scale of what's already out there

The evidence that this is happening at scale, not just in one engineer's personal setup, is direct. SkillsMP, one of the larger community skill directories, indexes roughly 1.9 million public skills scraped from GitHub. A benchmark from researchers at Stanford, CMU, Berkeley, and Oxford analyzed 47,150 of those and scored the average one at 6.2 out of 12 on quality. Catalog size and catalog quality aren't just uncorrelated here. They're close to inversely related, because the same openness that let the catalog grow to nearly two million entries is the openness that let most of them ship without anyone checking whether a near-identical skill already existed.

Recall degrades as this pile grows, in a way that should sound familiar from earlier in this series. An agent choosing between three overlapping skills for the same job has to guess which one the current task actually calls for, and every additional near-duplicate makes that guess less reliable. This is the retrieval oversaturation problem again, one layer up: past a certain point, adding more candidates doesn't add coverage, it adds noise for the selection mechanism to sort through, and the corpus gets harder to resolve correctly exactly as it grows large enough to need resolving well.

## The security failure mode has no clean analogue in the document world

Sprawl alone would be a productivity problem. What makes skill sprawl a different order of concern is that a skill, unlike a stale document, can execute code. A Snyk audit of 22,511 skills across four sources found 140,963 distinct issues, roughly 6.3 per skill. The same research, run under the name ToxicSkills, tested for prompt injection specifically and found it present in 36% of the skills examined. A stale policy document sitting unread in a folder is a governance embarrassment. A skill with an injection vulnerability sitting in an agent's active toolset is a live exposure, executing with whatever permissions the agent carries, every time it's invoked.

The mechanism connecting quality and security here is worth naming plainly, because it isn't two separate problems that happen to coexist. A skill that nobody reviewed for redundancy is, structurally, also a skill nobody reviewed for what it actually does when it runs. The same absence, no gate between "someone wrote this" and "this is now available to an agent," produces both failures from one root cause. Fixing the sprawl problem and fixing the security problem turn out to be the same fix, applied at the same point in the process, which is genuinely useful news for anyone trying to prioritize where to intervene first.

## What curation actually buys, measured

The counterfactual is where this stops being a warning and starts being an argument. The same SkillsBench research that found the average public skill scoring 6.2 out of 12 also found that curated, reviewed skills lifted agent pass rates by 16.2 percentage points on average, restricted to the top quartile of what's out there. Focused skills beat broad ones by a similar margin: two or three narrow, well-scoped skills delivered an 18.6 point gain, while a single monolithic skill trying to cover everything actually reduced performance by 2.9 points. Bigger and broader isn't the failure mode's opposite. Narrower and reviewed is.

None of this is solved by better tooling for writing skills faster. It's solved the same way document sprawl eventually gets solved: someone has to own the deduplication, the review, and the decision about what gets deprecated, and that ownership has to be a structural feature of how the library gets built, not a cleanup project that happens after the mess is already large enough to notice. What that structure actually looks like, concretely, is the next piece in this series.

---

*Sources: Elvis Sun, public account of agent skill duplication (X, 2026); SkillsBench (2026), Stanford/CMU/Berkeley/Oxford/BenchFlow benchmark of agent skills; Snyk ToxicSkills research and Agensi security audit (2026), via Agentman "The Agent Skills Ecosystem in 2026."*
