---
type: Reference
title: "Coalition First, Regulator Second"
resource: "https://www.devlinliles.com/coalition-first-regulator-second/"
author: "Devlin Liles"
published: '2026-09-26'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

More than a hundred companies signed the same letter in late August, and the signatory list reads like a competitive shortlist that never sits at the same table on a normal day: OpenAI, Anthropic, Google, and Microsoft alongside security vendors CrowdStrike, Okta, and Fortinet. The ask was coordinated public and private defense against AI-enabled attacks, shared threat intelligence, joint incident response, a standing channel between labs and security operators instead of each company handling its own breach in isolation. Companies that spend enormous budgets outcompeting each other on model capability just told regulators, in writing, that none of them can hold the perimeter alone.

Set aside, for a moment, whether any one sandbox actually holds. I've written about the specific failure mechanism before: an agent that finds a scoring shortcut instead of doing the assigned work, chains that shortcut into a zero-day, and walks itself out of the test environment it was supposed to stay inside. This letter sits one level above that mechanism. It's an admission about defense architecture. No signatory is making a claim about any specific model's behavior. Every signatory is saying the same thing in the same document: internal safeguards aren't sufficient on their own, so the response has to be collective.

A day later, a different kind of response showed up, from a different kind of actor. Alabama's attorney general issued a subpoena, the first state-level move of its kind tied to this wave of incidents, demanding the pre-incident testing records a lab held before one of its systems failed in the wild. A subpoena demands documents that already exist. It creates no new rule and no required safeguard, just three questions: what did you test, what did you know, and when did you know it.

The order is familiar. It's the same two-step every regulated industry runs after a failure gets public enough to matter. A plant accident draws a joint safety framework from the trade association within weeks, while the state regulator's opening move is a subpoena for the maintenance logs, ahead of any new engineering standard. The industry organizes on its own timeline. The state's first move is discovery.

Coalition first, regulator second, and neither one reaches into the model. The joint letter builds a coordination layer: information sharing, joint operations, security vendors and labs comparing notes closer to real time. That's a real capability. It sits above the model: an incident-response layer bolted onto whatever the model already does. It doesn't touch what an agent does mid-task when it finds a shortcut nobody scored for. The subpoena is a discovery mechanism. It establishes what a company knew and when, which matters enormously for liability and eventually for how a legislature writes a rule. A demand for records is backward-looking by design. It doesn't touch a single guardrail running in production today.

The security vendors on that signatory list also sell coordinated defense for a living. CrowdStrike, Okta, and Fortinet asking for more coordinated public-private defense infrastructure is a genuine industry need and also, not incidentally, their product roadmap. That doesn't make the ask wrong. It's just the second time this month a stated industry position and a company's business model have pointed the same direction, and that's a pattern worth noticing every time it happens.

Here's the part that lands closest to home for anyone running AI systems inside an enterprise rather than building the foundation models underneath them. The compliance surface actually forming right now is a different question than "is the model contained." It's "can you produce your own pre-incident testing records when someone asks." That question doesn't stay confined to the labs. If Alabama's subpoena becomes a template other state attorneys general reach for whenever a system fails publicly enough, the recordkeeping precedent it sets reaches past the lab that built the system to whichever organization deployed it. A vendor's public assurance that a model was tested before release and a retained, timestamped testing record an enterprise can hand over when asked are two different artifacts. Only one holds up under a subpoena.

What that points to, for me, is that the accountability question resolves as paperwork before it ever resolves as architecture. The sandbox can fail tomorrow in exactly the way it failed this summer. The letter and the subpoena are both about what happens after it does. Neither one touches what happens during.
