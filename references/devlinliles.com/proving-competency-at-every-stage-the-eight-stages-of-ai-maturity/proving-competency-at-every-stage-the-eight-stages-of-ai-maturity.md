---
type: Reference
title: "Proving Competency at Every Stage: The Eight Stages of AI Maturity"
resource: "https://www.devlinliles.com/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity/"
author: "Devlin Liles"
published: '2026-07-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most AI maturity models let you feel advanced. You place yourself somewhere in the middle, nod along, and move on. Ours does not work that way. Every stage has something you either can demonstrate or cannot. This is the measurement guide: what proof looks like at each stage, what the gaps look like, and the signals that tell you whether you are where you think you are.

Use this as a diagnostic, not a race. The point is not to reach Stage 8. The point is to know exactly where you are and what honest movement requires.

---

## Stage 1: Zero AI

No AI in your workflow. All output is human-generated through human effort. This is a position, not a failure state — but it is one with a shrinking window before the competitive cost becomes real.

### Proof you have moved past it

- Verified access to at least one approved tool
- AI has touched at least one real work deliverable in the last 30 days — not a demo, not a summarize-something-you-already-know task
- At least 20 prompts logged against real work in the past 30 days

### Green signals

- AI output went to a real stakeholder at least once this month
- You have a first-hand sense of where the tool is useful for your specific work and where it is not

### Red signals

- Every AI experiment is recreational or on content that would not matter if it was wrong
- You are still in evaluation mode with nothing logged from actual work

### Gap questions

- Have you used AI on anything that would have mattered to someone if it was wrong?
- Can you show a stakeholder what you produced with AI this month?

### If you push forward without this

Skipping Stage 1 practice entirely and jumping to task agents means you have no firsthand experience of model failure patterns on your actual work. Your agent definitions will reflect theory, not evidence.

---

## Stage 2: Off the Shelf

You use tools as shipped. Every output gets reviewed, every decision stays with you. This is where prompting skill is built. Most organizations that believe they are at Stage 3 or beyond are actually here.

### Proof you have moved past it

- A consistent pattern of AI-assisted deliverables you can point to — not one-offs
- At least one prompt pattern written down somewhere other than your memory
- You have taught at least one technique to someone else (if you can teach it, you own it)
- Before-and-after prompt pairs that demonstrate your prompting has improved over time

### Green signals

- Your prompt output requires fewer edits week over week on the same class of task
- You can articulate to a colleague what works and what does not for your specific work
- You have a written record of at least one thing you learned about prompting in the last 30 days

### Red signals

- You retype the same instructions from memory every session
- You have a notes file of good prompts you never actually open
- Most use is for things that feel impressive but do not move any deliverable — AI-generated images, summaries of things you already know, rewrites you did not need
- You cannot explain to a new team member what works for your role

### Gap questions

- What is one prompt pattern you would share with a new team member right now, from memory?
- Have you written down anything you learned about prompting in the last month?
- Can you point to three AI-assisted outputs in the last 30 days that changed something a stakeholder actually saw?

### If you push forward without this

Your Stage 3 agent definitions will be based on what you think the model does rather than what it actually does on your work. Weak definitions produce agents that need constant manual correction, which is slower than not using agents at all.

---

## Stage 3: Task

You define a task agent with explicit opinions, constraints, and standards, and let it run a single defined task without step-by-step approval. You review the output, not the process. This is the first stage where AI does work you are accountable for — a fundamentally different relationship with the tool than Stage 2.

### Proof you are here

- A documented evaluation framework with at least three named quality criteria for at least one agent
- Quantified before-and-after evidence from a prompt or agent change — numbers or measurable observations, not "it seems better"
- A reusable task library with version history: you can show how agent definitions changed and why
- The agent passes its own quality bar at least 95% of the time across real work, not demo inputs
- A time savings estimate you could defend with data if someone asked

### Green signals

- When the agent produces poor output, you fix the agent definition — not the output
- Your quality bar is written down and you have shared it with at least one other person
- You can point to a specific definition change, explain what it changed, and show measured improvement
- The agent's constraints explicitly state what it is not allowed to do
- Your task library has commits or dated versions, not just a current file

### Red signals

