---
type: Reference
title: "Unidirectional Quality Gates in AI-Assisted Development: The Ratchet Pattern"
resource: "https://www.devlinliles.com/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern/"
author: "Devlin Liles"
published: '2026-07-06'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Quality metric regression in AI-assisted development tends to be gradual and invisible. It does not arrive as a dramatic failure. It arrives as test coverage that drifts down a few percentage points per sprint, as lint warnings that accumulate in recently touched files, as type errors that appear in modules that were clean a month ago. No single merge introduces a large regression. The degradation is the cumulative effect of many small ones.

Human developers produce the same pattern. The throughput of AI agents accelerates the timeline considerably: what a human team might allow to accumulate over a quarter, a team running parallel AI agents can accumulate in two weeks.

The ratchet pattern is a straightforward mechanical response to this problem: quality metrics are enforced to be monotonically non-decreasing. A merge that would lower any measured metric below its recorded floor is blocked at the gate. The name borrows from the mechanical device, a gear with a pawl that permits rotation in one direction and locks against the other. Quality can advance freely. It cannot slip back.

## How the Mechanism Works

The ratchet state is stored in a checked-in file that records the current floor for each metric category: branch coverage percentage, total lint violations, type check errors, import boundary violations, and whatever other metrics the team has chosen to track. This file is updated whenever a merge improves on the current floor. It is never updated downward.

Before every merge, the pipeline runs the full measurement suite against the incoming change. Each measurement is compared to the corresponding value in the ratchet file. If any measurement falls below its floor, the merge is blocked with an explicit report showing which metric regressed and by how much.

The elegance of this approach is in what it does not require: it does not require a human reviewer to notice that a particular file's coverage dropped, it does not require a team norm about test coverage that depends on people remembering to check, and it does not require any per-PR configuration. The floor is defined once and enforced automatically on every merge.

## The Pre-Session Layer

The ratchet described above is a post-implementation gate. There is a complementary approach that operates earlier: checking structural constraints before an agent session begins, before any code is written.

Import boundary violations, type export constraints, and dependency direction rules are all properties of the codebase that can be checked against the intended scope of a task before any code is generated. If the task as specified would require an agent to work across a module boundary that the architecture does not permit, surfacing that constraint before the session starts is preferable to surfacing it at merge time.

Pre-session constraint checking requires encoding the structural rules of the codebase in a form the orchestrator can query. This is additional tooling, but it prevents a category of work from being attempted at all when the architectural constraints would invalidate it, saving the agent session cost and avoiding the friction of a blocked merge after work is complete.

## Calibrating the Floor

One practical question the ratchet raises immediately: what is the right starting floor? Setting the initial floor too high, at a value the codebase does not currently meet, blocks all merges immediately. Setting it too low fails to provide meaningful enforcement.

The practical answer is to measure the current state of the codebase, use those measurements as the initial floor, and then treat improvements as they come. This approach means the ratchet does not require any pre-existing quality discipline; it only requires that quality not get worse from wherever the team is starting.

There is nuance here for codebases with areas of intentionally different quality expectations: legacy code that will not be tested, generated files that should be excluded from coverage, experimental modules with acknowledged technical debt. The ratchet file can carry per-directory or per-module floors in place of a single global value, allowing different enforcement thresholds for different parts of the codebase.

## The Audit Value

A checked-in ratchet file that is updated on every merge creates a historical record of quality improvement over time. The git history of the ratchet file shows when each metric improved, how quickly, and implicitly correlates with the work that produced each improvement.

For teams that need to demonstrate quality trends to stakeholders, engineering leadership, security reviewers, compliance auditors, this history is more useful than point-in-time snapshots because it shows direction and velocity in addition to current state.

## Limitations and Tradeoffs

The ratchet works well for metrics that can be objectively measured and aggregated. It is less useful for quality properties that are harder to quantify: code clarity, architectural coherence, API design quality. These matter, and the ratchet does not address them. Human review remains important for the qualitative dimensions.

There is also a category of legitimate regression that the ratchet can mishandle: intentional removal of code that happens to remove covered lines, bringing down the coverage percentage even though the removal was the right architectural decision. The right response is usually a manual floor update with an explanatory commit message, and that deserves a team norm, so the floor update does not become a way to silently bypass the gate on regressions that were not intentional.

The ratchet is only as useful as the metrics it enforces, and Goodhart's law applies in full: when a measure becomes a target, it stops being a good measure. A high coverage percentage is not the same as good tests. A low lint error count is not the same as readable code. The ratchet enforces the floor on the things you choose to measure, which makes the choice of what to measure a consequential decision.
