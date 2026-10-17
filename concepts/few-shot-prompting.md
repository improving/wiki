---
title: "Few-Shot Prompting"
type: "Concept"
description: "Supplying examples in a prompt to activate and shape model capability, where one exemplar often suffices and repetition leaks values."
created: '2026-10-17'
updated: '2026-10-17'
tags: [prompting, evaluation, capability]
sources:
  - "/sources/one-exemplar-is-enough-and-a-second-one-leaks.md"
  - "/sources/the-model-knows-more-than-its-telling-you.md"
---

# Few-Shot Prompting

Few-shot prompting places worked examples in the prompt to demonstrate the desired structure and elicit capability that zero-shot prompts leave dormant. In this corpus it is both a practical technique — how many examples, and which — and a caution about measurement, since performance depends on how a model was asked, not only what it knows.

## Key Claims

- One example fully conveys a simple, consistent target structure, so additional examples rarely earn their [token cost](/concepts/token-cost.md).
- Repeating the same exemplar reinforces its specific values, causing leakage into extractions.
- Generic placeholders avoid echoing plausible values, reducing the risk of contaminated output.
- Structural variation may justify a second exemplar; mere repetition never does.
- Few-shot examples activate capabilities that zero-shot prompts leave dormant, as when [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) lifted PaLM 540B on GSM8K from 18% to 57%.
- Capability assessments have a shelf life as prompting skill improves, because measured capability is a function of how the model was asked.

## Related

- [Prompt Engineering](/concepts/prompt-engineering.md) — the broader practice few-shot prompting belongs to
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — a prompting technique that similarly unlocks latent capability
- [token cost](/concepts/token-cost.md) — the cost that redundant exemplars waste
- [Emergent Capabilities](/concepts/emergent-capabilities.md) — capability only revealed under the right prompting
- [One Exemplar Is Enough, and a Second One Leaks](/sources/one-exemplar-is-enough-and-a-second-one-leaks.md) — primary source
