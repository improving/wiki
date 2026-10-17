---
type: Reference
title: "Your Coding Agent Doesn&#x27;t Know What Your Last Three Engineers Knew"
resource: "https://www.devlinliles.com/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew/"
author: "Devlin Liles"
published: '2026-10-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I watched a coding agent ship a change last month that passed every lint rule, matched the style guide, and would have taken down a production service in about four hours. The bug lived in a convention nobody wrote down: the service pins a dependency version because of an incident eight months back, and the reason lives in three people's memory, two of whom left the company before the agent ever wrote a line of that fix.

The agent had everything a coding agent is supposed to have. It had the repository, the style guide, the lint configuration, the commit history going back years, and it read all of that correctly. What it didn't have was the conversation that happened in an incident channel eight months earlier, the one where someone typed "pin it, don't touch this until we've talked to the vendor" and then never wrote that sentence anywhere the agent could later find it.

Most organizations never write that sentence down, because writing it down feels redundant when the person who knows it is still sitting three desks away. The question gets answered in Slack, or in the hallway before standup, and the answer never leaves that conversation. The knowledge stays retrievable exactly as long as the person stays retrievable, and nobody notices the dependency until the day it breaks and the person who could explain it already gave their notice.

That gap gets more dangerous as coding agents get better. A junior engineer's bad pull request usually looks like a bad pull request: rushed, inconsistent, missing an edge case a reviewer can spot on sight. A senior reviewer catches the real problem because something about the change triggers a memory of the incident, even before they can articulate why. A coding agent's pull request doesn't trigger that memory, because it doesn't read as wrong. It looks clean and idiomatic, and it passes every automated check the org has built. The reviewer has no reason to slow down, because a PR that reads as competent doesn't ask for the kind of attention that catches missing context.

That's the gap the paper is aiming at: an organizational memory layer a coding agent can query the way it queries the codebase, so the reasoning behind a pin, a workaround, or an ugly-looking pattern stays retrievable after the people who knew it have moved on.

Building that layer is harder than it sounds, and it's harder in a specific way. It's a people problem wearing a systems-design costume. A retrieval layer only surfaces knowledge that got written down first, in language specific enough to still mean something eighteen months later. Someone still has to sit with the engineer who's leaving and ask why that dependency is pinned, or the incident retro still has to capture the actual decision instead of a generic postmortem line. Most orgs skip that step today because nobody budgets time for it. The three people who knew about the pin never felt urgency to write the wiki page while they were still around to just answer the question.

A shared memory layer doesn't generate the knowledge on its own. It only gives an organization somewhere to put it, and only if someone does the work of capturing it before the person who has it walks out the door.
