---
type: Reference
title: "The Review Bottleneck in AI-Assisted Delivery"
resource: "https://www.devlinliles.com/the-review-bottleneck-nobody-talks-about/"
author: "Devlin Liles"
published: '2026-07-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

AI coding tools made generation fast. Review stayed slow. That asymmetry now gates delivery velocity in most teams that adopted AI without redesigning how code gets evaluated, and it gets far less attention than the generation side of the story.

The math is simple. An AI agent generates a feature implementation in fifteen minutes. A human reviewer needs two hours to evaluate it properly: reading the code, understanding the architectural implications, checking for security concerns, verifying test coverage, confirming alignment with requirements. The team's effective throughput is gated by review capacity. They bought a machine that outputs at 10x and plugged it into a review process designed for 1x.

This is an old pattern in new clothes. Eliyahu Goldratt built the Theory of Constraints on the observation that improving a non-bottleneck resource does nothing for system throughput. Speed up one stage of a pipeline and the constraint moves downstream. Generation was never the constraint in software delivery. Verification was. AI made that visible by making generation nearly free.

## The Attention Tax

Code review was already the most cognitively expensive part of the development lifecycle. Michael Fagan formalized software inspection at IBM in 1976, and the practice has carried the same economics ever since: inspection catches defects cheaply relative to production, and it pays for that by spending the scarcest resource in the building, senior engineering attention. Herbert Simon named the underlying law in 1971: a wealth of information creates a poverty of attention. AI-assisted development is the cleanest demonstration of that line I have seen in my career.

Before AI, a senior developer reviewing a peer's pull request was evaluating code written by someone who thought about it, made deliberate choices, and could explain the reasoning behind any line. The reviewer's job was to catch what the author missed. AI-generated code inverts this. The reviewer is evaluating code written by a system that does not hold intent the way a human author does. The patterns might be unfamiliar. The dependency choices might be unconventional. The architectural decisions might be locally rational and globally incoherent. The reviewer is reverse-engineering whether the generated code fits a mental model of the system that only the human team holds.

Volume compounds the problem. More AI-generated PRs means more attention tax per day. Reviewers start rubber-stamping. They skim. They approve when tests pass, without asking whether the implementation is sound. The review process degrades invisibly, and the cost shows up weeks later in production incidents and the kind of architectural drift that accumulates until the system becomes hard to change.

By the 90-day mark, teams report approval times longer than they were before AI adoption. Generation got faster. Delivery got slower. The bottleneck moved from writing to evaluating.

## Permission Mode's Hidden Cost

There is a structural version of this problem that hits teams trying to maintain human oversight of AI agents. I call it permission mode: the agent proposes an action, the human approves it, the agent proceeds. This is the default operating model for most AI-assisted development today.

Permission mode feels safe because a human is in the loop. The reality is that the human becomes a throughput constraint that scales linearly while the agents scale with compute. One developer overseeing one agent can provide meaningful review. One developer overseeing three agents is context-switching between unrelated implementations. One developer overseeing ten agents is approving things they have not evaluated.

The usual responses are to hire more reviewers or to reduce review requirements. Both miss the point. More reviewers is a linear scaling strategy for a generation curve that is anything but linear. Reduced requirements is accepting higher defect rates with extra steps. The workable answer moves review from a human activity to a system activity, with humans reviewing the system's output one level up.

## Review as a Pipeline Stage

The teams solving this are converging on the same architecture. Review becomes a pipeline stage staffed by specialized evaluation agents. When code completes generation, it flows through parallel review processes. A security scanner evaluates vulnerabilities and dependency risks against defined rules and known vulnerability databases. A QA validator checks test coverage against documented requirements. An architecture checker tests for boundary violations against system patterns. A performance profiler evaluates resource usage characteristics.

Each review agent has defined criteria and a quality threshold. The implementation passes or fails each checkpoint without a human spending attention on it. The results are synthesized into a structured report of what each specialist perspective found, what passed, and what needs attention.

The human reviews the summary. That is a different cognitive task. Reading a structured quality report takes minutes. The human's job shifts from understanding every line to judging whether the automated review caught the right things, and making calls on items that need human context. That process scales with generation speed because the expensive part, multi-perspective evaluation, happens at machine speed.

