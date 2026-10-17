---
type: Reference
title: "Your AI Is Either Part of Your Mind or Just Another Tab"
resource: "https://www.devlinliles.com/your-ai-is-either-part-of-your-mind-or-just-another-tab/"
author: "Devlin Liles"
published: '2026-08-06'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

There's a philosopher's thought experiment you should know about if you're deploying AI at scale. It distinguishes two very different things that look identical from the outside, and the difference determines whether your AI program compounds or plateaus.

Andy Clark and David Chalmers published "The Extended Mind" in 1998. The setup: imagine Otto, a man with early Alzheimer's who carries a notebook everywhere. Before going anywhere, he consults the notebook. The notebook tells him the museum is on 53rd Street. He goes to 53rd Street. Clark and Chalmers' claim: Otto's notebook is part of his mind, in the same functional sense that biological memory is part of anyone else's mind. It's reliable, constantly accessible, and Otto consults it the same way others consult their own recollection. If we wouldn't say Inga doesn't "really" remember the museum's address because she retrieves it from memory rather than reasoning it out, why would we say Otto doesn't "really" remember just because his storage is external?

The argument is still contested in philosophy. What matters for our purposes is the distinction it draws between two modes of using an external cognitive resource.

Mode one: tool. You consult it, get an answer, set it aside. The tool augments a discrete task. You remain the same thinker before and after the interaction.

Mode two: prosthetic. The resource is so deeply integrated into how you reason that removing it doesn't just slow you down. It changes what you're capable of. You've offloaded cognitive functions to it. You think differently because of it. Your reasoning process depends on it.

That distinction is exactly what's playing out across organizations deploying AI right now.

Most early AI adopters are tool users. They prompt, evaluate, incorporate or discard the output, move on. The AI is consulted the way you'd consult a search engine or a reference document. The interaction is discrete. The cognitive process is unchanged. The productivity gain is real but bounded. You do the same tasks faster.

A smaller group of adopters are building something closer to prosthetic integration. They've restructured how they work so that model inference is embedded in their reasoning process, not appended to it. They think out loud to the model. They test half-formed ideas against it. They use it to extend working memory across complex, multi-session problems. Their thinking process has changed. The model is part of the cognitive loop, not a tool they reach for.

Andy Clark published "Extending Minds with Generative AI" in Nature Communications in 2025, extending his original thesis to generative AI specifically. His argument: AI systems constitute cases of extended cognition when they meet the functional criteria: constantly accessible, reliably deployed, and integrated into cognitive process rather than consulted episodically.

Prosthetic integration produces more capable users. It also produces dependent ones. Research on AI over-reliance found that deep cognitive integration introduces risks when the AI system assumes too much decision-making authority. Users who've offloaded reasoning to the model lose the ability to perform those tasks without it. That's the extended mind failure mode: the notebook gets lost, and Otto can't remember where the museum is.

This is not a reason to avoid deep integration. It's a reason to design it deliberately. The questions worth asking are: which cognitive functions should be integrated into the model, and which should remain exercised in human cognition? What happens to the workflow when the model is unavailable, wrong, or confidently incorrect? Are the people using the system maintaining enough baseline capability to catch errors, or have they become dependent on outputs they can no longer independently evaluate?

Three structural responses follow. Integration depth targets need to be explicit — not every role benefits from prosthetic-level AI integration. Workflows that capture the model's reasoning chain give humans something to evaluate and maintain skills against; workflows that only capture the output create invisible dependencies. And quality review processes that only look at final deliverables won't detect prosthetic dependency until the model produces a confident error that no one catches.

Clark and Chalmers' original argument was about where minds end and the world begins. The practical version in 2026 is about how you design the boundary between human cognition and model inference, and what you put in place to keep that boundary healthy rather than letting it dissolve.
