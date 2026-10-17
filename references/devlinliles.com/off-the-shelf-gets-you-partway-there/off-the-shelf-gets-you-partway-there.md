---
type: Reference
title: "Off the Shelf Gets You Partway There"
resource: "https://www.devlinliles.com/off-the-shelf-gets-you-partway-there/"
author: "Devlin Liles"
published: '2026-09-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

More than 2,500 Claude Code plugin marketplaces are registered at claudemarketplaces.com as of mid-2026, ranging from polished, actively maintained collections to abandoned repositories nobody has touched since launch. Roughly 40 products across the industry now support the same open Agent Skills specification, which means a skill written for one platform runs, unmodified, in a competitor's. Distribution, in other words, is solved. A skill can travel almost anywhere it needs to go. Whether it should be trusted once it arrives is a different question, and it's the question this entire series has actually been about, asked nine times now in nine different disguises.

Follow the thread back. A shared drive fails because nothing distinguishes the current file from the stale one. A folksonomy fails because nobody agreed on what a tag means. Keyword search fails on vocabulary it's never seen; semantic search fails on the noun it can't compress into meaning. Skill sprawl fails for the same structural reason the folder tree did: nothing catches a duplicate before it ships. Every one of these is the identical failure, wearing a different costume: a discovery problem with no authority sitting behind it, answered instead by whoever happens to be looking, or whatever got published first.

## Federation solves a real problem, and it's a narrower one than it looks

There's a genuine gap that everything built so far inside one organization's walls can't reach on its own: how does an agent find a capability that lives on the other side of a boundary neither party controls. A published specification called Agentic Resource Discovery answers exactly that, letting an organization list its available tools and agents in a file at a known path, crawled and indexed by an external registry. It's a real solution to a real problem, and it's precisely as far as it goes. A crawled entry is self-reported, batch-published metadata, exactly the kind active metadata replaced years ago inside a single organization's own catalog, and the specification explicitly hands off to the tool's own protocol once a capability is selected. Nothing in that handoff confirms the endpoint is healthy right now, which version is live, or whether the workflow calling it is authorized to invoke it unattended. Federation is a feed into a graph. It was never a substitute for building the graph.

## The goal state, stated plainly

Put every piece of this series together and the destination isn't exotic. It's one governed catalog that answers the same question for every kind of asset and every kind of consumer: is this current, is this owned, is this safe to use right now, by whoever or whatever is asking.

Documents and skills stop being two separate problems inside that catalog, because they were never actually different problems, only different objects going through the identical discovery failure. A person and a pipeline stop querying two descriptions of the same capability that happen to agree today and drift apart by next quarter, because there's one shared record: identity, description, version, owner, health, and authorization, read through two different lenses instead of maintained as two separate truths. And what crosses an organizational boundary through a federation protocol gets treated exactly like a newly authored internal skill would: verified, version-pinned, and logged into the same governance surface as everything built in-house, rather than trusted on arrival because it came with a passport.

This is the same architecture I've described elsewhere as the catalog becoming the control plane for data and AI governance together, and the reason it keeps arriving at the same shape from every direction in this series is that it's answering the same underlying question every time: who is allowed to trust this, and how would anyone find out if that trust turned out to be misplaced. An organization that started this journey with a shared drive and a search box that only found the word, not the meaning, ends it with a single system that knows the difference between current and stale, between reviewed and merely published, and between a capability that's healthy right now and one that only looks healthy because nobody has checked.

Nobody arrives here by skipping steps. Every organization in this series that's struggling with skill sprawl in 2026 is one I'd bet had never finished the earlier version of this problem for its documents either, because it's the same missing piece showing up twice. The fix was never a better search box, and it was never a bigger skill catalog. It was building the one thing that was missing at every stage of this series: something willing to say no.

---

*Sources: "Publishing a Catalog Is Not the Same as Running a Registry" (Devlin Liles, 2026); "The Catalog Is Now the Control Plane" (Devlin Liles, 2026); "Governance as the Control Plane for AI" (Devlin Liles, 2026); Agentic Resource Discovery specification (June 2026); Agentman, "The Agent Skills Ecosystem in 2026," on marketplace and cross-platform adoption figures.*
