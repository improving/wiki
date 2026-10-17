---
type: Reference
title: "The Machine Is Learning to Build Itself. You Still Have to Decide What to Build."
resource: "https://www.devlinliles.com/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build/"
author: "Devlin Liles"
published: '2026-07-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Anthropic just published the clearest data we have on what happens when AI starts building AI. The headline number is hard to ignore: their engineers now ship roughly eight times as much code per quarter as they did across 2021 through 2025, and more than 80% of the code merged into their codebase is written by Claude. A class of API errors that would have taken a human four years to grind through got fixed in a month. An optimization task that a skilled researcher reaches a 4x speedup on in a full workday, the model now reaches 52x.

Read that as a fire alarm and you will make bad decisions. Read it as a map and you will make good ones. The piece is really a story about which work moves to the machine, which work stays with the human, and the order those handoffs happen in. That order is the thing we have been teaching clients for the last year. We call it the eight-stage AI maturity model, and Anthropic's own trajectory is the cleanest case study of it I have seen.

## The model, in one paragraph

Maturity is not how good your tools are. It is how much of your work you can responsibly hand off, and how well you catch what goes wrong when you do. The progression runs eight stages. Stage 1 is Zero AI, where you know the tools exist but nothing touches a deliverable. Stage 2 is Off the Shelf, using Copilot, Claude, and Windsurf as-is. Stage 3 is Task, where you stop typing one-off prompts and start giving AI defined work with real context, a written evaluation rubric, and a reusable prompt library. Stage 4 is Workflow, multi-step chains wrapped in deterministic validation, adversarial agents, governance rules, and human punch-out points. This is the first stage that requires the team and IT, not just an individual. Stage 5 is Delegate, handing off whole sub-tasks against clear success criteria. Stage 6 is Coordinate, multiple agents running in parallel on shared infrastructure with conflict arbitration. Stages 7 and 8, Supervise and Orchestrate, are aspirational today: continuously supervised systems and AI managing other AI. No production-grade playbooks exist for them yet.

![[eight-stage-staircase.png]]

The rule we hammer on: you cannot skip stages. A team that jumps from Stage 3 to Stage 5 doesn't go faster. It goes faster toward mistakes it can't see. The reason most organizations stall below Stage 4 is not tooling. It is that moving up the stack is less about doing the work faster and more about building the machinery to catch the errors that speed introduces. Every stage carries a counterfeit, the version that looks like progress and isn't. The counterfeit of Stage 4 is the sharpest: without runtime checking, the first bad step contaminates every step downstream.

## Anthropic is just a company climbing the same stairs

Strip away the frontier-lab mystique and Anthropic's timeline maps onto the model almost line for line.

Their 2021–2023 era, people writing code on laptops, is Stage 1 to 2. Early chatbots generating snippets to copy and paste is Stage 2, exactly where most of the industry still sits today. Coding agents that write and edit whole files is Stage 3 into 4. "Autonomous agents that run code themselves and delegate hours of work to other agents" is Stage 5 pushing into 6. And the future they name, agents that build and train the next model with humans supervising, is Stage 8 with the loop closed, the stage they themselves call out as not yet real.

The evidence they share is what each transition actually looks like from the inside. The 8x code jump didn't come from people typing faster. It came from Claude writing the code while the engineer directs and reviews. That is the Stage-3-to-4 signature: the human's hands leave the keyboard and move to the steering wheel. The detail that should land hardest for any leader is what broke when they sped up. Once code flowed faster through the org, human code review became the bottleneck. They had to stand up an automated Claude reviewer that now catches roughly a third of the bugs behind past production incidents before merge. That reviewer is a Stage 4 control: a deterministic gate standing between fast generation and the main branch.

That is the whole game. Amplification doesn't remove the bottleneck. It relocates it. The economists call it Amdahl's law and Anthropic names it directly: speeding up one part of a process just exposes the part you didn't speed up. Every client we move from Stage 3 to Stage 4 hits the same wall in the same place. Generation gets cheap, so review, governance, and judgment become the constraint. The organizations that win are the ones that see the new bottleneck coming and build for it before it bites.

![[bottleneck-shift.png]]

## AI will make a big difference. It is not magic.

Here is the part the headline numbers skip, and the reason the maturity model puts hard gates exactly where it does. AI agents are probabilistic. Every step has a chance of being wrong, and when you chain steps together, those chances multiply. End-to-end success is per-step reliability raised to the power of the number of steps. That exponent is brutal.

Picture an agent that gets each step right 95% of the time. In isolation that is excellent, the kind of number that makes a demo look magical. Chain twenty of those steps into one autonomous workflow and your odds of a clean run are 0.95 to the twentieth power, about 36%. Push it to fifty steps and you are at 8%. The agent did not get worse. You just asked it to be right more times in a row than the math allows.

![[compounding-reliability-curve.png]]

Raise the bar to 99% per step, genuinely hard to achieve, and the same fifty-step chain still only clears 60%. Drop to 90%, which still feels good in a single test, and a ten-step workflow is already a coin flip.

