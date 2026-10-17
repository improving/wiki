---
type: Reference
title: "The Defect Is in the Definition"
resource: "https://www.devlinliles.com/the-defect-is-in-the-definition/"
author: "Devlin Liles"
published: '2026-08-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every software team knows the cost of finding a defect late. The multiplier varies depending on where in the SDLC you catch it, somewhere between 10x and 100x, but the direction is always the same: the later the find, the worse the math. In agentic systems, autonomy sharpens that penalty. An agent executing confidently toward a misspecified goal doesn't just produce a wrong answer. It produces a trail of irreversible actions, consumed budget, and downstream artifacts that all have to be unwound.

Planning answers how. Definition answers what. They are sequential, and they are not the same problem. Most agentic development failures I've observed trace back to definition, not execution. The agent did exactly what it was told. What it was told was wrong.

## What definition actually means

A well-defined task has four things, all written down: what you want, how you'll know it's done, what's off-limits, and what you're assuming going in. All four must be explicit.

The goal is the obvious one. Teams usually get this right at the headline level and wrong at the detail level. "Implement the authentication flow" is a goal. It is also a prompt for fifteen follow-on questions: which auth methods, which user types, what happens on failure, what state gets persisted, what's the session lifetime. An agent will answer all fifteen questions itself, without asking, using whatever assumptions are most natural from its training. Some of those answers will be correct. Some will be confident and wrong.

Acceptance criteria encoding bakes the definition of done directly into the task artifact. The agent has an internal check rather than relying on external review. BDD format, Given / When / Then, is the most effective structure for this because it is simultaneously a human-readable requirement and an executable test specification. A task without acceptance criteria is a task where "done" is subjective, which means the agent will decide when it's done, which means the agent will often stop too early or solve too much.

## Out-of-scope declarations are not optional

Agents are completion-seeking. That's the point, and it's also the failure mode. Without explicit out-of-scope declarations, an agent will expand into adjacent problems. The agent understood the task perfectly. The problem is that adjacent tasks were never declared out of scope, so from the agent's perspective, solving them was still within the assignment.

The pattern I've seen most often: a developer asks an agent to update an API endpoint. The agent updates the endpoint, notices that the corresponding tests are outdated, updates the tests, notices that the documentation doesn't match, updates the documentation, and in the documentation update discovers a related endpoint with a similar issue. By step six, the agent is three layers removed from the original task. All of it technically correct. None of it what was asked for.

Scope boundary confirmation is the practice of explicitly declaring what is out of scope before execution begins. It sounds obvious. It is almost never done. The discipline required mirrors what it takes to write a good ticket: most people skip it because they're confident the work is clear, and they discover it wasn't clear when the result comes back wrong.

## Assumption surfacing before execution

Every task carries assumptions the agent must make to execute it. The question is whether those assumptions are reviewed before or after the agent acts on them.

Assumption surfacing makes this list explicit. The agent generates its assumptions as a pre-execution artifact. A human reviews and corrects them. Only then does execution begin. Unchecked assumptions are the most common cause of confident-but-wrong execution. The agent isn't hallucinating; it's extrapolating from premises that were never verified.

Dependency mapping is the structural version of this: identifying which tasks must complete before others can begin, and surfacing the critical path before execution starts. In single-agent workflows this is simple. In multi-agent systems where agents work in parallel, dependency mapping is what prevents two agents from executing the same task with different assumptions, or one agent from starting before another's output is available.

## Specification formats matter

The format in which you encode a definition is not cosmetic. Machine-readable formats give agents ground-truth specifications they can reason against: OpenAPI for API contracts, JSON Schema for data structures, BDD Gherkin for behavioral specs. Prose specifications require the agent to interpret intent, which reintroduces ambiguity.

Structured YAML and XML task definitions encode tasks as data, enabling validation and templating, and making the whole backlog programmatically queryable. A team that stores task definitions as structured data can validate new tasks against existing ones for redundancy or contradiction (semantic deduplication) before they enter the work queue. This prevents agents from implementing the same thing twice with different names, a failure mode that becomes common as backlogs grow large enough that humans stop reading everything in them.

## Requirements validation as a gate

Requirements validation is the pre-execution check that proposed requirements are complete, testable, internally consistent, and not in contradiction with existing requirements. It is to definition what a linter is to code: it catches the obvious problems before they become expensive ones.

Most implementations stop at completeness. Testability and internal consistency are harder and more valuable. A requirement that isn't testable cannot produce a passing evaluation. A requirement that contradicts an existing one will cause an agent to satisfy one at the expense of the other, consistently, and the failure will look like an execution problem until someone traces it back to the definitions.

The rule of thumb I use: if you can't write a test that would fail if the requirement were violated, the requirement is not yet defined well enough to execute.

---

*Sources: Augment Code agentic design pattern catalog (2026); Vellum agentic workflows guide; BDD / Gherkin specification format (Cucumber documentation); OpenAPI specification standard; Iterathon agent orchestration guide.*
