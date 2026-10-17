---
type: Reference
title: "The Compression Cliff Nobody Budgeted For"
resource: "https://www.devlinliles.com/the-compression-cliff-nobody-budgeted-for/"
author: "Devlin Liles"
published: '2026-09-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I watched a team ship a prompt-compression pass to cut token costs, high-five over the invoice drop, then spend the next sprint chasing tool calls that stopped executing in production. They had done the math on tokens. Nobody had done the math on where the agent's instructions stop being enough instructions to actually run the agent.

The assumption behind that kind of pass is almost always the same one: cut the system prompt by a third, expect to give up something like a third of your reliability margin in exchange. Smooth in, smooth out.

Hou and Yang's paper on tool-using agents under compression describes a different shape entirely. Reliability holds close to flat as instructions get trimmed, right up until it doesn't. Past some threshold specific to the task, the tool-calling success rate falls off fast. Compression behaves like a cliff.

Token cost is a linear quantity, so it's natural to borrow that intuition for everything else getting cut. Every word removed takes an equal bite out of the invoice, and the mind assumes an equal bite comes out of performance too. Tool calling doesn't run on that kind of curve. A call either matches the schema or it doesn't. The argument is the right type in the right field, or the call fails. That's a threshold property, governed by whether the model retains enough of the tool definition to reproduce it exactly. It doesn't turn down smoothly as words disappear the way a quality dial would.

The instructions that look safest to remove are usually the repeated ones: the schema stated once in the tool definition and restated in the system prompt, the constraint spelled out twice, the worked example that reads as redundant once the model has demonstrated it "gets it" earlier in the conversation. A compression pass built to shrink token count treats exactly this material as the fat to trim. That redundancy is what lets the model regenerate precise call syntax when the conversation has drifted, when five other instructions are competing for attention, when the easy path is to approximate instead of match exactly. Removing it once rarely breaks anything. Removing enough of it means the model is reconstructing the schema from a rough memory of having seen it, and a rough memory is exactly where exact-match formatting comes apart.

The reason this stays invisible until a team has already crossed it is a measurement problem. Compression benchmarks mostly score two things: whether the shortened text still reads well, and whether the end-to-end task got completed. Both of those can survive real damage to argument precision, because a model can narrate a plausible attempt at a task even when the underlying tool call came back malformed and got quietly retried or dropped. The transcript still reads coherent. The dashboard still shows a completed task. Nobody is tracking the raw rate of malformed tool calls, so nobody sees the frontier they're approaching until they've already crossed it and the retries stop covering for them.

"Control under compression" names the actual question better than "how small can we make this prompt." The real question is how much compression a specific tool-calling task can absorb before the model loses the precision that exact execution demands, and that ceiling moves with the task. A two-argument API call tolerates more trimming than a twelve-field form. One tool tolerates more than ten competing for the model's attention in the same turn. A single spot check, run at whatever compression level someone happened to test, can land comfortably on the flat part of that curve and say nothing about how close the edge is.

Testing for that requires the same discipline as any frontier: run reliability against compression across the range a system will actually see in production, find where the curve bends, and treat that bend as the real constraint on the budget, not the invoice total. The team I watched didn't make a bad call shipping the compression pass. They tracked the number that was easy to track and stopped one measurement short of the one that mattered.
