---
type: Reference
title: "The 503 That Kept a Chat Interface Honest"
resource: "https://www.devlinliles.com/the-503-that-kept-a-chat-interface-honest/"
author: "Devlin Liles"
published: '2026-10-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I gave myself two weeks to build an internal benefits assistant for a company's employees. I called it PolicyBot, because naming a pilot project is the one part of this job that never gets harder. The ask was simple: let an employee ask about PTO accrual or dependent coverage and get a real answer, pulled from the company's actual current policy documents. Two weeks is not enough time to build a retrieval pipeline, validate it, wire up orchestration, and stand up an audit log. Under that pressure I made the call that always feels reasonable in the moment: build the chat interface first, since that's the part anyone reviewing the demo will actually look at.

I wired a chat surface directly to an LLM call. Retrieval was stubbed to one hardcoded snippet, the same snippet no matter what question came in. Nothing checked whether that snippet actually answered the question being asked. Nothing logged which source fed which answer. None of that showed up in the demo, because none of it had to. The interface looked like a finished product. It answered fluently. It answered instantly. Underneath it sat a single database table holding twenty real benefits policies, and not one of them ever got queried.

I ran a twenty-question benefits test set against this version and watched the failure show up as a number, not just a hunch. The metric was grounded-answer rate: the percentage of answers that actually cited a real, current policy from the seeded database rather than a hardcoded stand-in or something the model quietly filled in from its own training data. I set the target low on purpose, below 40 percent, so the failure would be impossible to argue with. It landed there anyway, nowhere close to a rounding error. Most of what a confident-sounding chat interface told an employee about their own benefits had nothing real underneath it.

## The pattern

The fix is a build-order rule enforced by a gate the endpoint itself checks, at request time, every time. A readiness check runs three things before the chat endpoint is allowed to answer anyone: retrieval-grounding accuracy, orchestration validation coverage, and audit-log completeness, each measured against a defined threshold. Until all three clear their bar, the chat endpoint returns a 503. The interface doesn't get to exist yet if what it would say isn't backed by something already proven to work.

I rebuilt PolicyBot against the identical scenario and the identical twenty-policy database, and the only thing that changed was the order things got built in. Retrieval genuinely queried the database this time, using a real similarity and keyword lookup instead of a hardcoded stand-in. An orchestration step checked that the retrieved snippet actually addressed the question before generation ever ran. Every answer wrote to a real audit log with its source attached. A readiness script ran all three checks and only then unlocked the endpoint. Same twenty-question test set, same grounded-answer-rate metric, but this time the target was 85 percent, and it cleared. The model behind the answers stayed exactly what it always was. What changed was everything feeding it.

The mechanism underneath this is a sequencing rule, stated plainly: identity, data, and orchestration get proven before the interface goes live, because those are the layers that make an interface's confidence honest instead of decorative. A response that collapses a multi-step pipeline into one flat verdict presents certainty that never got checked. A session that survives on a sticky connection presents continuity that doesn't exist. An interface that's allowed to answer before anything underneath it has been proven presents competence it hasn't earned yet. Gating the endpoint behind a readiness check is the plainest version of refusing to let that kind of overstatement happen by default, because the endpoint simply cannot answer until the check passes.

## Design considerations

This pattern closes one specific gap: the distance between what I've actually built and what my interface claims to be presenting. It stops right there. It has no opinion on whether the underlying layers, once proven, are proven to a standard that actually matters for the domain they serve. A retrieval accuracy threshold set too low still clears the gate and still ships a confidently wrong interface, just a slightly less wrong one than before. The gate enforces sequencing discipline. Setting the bar that sequence has to clear is a separate decision, made by whoever owns the risk, and I could just as easily set that bar low enough to hit a two-week deadline anyway, under the exact pressure that produced PolicyBot's first version.

There's a real cost to this discipline, and it shows up at the worst possible moment: right at the deadline. A team staring at a two-week demo window and a 503 where a chat bubble should be feels genuine pressure to loosen the threshold rather than move the date. That pressure is exactly why the check has to live in the endpoint itself rather than in a manual step someone remembers to run before a demo. A threshold that can be quietly adjusted under deadline pressure has already failed at the one job a gate exists to do: holding still regardless of the calendar.

The three checks I picked for PolicyBot, retrieval accuracy, orchestration validation, audit completeness, were the right three for a benefits chatbot pulling from a fixed policy database. They won't be the right three for every application. A system where retrieval barely matters but tool-calling carries most of the actual risk needs gates measuring something else entirely. Copying my three checks wholesale into a system whose risk sits somewhere different adds ceremony without adding safety. The mechanism worth keeping is the discipline itself: refuse to let the interface answer until the layers underneath it clear a threshold someone deliberately set. Deciding which thresholds actually matter for a given system is the harder, more specific judgment call, and it's the part of this pattern that has to be redone for every application rather than inherited from the last one.

What this pattern buys me, concretely, is a demo date that tells the truth. PolicyBot's first version hit its two-week deadline and lied about what it could do the moment anyone asked it a real question. The gated version either hits the deadline honestly or it misses the deadline visibly, with a 503 standing in for whatever wasn't actually ready. I would rather explain a missed date than watch an employee trust a benefits answer that came from nowhere.