- You regularly make manual edits to agent output — this is the single clearest signal that the agent definition is incomplete
- Quality evaluation is a feeling of "better" rather than a named, written criterion
- The task library exists only in your head or in an untouched notes file
- You have not measured time savings at all
- The agent definition has not changed in 30 days despite occasional bad outputs

### Gap questions

- What are the three quality criteria your agent is evaluated against? Write them down right now. If you cannot, you are still at Stage 2.
- When your agent last produced a poor output, did you fix the agent or fix the result?
- How has your agent definition changed in the last two weeks, and what prompted the change?
- Can you show output quality improving across a series of real runs?
- What is the agent explicitly not allowed to do?

### If you push forward without this

An agent that only performs at 85% will break a workflow system faster than any architectural decision. At 95% per-step accuracy, a 20-step pipeline completes correctly about 36% of the time. At 85%, you are below 5%. Wiring unreliable Stage 3 agents into a workflow does not solve the problem — it multiplies it. The errors travel further before someone catches them.

---

## Stage 4: Workflow

Multiple validated Stage 3 agents connected into a repeatable process, with handoffs, branching logic, and deterministic checking at every transition. Stage 4 is not Stage 3 made bigger — it is a different discipline, and the first that requires team and IT, not individual skill.

### Proof you are here

- At least one multi-step workflow running end-to-end in production on real work
- Human punch-out points that have been actively tested: someone attempted to bypass them, and the system blocked it
- At least one deterministic validation check running automatically on every output before it moves to the next step
- A signed team standards document defining output formats, quality thresholds, and conventions shared by all agents in the workflow
- An end-to-end success rate you can report — not just per-step accuracy
- An audit trail that lets you trace any failure to its origin step

### Green signals

- Your end-to-end success rate is stable or improving over a meaningful run period
- The workflow catches errors before they propagate to the next step
- You can trace any historical failure to its exact origin step using the audit trail
- Every agent in the workflow is individually passing its Stage 3 quality bar before it connects to anything else
- The team agreed on standards before agents went live, not after

### Red signals

- You are measuring per-step accuracy only and have not run an end-to-end completion measurement
- Validation between steps is a human reviewing the output — that is still Stage 2 with more steps
- Punch-out points exist on paper but have not been tested for bypass attempts
- Team standards were not documented and agreed upon before agents went live
- Any agent in the workflow still requires regular manual correction

### Gap questions

- What is your current end-to-end success rate across the full workflow length? If you do not know this number, you have not reached Stage 4.
- Can you point to a specific failure, trace it to its origin step using the audit trail, and explain what the fix was?
- Have you actively tested your punch-out points? What happened when someone tried to bypass one?
- Is every agent in your workflow passing its individual Stage 3 quality bar independently?
- Did the team agree on output standards before or after the first agent went live?

### If you push forward without this

Delegating to a workflow that cannot self-report failure means errors compound silently through the entire pipeline. Stage 5 autonomy on a Stage 4 foundation that has not been validated is not faster work — it is faster failure at a scale that is harder to untangle.

---

## Stage 5: Delegate

You assign work across connected workflows and manage by exception. Agents orchestrate and detect errors across workflows. You are not watching individual runs — the system is responsible for surfacing what requires human judgment.

### Proof you are here

- Cross-workflow protection gates exist and are proven: an error in one workflow cannot silently contaminate another
- AI artifacts are version-controlled with real commit history, not just saved file copies
- A dedicated adversarial agent is running in the pipeline with a rejection log you can produce on request
- At least one documented case where a workflow branched incorrectly, the system caught it before downstream impact, the correction was made, and the full event is logged
- A measurable ratio of self-caught errors to errors that escaped — and that ratio is improving

### Green signals

- The rejection log shows the adversarial agent is actually firing — regularly, on real work
- You have a documented recovery event, not just a documented failure
- Agent definitions show commit history driven by what the adversarial layer caught, not by hunches
- You are not manually monitoring the workflow at the same frequency you did at Stage 4

### Red signals

- The adversarial agent exists but the rejection log is empty or never acted on
- You have no documented case of the system catching a branch error — either it is never catching anything, or you are not logging catches
- Version control shows no history of definition changes driven by adversarial feedback
- You are still watching workflows manually at the same intensity as Stage 4

### Gap questions

