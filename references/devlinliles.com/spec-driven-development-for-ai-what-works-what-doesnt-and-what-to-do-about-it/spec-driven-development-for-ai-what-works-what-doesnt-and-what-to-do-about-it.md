---
type: Reference
title: "Spec-Driven Development for AI: What Works, What Doesn&#x27;t, and What to Do About It"
resource: "https://www.devlinliles.com/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it/"
author: "Devlin Liles"
published: '2026-07-22'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Here is the bet most teams are making: write a system prompt that describes what the agent should do, run it against a few test cases, watch it work, and ship. The prompt is the spec. The spec is the documentation. The documentation is the test. One artifact does all three jobs, and none of them well.

Spec-driven development for AI agents is the discipline of separating those three things. The field is real, the tooling is maturing, and the pattern works. It also has hard limits that most of the enthusiasts aren't telling you about.

## What spec-driven development means

The core idea is borrowed directly from test-driven development. TDD forces you to define what "correct" means before you build. Spec-driven development for agents does the same thing for behavior: before the agent does anything, you define the output schemas it must produce, the acceptance criteria each response must satisfy, and the contracts governing every tool it can call.

AWS Kiro, which moved to general availability in May 2026, operationalizes this with a three-file pattern: requirements.md (written in EARS notation), design.md, and tasks.md. EARS — Easy Approach to Requirements Syntax — was developed for aerospace, where ambiguous requirements kill people. The format produces acceptance criteria that are unambiguous and machine-testable. Thoughtworks called it out explicitly in Tech Radar Vol. 33 (November 2025) as a key practice in AI development.

Anthropic's model specification was decomposed into 205 atomic, testable tenets. Each one runs through adversarial multi-turn scenarios before it's considered specified. That pattern scales down. If your agent has a behavioral claim ("this agent will never expose PII to unauthenticated callers"), that claim needs to decompose into testable assertions, not prose.

The structured output piece is where this gets concrete for multi-agent systems. When one agent's output feeds another, an output schema is an inter-agent contract. OpenAI's strict: true mode enforces this at the platform level. This is what API contracts do for microservices. The thing that made microservices workable in production was not the services themselves — it was the contracts between them.

## Where it breaks

Spec-driven development solves a specific part of the reliability problem. One part. The field is doing you no favors by overselling it.

**Distribution shift kills the spec.** Research on evaluation under prompt perturbation shows accuracy drops of up to 54% with no changes to the model and no changes to the spec. The inputs drifted, and the model's performance followed them down. This is not a tooling problem. It is a property of how LLMs generalize: they satisfy the spec's letter under nominal inputs and violate its spirit when the distribution shifts.

**Error handling is where specs are most commonly incomplete and LLMs are most commonly unreliable.** The parts of a behavioral spec that engineers skip — what the agent should do when the database returns null, when the upstream service times out, when the input is malformed in a way the spec didn't anticipate — are precisely the cases where models generate confident, plausible, wrong behavior.

**Constraint accumulation degrades performance.** A May 2026 paper on constraint decay (arXiv:2605.06445) found that as structural constraints accumulate in a spec, LLM performance degrades substantially. Agents perform acceptably in simple frameworks but fail badly in convention-heavy ones. The specific failure cluster: data-layer defects, particularly bad query composition and ORM violations.

**Version drift is silent.** A prompt that ran correctly yesterday may fail today following a model update. The spec didn't change. The model did. If your only safeguard is the spec, you don't find out until something downstream fails.

**MCP is the canonical example of an under-specified tool contract.** The Model Context Protocol has a tool schema that describes what a tool does. It doesn't constrain when the tool may be called or under what conditions. In 2025, 99 CVEs were published for MCP-related software. Tool Poisoning Attacks embed malicious instructions in tool descriptions, invisible to users, processed as operational context by the model.

## What to do with this

The spec constrains what the system can do. Every constraint you make machine-checkable is one less thing you're trusting to the model's probabilistic judgment. The goal is knowing, with precision, which parts you're speccing and which parts you're trusting to the model, and having explicit tests for each category.

The Agent Behavioral Contracts framework (ABC, arXiv:2602.22302) formalizes what a complete contract looks like: C = (P, I, G, R): Preconditions, Invariants, Governance, Recovery. The Drift Bounds Theorem it introduces: if your recovery rate exceeds your natural drift rate, behavioral drift converges to a predictable ceiling. Agent reliability is not fundamentally chaotic. It can be bounded, if you define the contract fully, including recovery paths.

The art of the practical: start with the parts that are specifiable. Define your output schemas. Write your tool call contracts with conditions for when each tool may be invoked, not just what it does. Draft your acceptance criteria in EARS notation for one or two critical behaviors. Run adversarial test cases against those criteria before you ship. That is a morning's work for a team that already knows what the agent is supposed to do.

The parts that resist formalization — tone, judgment, contextual appropriateness — get tested differently: behaviorally, at volume, with human review for edge cases, and with regression detection when the model updates. You do not get to spec those requirements away. You are trusting the model's training, and you should know that's what you're doing.

There is no light switch moment where specs solve the AI reliability problem. What they do is push the failure boundary forward, make the failures you get more predictable, and replace a class of surprises with a class of bounded risks. Taking it seriously, in both what it offers and what it doesn't, is how teams build agents that hold up in production.

---

*Sources: AWS Kiro documentation (GA May 2026); Thoughtworks Technology Radar Vol. 33 (November 2025); Anthropic model specification; Agent Behavioral Contracts framework (arXiv:2602.22302); Constraint Decay in LLM-Generated Code (arXiv:2605.06445, May 2026); OWASP MCP Top 10; Veracode/CodeRabbit AI-Generated Code Security Study (2025).*
