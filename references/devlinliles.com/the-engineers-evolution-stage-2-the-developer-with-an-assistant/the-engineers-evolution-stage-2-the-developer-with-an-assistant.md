---
type: Reference
title: "The Engineer&#x27;s Evolution, Stage 2: The Developer With an Assistant"
resource: "https://www.devlinliles.com/the-engineers-evolution-stage-2-the-developer-with-an-assistant/"
author: "Devlin Liles"
published: '2026-06-24'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Engineer's Evolution, Stage 2: The Developer With an Assistant

*Part 1 of a series on how the software engineer's role changes as teams climb the AI maturity curve. Each post takes one stage and follows two example careers through it: a software developer and a QA engineer.*

---

Engineering leaders keep asking a version of the same question. As teams adopt AI, how does the software engineer's role actually change, and what should we expect of developers and testers at each step. The answer is encouraging and it runs against the popular fear. The role does not shrink. It expands. Engineers keep their development depth, gain far more design and architecture range, and add a new discipline on top: building the systems that produce and verify software at speed.

This series walks that growth one stage at a time. We use an eight-stage maturity model, and the early stages share a common goal: do the work you already do, faster and better, without tearing up your process. The later stages change how the work itself is structured. Most of the industry sits at Stage 2 right now. Public workforce data shows only about a third of technology workers use AI daily, and a much smaller fraction use it on work they would be held accountable for. The real prize for most teams is a clean run from Stage 2 to a mature Stage 4.

Before we get into the day to day, hold two ideas in your head. They explain every change that follows.

The first is that design and judgment grow on top of coding. The coding stays. As an engineer climbs, they start designing the systems that do the work and deciding where human judgment is required. The engineer who designs a workflow still reads, writes, and debugs the code underneath it, because that is what lets them catch when the system is wrong. The skill that matters most becomes critical thinking: defining what good looks like, anticipating edge cases, and recognizing when an agent has produced something plausible and wrong.

The second is that engineers move from using the tools to building the tools. At Stage 2 they consume off-the-shelf AI. From Stage 3 onward they increasingly build and maintain the machine that produces the software: the task agents, the skills that encode how work is done, the gates that catch mistakes, and the pipeline plumbing that ties it together. A growing share of engineering effort shifts from writing the product to writing the machine that writes the product.

Keep those two shifts in mind. Now let's look at where almost everyone starts.

## Stage 2: Off the Shelf

Stage 2 is the world most engineering teams live in today. An engineer has a capable AI assistant available, and they reach for it when it helps. The tooling is impressive. The workflow around it has barely changed.

### The developer's day

The developer works in the IDE the same way they always have. When a task gets repetitive or unfamiliar, they ask the assistant for help. Draft this function. Explain this block of legacy code. Write a first pass at a test. They read the suggestion, decide in the moment whether it is good, and accept it or throw it away. When the output drifts off course, they re-prompt and try again.

The gains are real and they are uneven. One prompt produces something clean. The next produces something confidently wrong that takes longer to fix than it would have taken to write. The developer absorbs that variance with their own judgment, re-prompting and reworking until the result is acceptable. The whole loop lives inside one person's head. Nothing is captured. Nothing is shared. The next developer who hits the same problem starts from zero.

So the day still looks like a developer's day. Mostly typing, with an assistant alongside. The load-bearing skill is still the craft itself: solid coding fundamentals, fast judgment of whether a suggestion is any good, and enough fluency to iterate on a prompt without losing the thread. The assistant speeds up the typing. It does not yet change the job.

### The tester's day

QA looks much the same. The tester reaches for an off-the-shelf tool to draft test cases or a script faster than writing them cold. Testing still happens after development, by hand, with the tool accelerating the keystrokes. The thinking is still the tester's. Results are inconsistent in the same way the developer's are, and nothing gets captured for reuse.

The skills that carry the work are unchanged: test case design, scripting fluency, and the ability to read the system under test and the requirements closely enough to know what to check. The tool helps the tester produce a draft. The tester still owns the design.

## What Stage 2 is really worth, and where it caps out

Stage 2 delivers a real productivity bump, and it is the right place to start. People build comfort with the tools, develop intuition for where the assistant is strong and where it lies, and learn to spot a plausible-but-wrong answer. That intuition is the raw material every later stage is built from.

The ceiling is structural. Every gain at Stage 2 is personal and ephemeral. Because nothing is encoded, the team cannot compound its learning. Two developers solving the same class of problem reach two different levels of quality, and neither one's insight survives the week. The variance that the assistant introduces gets absorbed by human attention, which means the faster you go, the more attention you spend catching mistakes. There is a real limit to how far a team can scale that way.

The main risk at Stage 2 is quiet: inconsistent output that looks fine in the moment and accumulates into drift over time. There is no system watching for it. There is only the individual, and the individual is busy.

## The move that matters

The jump that separates the stages is judgment. Stage 2 hands an engineer a powerful assistant and asks them to keep working the old way. Stage 3 asks them to do something different in kind: to write down how they work, encode their standards into agents the team can share, and step back from the keyboard to direct and review instead of type. That is where the role visibly starts to change, and it is where the next post picks up.

For now, the takeaway for engineering leaders is simple. If your team is at Stage 2, you are not behind, you are where most of the industry is. The opportunity is helping your engineers make the metacognitive shift from doing the work to designing how the work gets done. A better assistant will not buy that shift. That shift is the whole game, and we will spend the rest of this series unpacking it.

*Next in the series: Stage 3, where the developer becomes a director and reviewer, and the tester becomes a test designer.*
