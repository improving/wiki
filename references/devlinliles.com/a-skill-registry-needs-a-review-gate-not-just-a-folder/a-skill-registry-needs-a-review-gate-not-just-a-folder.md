---
type: Reference
title: "A Skill Registry Needs a Review Gate, Not Just a Folder"
resource: "https://www.devlinliles.com/a-skill-registry-needs-a-review-gate-not-just-a-folder/"
author: "Devlin Liles"
published: '2026-09-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A Git repository with a folder per skill is not a registry. It's a shared drive with better version history, and everything this series has already covered about why a shared drive isn't a system applies to it without modification. The difference between a folder of skills and a governed skill library isn't the storage mechanism. It's a small number of gates that run between someone writing a skill and an agent being allowed to invoke it in production, and Anthropic's own recommended lifecycle names most of them explicitly: plan, create, review, test, deploy, monitor, iterate.

Plan comes first for a reason that has nothing to do with process for its own sake. Workflow-specific skills, scoped narrowly to one repeatable task, consistently outperform broad ones, because a narrow scope makes the agent's trigger decision cleaner. A skill meant to cover invoice reconciliation, contract review, and expense categorization all at once forces the agent to guess, at the moment of matching a task to a skill, whether the current situation falls under this one broad umbrella. A skill scoped to invoice reconciliation alone doesn't require that guess. This is a planning decision, made before a line of the skill is written, and it's cheaper to get right at this stage than to fix after three overlapping broad skills already exist.

## The rule that does the most work: the author doesn't review their own skill

Security review is where most of the informal skill-sharing happening across organizations right now falls apart, and the single highest-leverage rule inside it is procedural rather than technical. The person who wrote a skill cannot be the person who approves it for deployment. That's not a vote of no confidence in the author. It's an acknowledgment that a script embedding a credential, or an instruction subtly worded to override a safety boundary, is exactly the kind of thing the person who wrote it is least likely to catch, because they wrote it with a specific intent in mind and will read it back with that same intent, not with an attacker's eye. Separation of duties is old governance, borrowed directly from financial controls and software change management, applied here to an artifact that can execute code with whatever permissions the agent invoking it happens to hold.

Evaluation is the step most informal skill-building skips entirely, and it's the step the data says matters most. A representative evaluation set for a skill covers three cases deliberately: situations where the skill should trigger, situations where it clearly should not, and the ambiguous middle where a reasonable agent could go either way. Run the new skill in isolation first, then run it again alongside the existing library, because a skill that performs well alone can still degrade the library's overall recall accuracy if its description overlaps with something already deployed. The discipline here is the same discipline this series covered for retrieval two pieces ago: a new signal has to earn its place by resolving cases the existing ones get wrong, not by adding one more plausible-looking option to a pile an agent now has to sort through.

## Version pinning is the part organizations reach for last and need first

Deploying a skill without pinning its version is the agent equivalent of a document with no publish date and no revision history, the exact failure this series opened with. Production should reference a specific, tested version, with the previous version kept available as an immediate rollback, and every update treated as a new deployment requiring the full review cycle again, not a quiet patch. A skill that changed silently between Tuesday and Thursday, with no version marker distinguishing the two, produces the identical failure mode as a stale policy document masquerading as the current one: whoever relies on it has no way to know which behavior they're actually getting.

The step most public skill libraries skip entirely, and the one that determines whether a skill's output can be trusted at all, is grounding any skill that reaches into business data behind a governed source rather than letting it query whatever it finds. A skill that runs flawlessly and returns a confident, wrong number because it pulled from an ungoverned or inconsistently defined metric has passed every code-level review and still produced exactly the failure the review was supposed to prevent. The skill encodes the procedure. Something else has to guarantee the data underneath it is what it claims to be, and that something is the same governed catalog layer this series is about to arrive at directly.

Monitoring closes the loop the same way it does for any production system: track which skills actually get invoked, re-run evaluations on a schedule rather than only at initial deployment, and deprecate skills whose failure rate climbs, rather than letting them sit in the library as one more overlapping option for the next agent to guess between. None of these seven steps is exotic. What makes them a system instead of a checklist is that they run in a fixed order, each one assuming the step before it actually happened, and the organizations getting this right are the ones treating governance as the first thing they build rather than the thing they retrofit after the first incident makes it unavoidable.

---

*Sources: Atlan, "Enterprise Skills 2026: A Governance Guide for AI Teams" (2026), seven-step implementation lifecycle; Anthropic Agent Skills documentation and security review checklist.*
