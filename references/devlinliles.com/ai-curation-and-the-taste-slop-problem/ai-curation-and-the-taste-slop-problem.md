---
type: Reference
title: "AI Curation and the Taste Slop Problem"
resource: "https://www.devlinliles.com/ai-curation-and-the-taste-slop-problem/"
author: "Devlin Liles"
published: '2026-09-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Kyle Chayka and Sophie Haigney spent part of a recent Hard Fork culture-desk segment on a phrase that has been rattling around in my head since I heard it: taste slop. The setup was a question, not a prediction. What happens to culture when a handful of AI systems do all the recommending?

I want to work through why that question lands differently than it would have five years ago.

Chayka already answered an earlier version of it in 2024, in a book called Filterworld. His argument was that algorithmic recommendation, Spotify's playlists, Netflix's rows, Instagram's explore page, had already flattened culture into something closer to a single global aesthetic. He gave the visual version of it a name: AirSpace, the experience of walking into a coffee shop in Reykjavik, Los Angeles, or Seoul and finding the same reclaimed wood, the same Edison bulb hanging over the register, because Instagram and Yelp had trained a generation of designers on the same visual reward signal. Netflix has said for a decade that its recommendation engine drives roughly 80 percent of what people watch on the platform, a single algorithm settling most of what hundreds of millions of people watch each night.

The flattening Chayka describes predates generative AI by close to a decade. Hard Fork's culture desk was circling something more specific: a change in how many separate systems are doing the flattening.

Here is the distinction I keep coming back to. Spotify's recommendation model has no visibility into what Netflix recommends. Netflix's model has no visibility into what Instagram's explore algorithm surfaces. Each of those systems was trained on a different catalog, optimized against a different metric, built by an engineering team answering to its own product roadmap. The result was still homogenizing, Chayka is right about that, but it homogenized in parallel, through dozens of independently built systems that happened to converge on similar incentives: engagement, watch time, session length. The convergence was an emergent property of similar economics, not a shared source.

Taste slop describes a different architecture. If ChatGPT, Gemini, Claude, and two or three other frontier chatbots become the interface people use to ask what to watch tonight or what to read next, the number of distinct systems doing the recommending collapses to something closer to four or five foundation models sitting underneath every category of culture at once. Spotify's algorithm only ever had authority over music. A general-purpose AI assistant recommending music, books, restaurants, and news from the same underlying model has authority over the whole map at once.

That is a different kind of consolidation than Filterworld described. It is the difference between five industries each hiring their own consultant and living with that consultant's blind spots, versus five industries hiring the same consultant. The first produces five flavors of narrowness. The second produces one flavor, applied everywhere.

The platform-era flattening reads now like an early preview of something larger, and the mechanism behind it is about to get more concentrated. Chayka's coffee shop example worked because a hundred different local designers, working independently, were all pointed at the same algorithmic reward signal and arrived at the same output. The AI-curation version needs only one model's training data and one company's tuning decisions, replicated across every person who asks that model for a recommendation.

There is a version of this that plays out quietly and a version that plays out as a real cultural rupture, and the difference hinges on something nobody in that Hard Fork segment could answer yet: whether these chatbot recommendation layers end up trained on different data with different incentives, the way Spotify and Netflix were, or whether they converge on similar training approaches the way large language models have already converged on similar architectures. If it is the latter, taste slop becomes an accurate description of what happens once the last handful of independent filters left in culture turn out not to be independent after all.

That is the part of the question I cannot stop turning over. Filterworld already showed that any sufficiently optimized recommendation system flattens taste on its own, one platform at a time. What is actually open is whether we are about to lose the accident that kept that flattening from becoming total, the accident of enough different systems built by enough different teams that no single failure of judgment could reach everywhere at once.