- When did your system last catch a branch error before downstream impact? Can you show the log entry?
- What changed in your agent definitions in the last 30 days, and what did the adversarial agent surface that drove it?
- If the workflow runs tonight without anyone watching, what is the documented path for a bad output?
- Can you show the ratio of caught-to-escaped errors over the last 30 days?

### If you push forward without this

Stage 6 concurrent agents amplify the errors Stage 5 failed to catch. A bad output from one agent that was not caught at Stage 5 becomes a conflict event when multiple agents share state — and the compounding happens faster than any human can intervene.

---

## Stage 6: Coordinate

Multiple agents working concurrently on shared infrastructure. Coordination logic operates at agentic speed. The human coordination problems that used to take days now happen in minutes — which means the failure modes that used to surface slowly now surface fast and in combination.

### Proof you are here

- 30 consecutive days of parallel execution with no documented cross-contamination event
- At least one system-level failure recovered with a written root cause analysis — from production, not staging
- An audit confirming lower-stage quality gates still hold under concurrent load — they often degrade in subtle ways when multiple agents run simultaneously
- A live distributed tracing dashboard showing every agent, its current state, and its interaction history in real time

### Green signals

- The root cause analysis document points to a real production failure, not a hypothetical
- The tracing dashboard has caught something you would not have detected otherwise
- A concurrent load audit found no regressions in lower-stage quality gates
- Conflict arbitration logic has been tested with intentionally conflicting agents and documented

### Red signals

- Concurrent agents running without distributed tracing — you are operating on faith
- Conflict arbitration logic has never been tested under adversarial conditions
- Lower-stage gates have not been audited since moving to concurrent execution
- No production root cause analysis exists — only staging experiments

### Gap questions

- What does cross-contamination between your concurrent agents look like, and how would you detect it within five minutes?
- Can you show a conflict event from the last 30 days, how the system handled it, and what the trace log recorded?
- Have any lower-stage quality gates degraded under concurrent load? When did you last check?
- Is your root cause analysis from production or from a test environment?

### If you push forward without this

Stage 7 predictive supervision requires clean historical data about how your system actually fails. If Stage 6 has not run cleanly with full tracing, the historical record is corrupted and any predictive layer will be calibrated to noise rather than signal.

---

## Stages 7 and 8: Supervise and Orchestrate

Stage 7 is continuous supervision — AI systems running under team-governed policies, with adversarial agents monitoring other agents and predictive logic that identifies at-risk conditions before failures occur. Stage 8 is full orchestration — AI managing AI, allocating work and resolving conflicts inside governance frameworks humans define, with human input concentrated at the intent layer.

Both stages are aspirational. No organization is running them reliably in production today. The tools, governance frameworks, and auditable playbooks that would make them repeatable do not yet exist at enterprise scale. Research preprints and lab demos describe what they could look like. That is not the same as a certified, observable, governable production system.

The proof criteria for these stages cannot be written the same way as the earlier ones, because the field has not produced enough production examples to establish what proof looks like. The diagnostic question is blunt: if you cannot point to a system that has been running under adversarial validation for at least 12 months and survived an independent audit, you are describing a prototype. Naming the stages keeps the horizon honest. Claiming to be there is the most common counterfeit in the model.

What does apply: the governance infrastructure built at Stages 3 and 4 — quality gates, audit trails, version-controlled definitions, adversarial validation — is what makes Stages 7 and 8 theoretically reachable. If that infrastructure is solid, you are positioned to move toward supervised autonomy when the field catches up. If it is not, no amount of sophisticated tooling will get you there.

---

## The single most common misread

Most organizations are at Stage 2 and believe they are at Stage 4. The diagnostic is simple: ask what happens when the AI system encounters an unexpected input. At Stage 2, the human is watching and adapts in real time. At Stage 4, the quality gates catch it. If there are no quality gates and the human is still watching continuously, you are at Stage 2 regardless of how sophisticated the agents look.

The gap between feeling advanced and being advanced closes in one direction only: by producing the artifact. Not the impressive demo. Not the enthusiastic status update. The evaluation framework, the version-controlled agent definition, the rejection log entry, the end-to-end completion rate measured at production length.

Work backward from the proof criteria at the stage you believe you have reached. If you cannot show the artifact, you have not reached the stage. If you can show it, you have earned the right to move. That is the whole point of proving competency at every stage — not to feel advanced, but to actually be it.