![[compounding-step-math-bars.png]]

This is why the success rate on a single shot tracks task length so cleanly. Trivial tasks are one or two steps, so they hold near the model's raw per-step reliability. Open-ended problems are long chains of dependent decisions, so they collapse toward the bottom of the curve. The longer and more autonomous the task, the more steps, and the more the compounding bites. The same data Anthropic shows internally, where open-ended success climbs but still trails the easy stuff, is this exact math playing out.

![[task-complexity-success.png]]

So what do you do about it? You do not wait for a perfect model. You break the chain. Every deterministic check, schema validation, and adversarial agent in Stage 4 is a place where one bad step gets caught and repaired before it poisons everything downstream. A gate that catches even 80% of errors at each step turns a chain that would have collapsed into one that holds. The model stays imperfect. The system around it stops compounding the imperfection.

![[validation-gate-effect.png]]

That is the entire reason Stage 4 is the hard wall, and the reason it is the first stage that demands team and IT standards rather than individual skill. Stages 1 through 3 are about getting good with the tool. Stage 4 is about engineering the system that makes an imperfect tool safe to trust at length. Skip it, and the 8x productivity story turns into an 8x cleanup story. The teams getting real leverage are not the ones with the best model. They are the ones who built the gates.

## Where the human stays, and why it isn't sentimental

The comfortable read of this story is that humans stay in the loop because we are special. That is not what the data says, and pretending otherwise will get a client hurt.

Here is the honest version. Anthropic's models have gone from helpful to superhuman at execution inside a defined problem. On running a well-specified experiment, they match or beat skilled researchers. On the squishy stuff we assumed was safe, they are climbing fast too: their best model now picks a better next research step than the human did 64% of the time in the cases they studied, up from 51% the prior November. The work that is genuinely still human is narrow and getting narrower. It is research taste and judgment. Choosing which problem is worth solving. Deciding which result to trust. Knowing when an approach is a dead end and killing it.

That is not a consolation prize. It is the highest-leverage work there is, and it is exactly the work the maturity model puts a human on at every stage. At stage 3 the human decides which opinions are worth codifying. At stage 4 the human sets the quality gates and decides what an exception even is. At stage 5 the human decides what is safe to stop watching. At stage 8 the human adjudicates the exceptions the swarm cannot. The doing collapses toward zero cost. The deciding does not. As the machine absorbs the perspiration, the value of good direction goes up, not down.

There is a real disagreement worth naming. Anthropic is candid that research taste might be just another capability AI fails at for a while and then masters, the way it eventually learned to explain why a joke is funny. They might be right. But even their conservative reading still implies compounding acceleration, because a human spending all their time on the small fraction of work that is direction-setting is steering vastly more output than before. You do not have to believe in full recursive self-improvement to act on this. You only have to believe that the cheap part is getting cheaper, which it observably is.

## What this means for you, specifically

If you are reading the 8x number and feeling behind, the right response is not to buy more licenses. It is to find out which stage your teams are actually on, because most are at Stage 2 and think they are further along. Daily tool use is not maturity. Codified, measured, gated workflows are.

Three things are true at once, and a real strategy holds all three. The amplification is real, and the teams capturing it are pulling away. The bottleneck always moves, so your next constraint is review, governance, and judgment, and that capacity has to be built before it breaks, not after. And the human role is shrinking in surface area while growing in leverage, which means the best people should spend less time producing and more time deciding.

The machine is learning to build itself. That is not the end of the human in the loop. It is the promotion of the human to the part of the loop that was always the point. The doing is getting cheap and imperfect at the same time, which is exactly why the gates and the judgment matter more, not less. The question Anthropic is asking inside their own walls is the one every leadership team should be asking inside theirs: when the doing is free, are we actually any good at deciding what to do?

---

*Sources: Anthropic Institute, "When AI builds itself" (anthropic.com/institute/recursive-self-improvement). Internal framing draws on Improving's eight-stage AI maturity model.*

---

## Notes for Devlin (not for publication)

- CTA removed per your note. Post now ends on the reflective question rather than a sales ask.
- Stage labels corrected to the canonical model from your State of AI deck (Stage 1 Zero AI through Stage 8 Orchestrate; 7-8 flagged aspirational). Earlier draft used a Stage 0 / placeholder version reconstructed from meeting notes.
- Added the compounding-error section ("AI will make a big difference. It is not magic.") with four visuals: the reliability curve, the step-math bars, the task-complexity chart, and the gate-effect chart. All charts are original (not Anthropic's). The task-complexity chart is labeled directional/illustrative since I built it to show the pattern, not exact published values.
- The math is standard: end-to-end success = p^n. The 80%-catch gate figure in the last chart is an illustrative assumption, not a measured number; swap in real eval data when you have it.
- All Anthropic figures are quoted as the article states them, with caveats intact (lines-of-code overstates productivity; 52x is setup-dependent; the 64% sample was deliberately drawn from weak-human-move moments).
- Images live in Research/Content/assets/ and embed via Obsidian wikilinks. If you publish outside Obsidian, export the PNGs alongside the post.
