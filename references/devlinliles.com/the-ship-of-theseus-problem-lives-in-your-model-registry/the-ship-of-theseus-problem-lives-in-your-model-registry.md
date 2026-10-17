---
type: Reference
title: "The Ship of Theseus Problem Lives in Your Model Registry"
resource: "https://www.devlinliles.com/the-ship-of-theseus-problem-lives-in-your-model-registry/"
author: "Devlin Liles"
published: '2026-08-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The ancient puzzle goes like this: sailors replace every plank in Theseus's ship over the years, one by one, until no original material remains. Is it still the same ship? Philosophers have argued about this for centuries. Most enterprises deploying AI haven't had to care. Until now, when the answer has real legal, operational, and safety weight.

The model you validated in a controlled evaluation last quarter may not be the model running in production today. Not because you made a mistake. Because the provider updated it.

OpenAI, Google, Anthropic, and every major model provider issue "silent updates": weight changes that don't increment the version number you pinned in your code. The endpoint name stays the same. The behavior drifts. GPT-4-turbo in May 2024 and GPT-4-turbo in November 2024 share a name but not identical weights. The Azure OpenAI platform has formalized this pattern: GA models receive retirement dates at launch, and when a version retires, your deployment can be auto-upgraded to a replacement model you didn't explicitly choose if your deployment policy is set to "upgrade when expired." The endpoint stayed. The model changed.

This is the Ship of Theseus problem in enterprise AI, and most organizations aren't governing it.

The issue isn't whether the replacement model is better. Often it is. The issue is that identity continuity — knowing that "this model" is the same entity across time — is foundational to three things that regulated enterprises need: compliance evidence, reproducibility, and trust.

Start with compliance. If your AI system makes credit decisions, clinical recommendations, loan denials, or employee performance assessments, you have regulatory obligations to document what system made what decision and why. "We used GPT-4-turbo" isn't a sufficient answer when the weights behind that name changed three times during the period in question. The auditor will ask which GPT-4-turbo. The answer matters. The Ship of Theseus problem isn't academic when your SOC 2 auditor or a regulatory inquiry shows up and wants to trace a decision back to a specific model state.

Reproducibility compounds this. Reproducibility is the foundation of scientific validity in AI evaluation, and it's already in crisis. The AI reproducibility literature is consistent on this point: surveys of ML research reproducibility find substantial failure rates tied to unpinned versions and drifting dependencies, with over 70% of researchers reporting inability to reproduce another group's findings. That's before you factor in the provider silently updating the weights under you. If you published evaluation results in Q2 and the model changed in Q3, your Q2 results are now describing a system that no longer exists.

Trust is the third leg. Users and operators develop calibrated expectations about a model's behavior: its tendencies, its failure modes, its handling of edge cases. Those expectations are built on observation of a specific set of weights. When weights change silently, the contract breaks. The entity they validated isn't the entity running anymore. In a medical context, continuity of care arguments rest on the assumption that the diagnostic AI assisting a clinician this week is behaviorally identical to the one from last week's baseline. That assumption is rarely enforced technically.

The structural response here is straightforward, though most organizations haven't implemented it. First, pin at the model version level, not the endpoint name level. Every major provider exposes timestamped or hash-identified model versions. Use them. Your inference calls should specify the exact version, not the alias. Second, add model identity to your audit logging. Every inference event should record not just the endpoint name but the resolved model version returned by the API. Third, treat model updates like software deployments: require a re-evaluation cycle before any model version change goes live in production for regulated use cases. The same change management discipline you apply to application code applies to the model your application depends on.

There's a harder philosophical question embedded in this that doesn't resolve cleanly: when does a fine-tuned model become a genuinely different model? Add safety fine-tuning, and the behavior changes. Add instruction tuning, and the personality shifts. Change the RLHF reward signal, and the model's tendencies realign. At some threshold, you're not fine-tuning the same base model anymore. You've built a different artifact. The industry doesn't have consensus on where that threshold is, and the naming conventions don't signal it.

Theseus's sailors knew they were replacing planks. Your model registry probably doesn't.

The practical discipline is this: treat model identity as an operational variable, not an assumption. Know what version is running. Know when it changes. Have a re-validation protocol before it goes back into a regulated workflow. The model you deployed and the model running in production are the same ship only if you've made sure the planks haven't been replaced while you weren't looking.