The shift is from watching the code stream to reviewing outcomes. From permission mode to governance mode. The human operates at a different altitude, making the calls that require business context, stakeholder knowledge, and strategic awareness, while specialized agents handle the technical evaluation that was eating their attention.

## The Business Cost

The review bottleneck translates directly to delivery velocity. If you generate code at 3x speed and review at 1.2x speed, effective throughput scales by about 1.5x, nowhere near what the AI investment promised. Release cadence suffers. Time-to-market commitments that depended on acceleration slip. The ROI conversation with leadership becomes painful: we spent this much on AI tools and we still ship at the old speed, we are just tired.

Senior developers feel it differently. Fifteen years of experience and careful judgment become attention tax. They wanted AI to eliminate the grunt work, and it manufactured a new kind: reviewing generated code faster and with less mental energy, which means approving without fully understanding. Teams that keep the old review structure watch senior retention drop. The work is infinite and uninteresting, and senior people leave work like that.

Quality follows the same curve. Hidden defects that should have been caught in review surface in production two or three abstraction levels away from the original implementation, where they are exponentially more expensive to fix. Teams that move to pipeline review address all three at once: delivery accelerates, senior developers return to work that requires judgment, and evaluation stays consistent because it no longer degrades with attention fatigue.

## Trust Calibration

None of this works on day one. You cannot delegate human review to agent review until the agent review has earned trust, and trust is earned through demonstrated accuracy over time.

The practical path is progressive delegation. Run the agent review pipeline in parallel with human review and compare results. When the security agent catches the same issues the human reviewer catches, plus issues the human missed, you start trusting its assessment. When the architecture agent consistently flags the same boundary violations the senior architect flags, you delegate that evaluation to run continuously while the human spot-checks. Each calibration point moves one concern from human-must-evaluate to agent-evaluates-human-spot-checks. Over months, the human's review scope narrows to the things that require human judgment: business alignment, strategic tradeoffs, novel architectural decisions.

Research from MIT Sloan backs this up: human-AI collaboration achieves 94 percent success rates when governance infrastructure is in place. Full autonomy without human oversight drops to 73 percent. The optimal point is elevation. Humans on the decisions that require judgment, agents on the evaluation that requires consistency.

## Where the Argument Could Break

Three objections deserve a serious answer.

The first is correlated failure. If a language model generated the code, a language model reviewing it may share the same blind spots, the way two copies of the same compiler miss the same bugs. This is the strongest objection, and it shapes the design. The pipeline leans on deterministic tools where they exist (static analysis, dependency scanners, coverage measurement), uses evaluation agents with distinct criteria and contexts, and keeps human spot-checks permanently in place. Diversity of evaluators is the defense, the same logic that motivated N-version programming in fault-tolerant systems.

The second is history. Automated review is decades old, lint dates to Bell Labs in the late 1970s, and static analysis never displaced human review. True, and the older tools were never asked to. They checked syntax-level properties. The current generation evaluates semantics, architectural conformance, and test adequacy. Automation's job here is to absorb the attention tax so human judgment gets spent where it pays.

The third is accountability. Someone has to own the approval, and "the pipeline passed" is a thin defense in an incident review. Agreed. Governance mode keeps a named human approving every release. What changes is the evidence behind the approval: a structured, multi-perspective report in place of a fatigued skim of ten thousand generated lines. The approval gets stronger, because it rests on evidence.

The review bottleneck is fixed by reviewing differently, at a different altitude. If your team is drowning in AI-generated PRs, the first move is to identify which review concerns can be expressed as automated criteria. Security checks have defined rules. Architecture boundaries have defined patterns. Test coverage has defined thresholds. Every one of those can be evaluated by an automated agent, which frees the human reviewer for the question automation cannot answer: whether this implementation solves the right problem for the right reasons.

Generation speed is a gift. The review process is where you unwrap it or let it pile up unopened. Teams that redesign review for AI speed deliver the value AI generation promises. Teams that keep reviewing at human speed deliver frustration.
