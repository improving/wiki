---
type: Reference
title: "94 Percent Confidence, Exact Match, Auto-Resolved"
resource: "https://www.devlinliles.com/94-percent-confidence-exact-match-auto-resolved/"
author: "Devlin Liles"
published: '2026-10-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built an IT service-desk agent that auto-remediates common Intune-managed endpoint issues: a password reset, a license reassignment, a compliance-policy re-push. No ticket, no human in the loop, when the agent has enough evidence to act on its own. When it doesn't, it escalates to a technician. That split, autonomous action or human review, is the entire product. The question I hadn't answered was what the user actually gets to see once the agent has made that call.

The answer, in the first version, was almost nothing. A user or technician saw "resolved automatically" or "escalated for review." That's it. No confidence score, no evidence, no sense of how close a given decision came to the line between the two outcomes. The agent computed a confidence number internally on every single ticket. It just never told anyone what that number was.

I ran forty synthetic tickets through this version, thirty clear-cut and ten built deliberately near the auto-versus-escalate threshold. The clear-cut tickets behaved the way you'd hope. The borderline ten are where the silence cost something real. A device with a partially matching compliance signature, close enough to the threshold that a person looking at the actual number would have flagged it as a coin flip, got auto-resolved with the same flat "resolved automatically" label as a device with an exact match. I measured borderline-error rate, the share of those ten near-threshold tickets that resolved incorrectly with no flag that they'd been close calls, and it came in above 40 percent. Four times out of ten, on exactly the tickets where a close call mattered most, nobody had any way of knowing it had been close at all.

## The pattern

The fix disclosed the confidence score and the specific evidence behind every action, not after a complaint, on every single decision. "Auto-resolved: 94 percent confidence, compliance signature exact match." "Escalated: 61 percent confidence, partial signature match, below the 80 percent autonomy threshold." Same two outcomes as before. The difference is that the number and the reason are now sitting right next to the label instead of hidden behind it.

Borderline cases get visibly flagged as close calls instead of looking identical to the clear-cut ones. Once that's in place, every ticket discloses its basis, and the technician looking at the borderline cases can tell, at a glance, which ten out of forty deserve a second look before anyone trusts the label attached to them. The mechanism costs almost nothing technically. The confidence number already existed inside the model. The only thing that changed is whether it ever reached a human.

What this actually buys is the difference between trusting a system on faith and trusting it on evidence you can inspect. "Resolved automatically" asks for faith. "94 percent confidence, exact match" gives you something to check your own judgment against, case by case, instead of a binary label standing in for a decision you can't see the inside of.

This is the sliver of a much bigger governance gap that outside research keeps flagging as the weakest point in how organizations manage autonomous systems right now. McKinsey's 2026 AI Trust Maturity Survey scores organizations across five responsible-AI dimensions, and the newest one, added specifically because staged, evidence-gated maturity assessment applied to autonomy is now its own axis, is "agentic AI governance and controls." It's also the lowest-scoring of the five, with only around 30 percent of organizations reaching maturity level 3 or higher on it, and nearly two-thirds of respondents cite security or risk concerns, not regulation and not technical limitations, as the top barrier to scaling agentic AI at all. Disclosing a confidence score doesn't solve agentic governance broadly. It closes exactly the sliver of it that reduces to "the user couldn't tell how close to the line this decision was."

## Design considerations

Disclosure and calibration are two different claims, and conflating them is the single easiest way to oversell this pattern. Showing a confidence number builds trust in the process of showing it. It says nothing about whether the number itself deserves that trust. A badly calibrated model can report 94 percent confidence on a wrong answer exactly as readily as on a right one, and a disclosure mechanism with no calibration check sitting behind it risks becoming transparency theater: a confident-looking figure that isn't actually reliable about how often it's wrong. Disclosing the number is necessary. It's not sufficient, and I'd rather say that plainly than let a well-labeled wrong answer pass as a solved problem.

There's a real tension between disclosure and usability that shows up fast at volume. Forty tickets a day, every one carrying a confidence score and an evidence snippet, is a genuine improvement over a blank label. Four thousand tickets a day, every one carrying the same disclosure, risks becoming exactly the kind of noise a technician learns to stop reading. Disclosure earns its keep specifically on the decisions where a person might actually act on the information, which in practice means weighting attention toward the borderline cases rather than treating every ticket, clear-cut or not, as equally worth a technician's eyes.

The threshold itself is a policy decision this pattern doesn't make for you. Eighty percent confidence as the autonomy line is a number somebody chose, not a number the mechanism derived. Move that line and the same disclosure format keeps working exactly as before, faithfully reporting whatever threshold got set, with no opinion on whether 80 percent was the right place to draw it for this specific class of remediation. Getting the threshold right is a separate, harder conversation, usually involving whoever owns the cost of a wrong auto-resolution against the cost of an unnecessary escalation, and no amount of clean disclosure formatting substitutes for having that conversation honestly.
