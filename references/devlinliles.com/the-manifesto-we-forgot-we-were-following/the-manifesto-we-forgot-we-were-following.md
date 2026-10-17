---
type: Reference
title: "The Manifesto We Forgot We Were Following"
resource: "https://www.devlinliles.com/the-manifesto-we-forgot-we-were-following/"
author: "Devlin Liles"
published: '2026-06-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2013, I defined technical debt as "the eventual consequence of continually trading craftsmanship for short-term velocity." The key word was *continually*: the normalization of the shortcut until the shortcut becomes the standard. A single pragmatic tradeoff is just engineering. The pattern is the debt.

In 2026, I am making nearly the same observation about how organizations relate to the Agile Manifesto. We have been following it for so long that we have forgotten what it was a response to, and we now treat the trade-offs it articulated as timeless principles. They were context-specific responses.

The result is organizational technical debt of a different kind.

## The Debt We Carry

The seventeen authors who met at Snowbird in 2001 were reacting to something specific: document-driven, heavyweight, plan-everything-first processes that had buried working software under process artifacts. The Manifesto's four values are formulated as trade-offs because the constraint of the era was scarce human execution capacity, and every hour spent on the right side of an "over" was an hour unavailable to the left. In 2001, that constraint was real and binding. The trade-offs were correct.

The authors also hedged, in the text itself: "while there is value in the items on the right, we value the items on the left more." The "over" was a weighting. Twenty-five years of practice turned it into an instead-of. Organizations that adopted Agile between 2001 and 2015 built processes, cultures, and mental models around the harder reading, and the "over" formulations became embedded assumptions:

- Documentation is overhead. Working software is what matters.
- Detailed plans are a waste. Responding to change is what matters.
- Processes and tools constrain people. Individuals and interactions are what matter.

Each was a defensible position in 2001. Each is a dangerous default in 2026, where AI removes the constraint that made the trade-offs necessary.

Consider the team that defaults to "we don't have time for thorough documentation" in a context where AI can maintain documentation from code and conversations. Their code is difficult to onboard, difficult to audit, and vulnerable to knowledge loss. That team has accumulated Manifesto debt. They are applying Constraint Era practices in a Synergy Era context and producing outcomes worse than they should be. The Agile values held; the context changed and the practices did not.

## The Parallel

Ward Cunningham coined the debt metaphor in 1992 to describe how reasonable shortcuts compound when they go unaddressed. The mechanism is normalization. "We don't test this module" becomes "we don't test this area" becomes "we mostly skip tests on legacy code" becomes an undocumented policy that new team members inherit without understanding the history.

Manifesto misapplication normalizes the same way. "We deprioritized documentation on that project" becomes "our team moves fast and doesn't do docs" becomes a cultural identity that blocks the adoption of AI-native practices that could produce both speed *and* documentation.

The fix, in both cases, is the same: name the pattern. Stop calling it pragmatism. Identify what the original tradeoff was responding to, ask whether that constraint still applies, and make a conscious decision about whether the practice is still appropriate or whether it is now producing worse outcomes than the alternative.

## What the Manifesto Actually Says

Read by intent, the values are statements about what the authors valued most and why. The trade-off framing was the packaging.

They valued *individuals and interactions* because they had seen processes and tools used as substitutes for competent, collaborative people. The target was processes-without-people, a failure mode, never processes as such.

They valued *working software* because they had seen documentation produced in place of software. The target was documentation-without-software, the same shape of failure, never documentation as such.

The intent is competence, collaboration, outcomes, adaptability. The formulation is context-specific.

The P.O.S.T. reformulation restores the intent: Individuals & Interactions *times* Processes & Tools equals Productivity. Working Software *times* Comprehensive Documentation equals Outcomes. The values are the same. The math is different.

## Where the Argument Could Break

One objection says there is no debt, only misreading: the authors themselves wrote that the items on the right have value, so the Manifesto needs no reinterpretation. Correct about the text, and beside the point about the practice. Organizations run on practice, and a correct document misapplied for twenty-five years leaves the same accumulated interest as a wrong one. The debt lives in the defaults teams inherit, and those defaults are what have to be named and paid down.

A second objection cuts at my documentation example: AI-maintained documentation could recreate the 2001 failure mode at zero marginal cost, mountains of generated text that nobody reads and nobody trusts. This is a real risk, and the answer lives in the direction of the dependency. The failure the Manifesto's authors saw was documentation produced in place of software. Documentation derived from working software inverts that relationship, and it needs the same quality gates as any other AI output. Generated text without gates is slop, and slop is just debt with better formatting.

A third objection holds that the constraint never lifted, it moved: human judgment and review capacity are now the scarce resource, so trade-offs survive in a new form. I agree, and that is the point. The trade-offs need reformulating around judgment allocation, which is exactly what the P.O.S.T. framing does. What cannot survive is running the 2001 trade-offs against a constraint that no longer binds.

Organizations that make this shift are abandoning nothing. They are practicing Agile more faithfully, closer to the intent, than the organizations still trading off values that AI has made simultaneously achievable.
