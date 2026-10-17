---
type: Reference
title: "Technical Debt Is a Chronic Condition, Not a Single Decision"
resource: "https://www.devlinliles.com/technical-debt-is-a-chronic-condition-not-a-single-decision/"
author: "Devlin Liles"
published: '2026-07-11'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most important word in my definition of technical debt is one that almost never appears in anyone else's definition.

*Continually.*

Technical debt is "the eventual consequence of *continually* trading craftsmanship for short-term velocity."

Not once. Not occasionally. Continually.

## Why the Word Matters

Ward Cunningham, who coined the metaphor, meant it as a single, deliberate choice: ship something you know isn't quite right, document the gap, pay it back later. That is a reasonable engineering tradeoff. It happens. It can be managed.

What I observed in teams was something different. The tradeoff wasn't being made once and documented. It was being made every sprint, by default, without discussion, because there was never a sprint where the deadline gave you room to do it right. The debt was not a conscious choice; it was the output of a process that had no mechanism for making a different choice.

That is a chronic condition. And chronic conditions require different treatment than acute ones.

## The Accumulation Model

A single decision to skip tests on a module is recoverable. You go back, you write the tests, you move on. The cost is an afternoon.

A year of making that decision, every sprint, on every module? The cost is a codebase where nobody understands the dependencies, where every change is a controlled explosion, where the team's entire velocity is consumed by managing the consequences of previous decisions. The cost is not additive — it compounds.

This is why "we'll pay it back later" almost never happens. The debt is not a discrete item on the backlog. It is distributed through thousands of small decisions that each seemed reasonable at the time, and it is now woven into the structure of the system itself.

## The Root is Behavioral, Not Technical

Here is the reframe that matters: technical debt is a behavioral problem with technical symptoms.

The technical symptoms are visible and measurable: slow builds, fragile tests, undocumented interfaces, high defect rates, velocity that declines quarter over quarter. Those are real, and they hurt.

But the root cause is behavioral: a team that has normalized the tradeoff. A team where "we'll do it properly next sprint" has become the default closing statement for every "we should probably..." conversation.

You cannot fix a behavioral problem with technical solutions. You can refactor the codebase, but if you don't change the pattern of decision-making that produced it, the new codebase will accumulate the same debt.

The fix is cultural. It requires a team that treats quality as non-negotiable — not as a luxury to be added after the features are shipped, but as a constraint on how features get built. This is the craftsman's position: professional standards are not a line item that gets cut when the sprint is full.

## What This Looks Like in Practice

In practical terms, the chronic debt pattern tends to look like this:

**Symptom:** "We're going to be a little light on test coverage for this feature." Heard weekly. Across all features.

**Intervention:** Stop. Name the pattern. "We have said that fourteen times this quarter. We are not light on test coverage for this feature — we have decided not to write tests, and we have made that decision repeatedly." Naming it as a recurring choice rather than a situational tradeoff is the first step toward making a different choice.

**Alternative:** Define the team's non-negotiable standards explicitly, before the sprint starts. Not "we prefer tests" but "we do not ship code without tests." The definition of done is a technical debt prevention mechanism, not a process artifact.

## Debt and the AI Era

I have been asked whether AI changes this conversation. The short answer: it escalates it.

AI-assisted development can write code faster than a human. That is genuinely useful. It also means that teams without quality standards can now accumulate technical debt at a much faster rate. The bottleneck on debt accumulation is no longer how quickly humans can write code. If your process has no quality gates, AI removes the last natural governor on how fast the debt grows.

The craftsman's standards become *more* important in an AI-assisted environment, not less. The question "is this right?" needs to be asked before the AI writes the code (in the prompt), during the generation (in the review), and after it's integrated (in the tests). The habit of quality does not automate.

---

*Part of the *[*Thought Leadership series*](../Topic%20Progression.md)* — Thread 1: People, Culture & Organizational Systems.* *Related: [[T01-software-craftsmanship-as-identity]], [[T03-automation-as-professional-obligation]], [[X05-technical-debt-meets-post-ai]]*
