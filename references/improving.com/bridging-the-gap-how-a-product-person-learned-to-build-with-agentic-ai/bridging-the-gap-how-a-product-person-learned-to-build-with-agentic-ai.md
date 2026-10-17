---
type: Reference
title: "Bridging the Gap: How a Product Person Learned to Build With Agentic AI"
resource: "https://www.improving.com/thoughts/bridging-the-gap-how-a-product-person-learned-to-build-with-agentic-ai/"
author: "Tim Dickey"
published: '2026-06-03'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

I didn’t become a developer, I just got tired of being the “business person” who talked about software while everyone else actually built it.

So, I did something that felt a little reckless for a Scrum Master / Product Owner / BA / PM: I started building software myself using an agentic AI framework called BMAD as my set of training wheels.

What happened changed how I show up on the “business side” of every product team I work with.

## **When I Stopped Staying in My Lane**

The turning point was a night I fired up BMAD’s “party mode.”

Party mode spins up a cast of agent personas, product manager, analyst, architect, developer, tester, Scrum Master, and drops them into a shared chat. I typed in a wild concept for a Scrum‑stances coaching app, hit enter, and watched the room explode.

In minutes, the agents were asking sharper questions than most real meetings:

- “Who’s the *actual* user — solo Scrum Masters, or Scrum Masters inside orgs?”
- “Who pays if management is part of the problem?”
- “Is this a board tool, or a stance‑development tool?”
- “Is this really enterprise SaaS, or an open source community tool in disguise?”

I came in “just” testing an AI framework. I left realizing the system had reflected my own fuzziness back at me and then helped me clean it up. This wasn’t about becoming a 10x engineer. It was about becoming a **more honest, more useful product person** by stepping into the build, not just facilitating around it.

## **Why “Business**‑**Side Only” Is Becoming a Liability**

For most of my career, staying on the business side felt responsible. My job was to coach, clarify, prioritize, and translate. When things got “too technical,” I’d hand off to a developer or architect and trust them to fill in the blanks.

That made sense when the build side was the bottleneck. Humans wrote all the code. Documentation was expensive. Asking for “one more experiment” meant weeks of effort.

Agentic AI broke that equation. Now:

- A small agent swarm can draft an architecture doc in minutes.
- A dev agent can scaffold a whole web app while you refill your coffee.
- An analyst agent can rip apart your PRD and rebuild it with tighter constraints and better benchmarks.

The slow part isn’t typing anymore. The slow part is thinking:

- Are we solving a real problem or a vanity problem?
- Are our constraints real or just habits?
- What’s the economic cost of “just one more dependency” or “just one more model”?

If you stay purely on the business side, you make big calls about scope, risk, and value **without feeling those decisions in the code, the architecture, or the spend.** That’s not safer, that’s just blind. I didn’t want to be blind anymore.

![asset 1 - Bridging the Gap: How a Product Person Learned to Build With Agentic AI ](images/AdobeStock_247176662.jpeg)

## **BMAD: Training Wheels for Non**‑**Developers**

BMAD wraps your work in a familiar team shape:

- Product manager persona to challenge vision and scope.
- Analyst persona for PRDs and briefs.
- Architect persona for stacks and constraints.
- Developer persona for implementation and refactors.
- Tester persona for acceptance criteria and coverage.
- Scrum Master persona to nag about “dev‑ready” vs. wishful thinking.

You talk to them in plain language. They answer in artifacts: markdown docs, stories, tests, code, workflows. For someone like me, that does two things:

1. **Lowers the barrier to entry.** I don’t have to know every tool’s syntax. I can say, “Help me design a Cynefin facilitation app that deletes data after 72 hours,” and the agents handle scaffolding while I steer.
2. **Raises the bar on my thinking.** Weak requirements, fuzzy users, and magical MVP thinking get exposed fast. The agents keep asking, “Who is this for? What does ‘done’ look like? What does that choice mean for architecture and testing?”

BMAD didn’t turn me into a full‑stack engineer. It turned my product instincts into something testable, and it made the build side feel less like a black box.

## **Hands**‑**Dirty Moment #1: A Cynefin App in an Afternoon**

As a facilitator, I love the Cynefin framework. Explaining it in slides felt flat. I wanted a tiny web app to use in workshops: capture examples, sort them into domains, then wipe the slate clean.

Pre‑AI, that idea would have lived on a “someday” board. With BMAD, I:

- Opened a clean repo and installed the framework.
- Told the agents what I wanted: a simple React app, backed by a database that auto‑deletes data after ~72 hours.
- Let the dev and architect personas propose a stack and wire up the basics.

In a single afternoon, I had:

- A working front end.
- A cloud backend with the right tables and retention.
- A thin but real app I could stand up, use with a team, and tear down.

I still had to review code, tweak copy, and adjust UX details. I had to learn enough to fix tooltip behavior and move text where it actually helped the conversation.

But, my facilitation pain turned into a **real product**, not just a user story. Once you’ve seen a throwaway prototype become a usable app in a day, it’s harder to ask a team for three sprints on something you’ve never tried to stand up yourself.

## **Hands**‑**Dirty Moment #2: Getting Called Out by My Own PRD**

In another experiment, I dropped BMAD into a brownfield research repo: a multimodal neural‑net project. I already had a PRD. It felt solid. Then I asked the analyst persona to review it. The feedback stung, in a good way:

