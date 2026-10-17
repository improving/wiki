---
type: Reference
title: "The Categorization Skill That Never Changed"
resource: "https://www.devlinliles.com/the-categorization-skill-that-never-changed/"
author: "Devlin Liles"
published: '2026-10-16'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

An internal expense-report assistant I worked on started with exactly one job: categorize expense line items, meals, travel, software, other, against a fixed policy. It worked well, and it stayed simple because it only had to do the one thing. Then, over four releases, the team kept bolting unrelated functionality onto that same skill instead of building anything new. Release two added travel-policy question answering. Release three added currency conversion. Release four added receipt-OCR troubleshooting help. Each addition edited the same prompt file that had started as a clean, narrow categorization tool.

I kept a fixed thirty-item seeded expense test set and ran it against all four releases, checking categorization accuracy at each version. The categorization task itself never changed across those four releases. Nobody touched the policy it categorized against, nobody changed what counted as a meal versus travel, nothing about the actual problem being solved shifted at all. And accuracy still showed a measurable downward trend from release one to release four.

That's the part I want to sit with, because it's the counterintuitive piece. The regression had nothing to do with the categorization logic getting worse on its own terms. It came from cross-talk, instructions for the newer, unrelated functions sitting in the same prompt file and competing for the model's attention with the original categorization instructions every single time the model processed any request at all, categorization included. A prompt file that started as one clean job turned into four jobs sharing one file, like four roommates who never agreed to live together and keep leaving their stuff in each other's space.

## The pattern

The fix separates the four capabilities into four single-responsibility skills, each its own narrowly scoped prompt file, dispatched by a thin router that decides which skill a given request actually needs and sends it there. Categorization gets its own skill file, and so do travel-policy question answering, currency conversion, and receipt-OCR troubleshooting. None of them share a prompt anymore.

What I actually verified, and what I think is the load-bearing claim here, is that the categorization skill's prompt file stayed checksum-verified byte-identical across all four releases. Adding currency conversion in release three left the categorization file untouched, because the new capability lived somewhere else entirely and had no reason to reach into it. Accuracy stayed flat instead of declining, and it stayed flat as a direct, mechanical consequence of a file that literally could not have changed. Nobody improved the categorization prompt to get that result. That distinction matters. The fix worked by making the categorization file structurally untouchable, so the regression had no path to travel down.

The router's job is deliberately thin. It reads a request, decides which of the four skills should handle it, and sends the request there. It doesn't try to be smart about the content of any individual skill, and it shouldn't, because the moment routing logic starts encoding domain knowledge about categorization or currency conversion, it recreates a shared surface that regressions can travel across. The router's only job is dispatch. Each skill's only job is the one thing it was built to do.

## Design considerations

The obvious cost is that this trades a single simple prompt for a small system: a router plus four separate files, more moving parts, more places to look when debugging a request that went to the wrong place. For a genuinely single-capability tool that's never going to grow a second job, this is overhead with no return, and I wouldn't reach for it preemptively just because a tool might someday need a second capability. The pattern earns its keep at one specific moment: right when a second, genuinely unrelated capability is about to get added to an existing prompt.

The harder judgment call is deciding what counts as genuinely unrelated versus what's actually the same capability wearing a different name. Categorization and currency conversion are clearly separate jobs; nothing about deciding whether an expense is travel or meals depends on knowing today's exchange rate. But I've seen teams draw this line too finely, splitting a single coherent capability into three skills that all needed to share context anyway, which just moves the cross-talk problem into the router instead of eliminating it, and adds coordination overhead on top. The test I actually use is whether one capability's instructions would ever need to change because of something happening in another capability. Categorization's rules don't change because currency conversion added a new exchange-rate source. That's real independence. If two supposed capabilities keep needing coordinated updates because a change in one always implies a change in the other, they're probably one capability that got split prematurely, and the router between them is just friction with no isolation benefit to show for it.

There's also a scaling question this pattern doesn't answer on its own: what happens once you're not adding a fourth skill but a fortieth. A thin router dispatching across four well-understood capabilities is a clean design. A thin router dispatching across forty skills, written by different people at different times, starts to accumulate its own version of the problem this pattern was built to solve, just one layer up, at the level of the catalog instead of the level of a single file. Keeping any one skill's prompt from touching any other's is necessary, but it's not the same discipline as keeping the whole collection of skills from growing into an unmanaged pile that nobody's reviewing for overlap or redundancy. This pattern protects the boundary around each individual skill. The boundary around how many skills you end up with in the first place is a separate discipline, and one this pattern leaves entirely up to you.
