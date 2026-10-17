---
type: Reference
title: "The Shared Drive Was Never a System"
resource: "https://www.devlinliles.com/the-shared-drive-was-never-a-system/"
author: "Devlin Liles"
published: '2026-09-04'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Ask someone where the current version of a document lives and watch what happens. They don't open a search box. They open a Teams thread, scroll back three weeks, and find the file someone attached to a message titled "final v3 (2)." That's not a search failure. That's the actual system, the one that was running the whole time underneath whatever folder structure IT rolled out in 2019.

Well over three-quarters of Improving's clients are running at least one critical process off a shared drive and an Excel workbook on the day we first sit down with them: a spreadsheet reconciling numbers a database should own, a workbook that quietly became the system of record for something with real financial or regulatory weight attached to it. That's not a special case. It's the default state of a shared drive with a folder tree someone designed once, back when the organization had a fraction of its current headcount and one program line. Email quietly becomes the real record of who decided what and when. A wiki that three people update and two hundred people read, if they remember it exists. Slack or Teams search, which finds the message but not the decision the message was referencing. None of these were built as a knowledge system. They were built as places to put things, and a place to put things is not the same as a way to find them again.

The folder tree is the clearest example of a structure that made sense once and stopped making sense the moment the organization outgrew the assumptions baked into it. Someone decided, on day one, that documents belong to a client, or a project, or a department. That decision was reasonable given what existed then. Three years later the company has matrixed teams, documents that belong to two clients and no department, and a project that got renamed twice. The folder tree didn't get worse. The organization got more complicated than a tree can represent, because a tree only lets a document live in one place, and by year three almost nothing in a real business lives in only one place.

Tribal knowledge fills the gap the folder tree leaves open, and it fills it in a way that feels like it's working right up until the person holding it leaves. The actual answer to "where's our standard process for X" usually isn't in a document at all. It's in the head of whoever set the process up, phrased as "ask Sarah" or "I think it's the one Marcus sent around after that client call." That's a real retrieval system. It has excellent precision, because a person who knows the answer gives the exact answer, not fifty candidates to sort through. It has a single point of failure that never shows up on a risk register, because nobody writes "our process knowledge for onboarding depends on one person's memory" into a project plan.

## Search finds the word, not the thing

The instinct once an organization notices the folder tree isn't working is to bolt search on top of it. That fixes less than it looks like it fixes. A keyword search index reads a folder structure that was never designed to be searched, and it has no way to weigh one file against another: not by how current it is, not by who approved it, not by whether it's still true. It will happily return the draft from eighteen months ago ranked above the version that's actually in use, because nothing about the file's name or location tells the index which one is real.

The deeper problem is vocabulary. A search box only finds what the person searching already knows to call the thing. Someone looking for the reimbursement policy who types "expense report" gets nothing if the actual document is titled "T&E Guidelines," and a person new enough to not know the internal shorthand is exactly the person most likely to need the document and least likely to find it. This is the gap every enterprise search rollout eventually runs into: the technology works as advertised, and the organization's own naming inconsistency is what defeats it.

What actually happens, in almost every organization I've evaluated, is that the real search index is a person. Someone becomes the unofficial answer to "who would know," and the entire knowledge system runs on that person's availability, memory, and willingness to keep answering the same question. That's not a criticism of the person. It's a description of what fills a vacuum when nothing else is built to fill it.

## The instinct that comes next is usually right, and usually incomplete

Once this becomes visible, and it usually becomes visible during a reorg or an acquisition, when two of these ad hoc systems have to merge, the first fix everyone reaches for is the same one: organize it better. Tag things. Build a taxonomy. Get everyone using the same terms. That instinct is correct. A folder tree with no metadata and a search index with no structure genuinely can't do the job.

What the instinct usually misses is that a better taxonomy is a starting point, not a destination, and most of what gets built at this stage decays for reasons that have nothing to do with how well it was designed on day one. That's the next problem worth taking apart on its own, because it's where almost every organization's second attempt at this quietly goes wrong.

---

*Sources: Hedden Information Management, "Taxonomies vs. Ontologies"; Improving client engagement practice observations, 2024-2026.*
