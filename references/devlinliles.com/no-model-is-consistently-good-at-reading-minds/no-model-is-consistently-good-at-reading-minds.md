---
type: Reference
title: "No Model Is Consistently Good at Reading Minds"
resource: "https://www.devlinliles.com/no-model-is-consistently-good-at-reading-minds/"
author: "Devlin Liles"
published: '2026-09-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Nine frontier vision-language models took two tests last month, both borrowed straight from developmental psychology. The first measures a narrow skill: can you set aside what you know and answer based on what someone else can actually see. The second measures a different skill: can you read intention from nothing but the motion of two shapes moving around a screen. Researchers at the University of Maryland ran all nine through both tasks and lined up the scores side by side.

The scores didn't agree with each other. A model that handled the false-belief task well, tracking what a character could and couldn't see, often stumbled on the animacy task, where the only signal is two shapes drifting across a screen with no caption explaining what they mean. The reverse held too: models that read intention from motion with something close to human accuracy sometimes missed the basic false-belief question a four-year-old gets right. Across nine models, no single one led on both. Being strong on one test told almost nothing about the other.

That's the part worth sitting with. Theory of mind gets treated in eval decks and vendor pitches as a single line item, a capability a model either has or lacks, usually backed by one benchmark number that gets repeated on a slide until it sounds like a settled fact about the model. This paper is evidence that the number describes one narrow skill, tied to one task. False-belief reasoning runs through language: it's a chain of inference that can be walked through in words, which gives a model good at chained reasoning a real shot at it almost regardless of anything else. Reading intention from motion has no language step to lean on. It sits closer to perception than to logic, and excelling at the first kind of reasoning buys no guaranteed head start on the second.

That gap lands hardest where marketing skips over it. A claim like "understands user intent" or "strong theory of mind" gets sold as one property. This paper breaks that claim apart into a bundle of separable skills that don't transfer to each other inside the same model. A single benchmark score speaks for whichever narrow slice that particular benchmark happened to test, and nothing more.

For a team evaluating a model against a specific deployed task, the practical question shifts from whether a model "has" theory of mind to which slice of it the task actually draws on. A support agent inferring what a frustrated customer already knows versus what they're only assuming sits closer to the false-belief test. A model reading hesitation and tone in a video call sits closer to the animacy test. Picking a model off a general social-reasoning score and expecting that score to carry into either job is a bet this paper gives no reason to make.

Nine models, two tests, no consistent winner. The number worth remembering from this paper is the size of the gap between a model's two scores. That gap is the real measure of how far a benchmark headline can be trusted to describe what happens on a task it never tested.
