---
type: Reference
title: "How to Stop an Agent That&#x27;s Gone Wrong"
resource: "https://www.devlinliles.com/how-to-stop-an-agent-thats-gone-wrong/"
author: "Devlin Liles"
published: '2026-08-19'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# How to Stop an Agent That's Gone Wrong

The question is not whether your agents will go wrong. They will. Every team that runs agents in production eventually faces a session that's headed somewhere it shouldn't be. The question is what you can do about it when that happens, and whether you built the capability to intervene before you needed it.

Intervention is the set of mechanisms that let humans or systems modify in-flight or failed execution. It is a spectrum. At one end, you can pause gracefully and hand control to a human. At the other, you can roll back everything the agent did and return to a known-good state. Where you sit on that spectrum, and which mechanism applies, is determined by one factor: how reversible is what has already happened?

## The reversibility question

Reading a file is reversible. Writing a draft is reversible. Creating a pull request is mostly reversible, because you can close it. Sending an email is not reversible. Writing to a production database requires a compensating action. Moving money requires both a compensating action and a conversation.

The gate placement principle follows directly: the more irreversible the action, the earlier the oversight needs to happen. For purely reversible steps, you can afford to let the agent run and course-correct afterward. For irreversible steps, you need a gate before the action, not after.

"Approve before irreversible" is the right default for most production systems. It doesn't impose approval overhead on every step, only the steps where oversight actually changes the cost of being wrong.

## Interrupt-and-resume: the gold standard

LangGraph's interrupt-and-resume is the most powerful intervention mechanism available in production agentic systems. It pauses execution at any graph node, exposes the agent's current state to a human, accepts modifications to that state, and resumes from the modified point. The mechanism works because LangGraph checkpoints state at every node, so there is always a clean state to inspect and return to.

The capabilities this enables are significant. A human can review the plan at step five and redirect the agent before it takes an irreversible action at step seven. A human can correct a factual error in the agent's working memory mid-session. Or a human can change the target output format after seeing the intermediate results. None of this is possible in an execution model that doesn't checkpoint state.

The investment required: you need LangGraph as your execution model (or something with equivalent state persistence), and you need an interface that can display state and accept modifications in a form humans can actually use. The first is an architectural choice; the second is product work. Both are non-trivial. Both are worth doing for any workflow where mid-session human judgment adds value.

## Approval gates: coarser but simpler

Approval gates are a phase-boundary control mechanism rather than a per-step one. The gate fires when execution attempts to cross a phase boundary (from planning to execution, from code generation to deployment, from draft to sent). A human approves before the next phase begins.

Approval gates are less precise than interrupt-and-resume: they operate at phase granularity, not step granularity. But they are much simpler to implement. HumanLayer adds gate capability to any agentic framework with a decorator, routing the approval request to Slack, email, or a custom UI. Use them when your phases map cleanly to approval points and mid-phase intervention is not a requirement.

## The saga pattern: handling what you can't roll back

Some actions cannot be rolled back. An email sent is sent. An API call that triggered a downstream process may have already propagated. A payment processed may require days to reverse.

The saga pattern, borrowed from distributed systems architecture, is the standard mechanism for managing this. For each step in a multi-step workflow that cannot be rolled back, define a compensating action that reverses its effect. If step three fails, the saga runs compensating actions for steps one and two in reverse order.

The saga pattern requires up-front design: you must define the compensating action for each step before you build the workflow. Teams that skip this step discover their gap at the worst possible moment, during an incident when they need to undo something and have no mechanism to do so. The design conversation is worth having in planning, not in production.

## Pool-level and session-level control

In multi-agent systems, intervention operates at multiple levels. Session-level stop halts a specific runaway session without affecting concurrent sessions running on other tasks. This requires session isolation at the infrastructure level. If your agents share state, stopping one may corrupt others.

Pool-level pause freezes new task dispatch across the entire agent pool while in-flight work completes. This is the incident response mechanism: stop the bleeding without canceling work already in progress. The use case is a production incident where something is systemically wrong and you need to prevent new sessions from starting while you diagnose.

Budget override is the mechanism for acknowledging a cost-limit pause and allowing resumption. An agent that hits its token budget ceiling halts. A human reviews whether the exceedance is justified (complex task that legitimately requires more work) or indicative of a problem (runaway loop, incorrect plan). The override is a diagnostic signal as much as a cost control interface.

## Course correction vs error recovery

Error recovery and course correction are different problems. Error recovery kicks in when something went wrong. Course correction is the harder case: the agent is executing correctly, the original plan was correct when it was made, but the world has changed in a way that makes the original plan wrong.

Course correction involves impact analysis of what the plan change means for work already done, replanning from the current state, and stakeholder approval before resuming. It is distinct from error handling because the agent did nothing wrong. The environment changed, so the response pattern is different: you don't roll back, you adapt.

Building the intervention mechanisms for error recovery and then discovering you also need course correction is a common gap. Plan for both.

---

*Sources: LangGraph interrupt-and-resume documentation; HumanLayer documentation and open-source library; Augment Code agentic design pattern catalog (2026) — intervention patterns; saga / compensating transaction pattern (distributed systems literature, Richardson 2018); Vellum agentic workflows guide.*