- Clearer problem statements, fewer buzzwords.
- Explicit hardware and training targets: “On this class of GPU, aim for this many hours, this many parameters, this kind of throughput.”
- A competitive landscape I hadn’t fully articulated.
- A challenge to a “nice to have” external dependency that really belonged in a later phase.

I didn’t need to become a CUDA expert. I needed to accept that my original PRD was closer to a vision memo than an engineering doc. Since then:

- I ask sharper questions when someone proposes “just one more library” or “one more model.”
- I talk about constraints in concrete terms: time, memory, throughput, accuracy, not just “faster” and “better.”
- I respect the cost of “research work” in a way I didn’t before I’d seen it wired all the way through.

You can do a smaller version of this on any product:

- Take a PRD you’re proud of.
- Ask an analyst‑style agent to tear it apart and rebuild it.
- Bring those sharper edges back to refinement and planning.

## **Hands**‑**Dirty Moment #3: Turning Scrum**‑**Stance Awkwardness into a Product**

The most personal experiment was the Scrum‑stances app. As a Scrum Master and coach, I’ve had awkward shifts between stances. Moving from coach to teacher, or facilitator to change agent, isn’t always graceful. It doesn’t always hurt the team, but you know when it lands wrong.

One day, I dropped that awkwardness straight into party mode: “I have a wild idea for a Scrum application that helps Scrum Masters practice stances, not just move cards. Let’s use scrum.org as a canonical source and build what I wish I’d had moving from PM to Scrum Master.” The agents:

- Framed a problem statement around the gap between certification and lived practice.
- Called out how luck‑based mentor access really is.
- Challenged my “first mover” language and reframed it as “first to operationalize stance development.”
- Hammered privacy and psychological safety: reflections only help if Scrum Masters feel safe writing them.

Then they zeroed in on something I’d been dancing around:

- This wants to be open source, community‑driven, and individually adopted.
- Scrum Masters should be able to sign up without management buy‑in.
- Crowdfunding and sponsorship fit my values better than chasing license revenue.

In other words, they turned my **origin story** into a product strategy. I didn’t leave with a finished app. I left with:

- A sharper brief.
- A stack that invites contributions instead of scaring them off.
- A more honest way to explain my “why” to other Scrum Masters.

My lived awkwardness stopped being a war story and became first‑class product input.

## **How This Changed My Day Job**

I’m still a Scrum Master / Product Owner / BA / PM, but I’m different now because I’ve spent time on the build side with agents:

- **In refinement**, I don’t accept fuzzy stories or acceptance criteria. Not because a book says so, but because I’ve watched agents flail on vague inputs and invent solutions I didn’t intend.
- **In planning**, I talk concretely about tradeoffs. I ask, “What does this tool choice do to our CI? To other contributors?” I’m not out‑architecting anyone; I’m trying to understand the risk and cost I’m asking them to accept.
- **In coaching**, I don’t just tell teams to “get closer to the build.” I can say, “Let’s sit with an agentic dev for an afternoon and spike a small thing together. You’ll see what clean stories and constraints do to speed.”

Mostly, I have more empathy. When devs push back on scope, I’ve felt that tension in my own experiments. When QA asks for better acceptance criteria, I’ve seen the difference in automated tests. When architects question “just one more integration,” I can picture the dependency tree, not just the roadmap.

I’m still the business‑side person who jokes about “playing a developer on TV.” But that act has real consequences: it makes me a better partner to the people who live in the code every day.

![Asset - Embracing a Learning Mindset... in Development and Life](images/AdobeStock_172387489.jpeg)

## **Getting Started: A Tiny Playbook for Business**‑**Side Folks**

If you’re a Scrum Master, Product Owner, BA, PM, or any business‑focused team member, here’s a small, concrete way to start.

#### **1. Pick a problem that annoys *****you****

Keep it tiny and selfish:

- A facilitation tool (like the Cynefin app).
- A micro‑dashboard you wish existed.
- A little companion for a workshop or training you already run.

#### **2. Commit to one weekend of building**

- Set up an agentic framework (BMAD or something similar).
- Don’t chase the “perfect stack.” Let the architect/dev personas propose a default.
- Your goal isn’t “production‑ready.” It’s “something I can click around in and learn from.”

#### **3. Lean into the conversations, not the code**

- Ask the analyst for a brief or PRD.
- Ask the PM persona to challenge your users and value prop.
- Ask the architect what tradeoffs your choices imply.
- Let the dev agent scaffold, then you read and question the output.

#### **4. Bring one artifact back to your team**

On Monday show up with:

- A tiny running thing, or
- A sharper PRD/brief, or
- A clearer view of constraints and costs.

Then say, “I tried building this weekend. Here’s what I learned about how we write stories / talk about constraints / reason about cost.” You don’t have to become a developer, but you do need to **touch the build**. Because at the end of the day:

- **We are people solving problems for people.**
- **We are people doing business with people.**
- **We are people using generative AI to build products for people.**

Trust changes everything.

One of the fastest ways I’ve found to earn that trust is to spend a little of my own time in the team’s world: hands on the keyboard, agents at my side, learning by building.

Ready to bridge the gap between business and build? [Reach out to Improving to see how agentic AI can accelerate your product teams.](https://www.improving.com/contact/)
