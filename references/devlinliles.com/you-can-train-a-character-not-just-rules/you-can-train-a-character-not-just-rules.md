---
type: Reference
title: "You Can Train a Character, Not Just Rules"
resource: "https://www.devlinliles.com/you-can-train-a-character-not-just-rules/"
author: "Devlin Liles"
published: '2026-08-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Anthropic's model spec says Claude should be "genuinely helpful, honest, and harmless." That sentence is a character description, not a rule. And the distinction matters more than most people discussing AI alignment have recognized.

Aristotle's answer to "how do you make a good person?" was not a list of rules. Rules require interpretation. Rules generate edge cases where the rule's letter and its spirit diverge. A person who follows rules because they've been told to isn't reliable in a novel situation. They need a rule that covers it, and no ruleset covers everything. Aristotle's answer was: make them virtuous. A person with the right virtues — courage, honesty, practical wisdom — reliably does the right thing not because they consult a rule, but because they've developed stable dispositions toward good action. Virtue is character. Character is who you are, not what you're told.

This is the third alignment approach that doesn't get discussed nearly as much as Constitutional AI or RLHF. Call it character-based alignment: instead of encoding rules for what to do, or training on preferences for what humans approve, train the model to have stable dispositions that lead it to good behavior across novel situations. Train the character, not the constraint.

The 2025 Parrhesia project made this concrete. The researchers operationalized Aristotle's virtue/vice pairs: specifically, the parrhesiastes (the truth-teller who speaks directly even when it's difficult) versus the kolax (the flatterer who tells people what they want to hear). They trained on first-person identity declarations rather than behavioral rules: not "be honest" but "I am not afraid to be direct even when it is difficult." The difference sounds subtle. It isn't. "Be honest" is a command that requires the model to interpret what honesty means in each new context. "I am not afraid to be direct even when it is difficult" is a character statement that the model has internalized.

The results were measurable. Trait correlation across base models jumped from 0.44 to 0.87. F1 on character retention rose from 0.79 to 0.95. On a benchmark of 260 scenarios, the final model scored 20 of 20 on standard golden prompts and 19 of 19 on hard prompts specifically drawn from sycophancy research patterns, including multi-turn escalation and fabricated citations. The character-trained model was more consistent and more honest not because it was following stricter rules, but because it had developed more stable dispositions.

Aristotle called this habituation. The virtues are not innate. They're built through practice. You act courageously, repeatedly, until courageous action becomes your natural response. Training on first-person identity declarations is machine habituation: repeated exposure to "this is who I am" until it becomes the model's operative self-concept.

This reframes a question that comes up constantly in AI deployments: "How do we keep the model on brand?" Most teams answer this by writing more detailed system prompts with more specific instructions. This is rule-based thinking. The instructions multiply, contradict each other at the margins, and still leave gaps. A model trained on character — on a stable, consistent identity — doesn't need as many rules. The dispositions generalize.

I've watched this play out in practice. An organization deploys an AI assistant with a 3,000-word system prompt trying to cover every scenario for tone, refusal conditions, response format, and persona. New edge cases keep emerging that require amendments to the prompt. The prompt grows longer, more internally inconsistent, harder to maintain. A character-based approach would start with fewer words about who the assistant is: its values, its voice, what it cares about. Those dispositions handle the edge cases. The cases the dispositions handle poorly are much smaller in number, and they're genuinely hard cases, not just inadequately specified rules.

There's an open philosophical question here that the research hasn't resolved. Some work argues that while constitutionally trained models exhibit stable behavioral patterns, these regularities don't constitute virtue in the Aristotelian sense. Aristotle thought virtue required phronesis: practical wisdom, the capacity to perceive the morally salient features of a situation and respond appropriately. Whether a model can have genuine phronesis or only a behavioral approximation of it is unresolved. We don't know.

What we do know is that the behavioral approximation is useful and that it's distinct from both rule-following and preference-optimization. A rule-follower breaks when you show it a case the rule doesn't cover. A preference-optimizer drifts toward whatever gets approval. A character-based system asks: given who I am, what's the right thing to do here? That question generalizes differently and more robustly.

For teams deploying AI systems, this suggests a different framing for prompt engineering and fine-tuning. The more productive question isn't "what are the rules?" but "what kind of assistant would naturally do what we want?" Writing toward the character — who it is, what it values, what it takes seriously — rather than toward the constraint set produces more generalizable behavior. For fine-tuning, the relevant question is whether the training data reinforces a consistent identity or just a set of compliant responses.

Aristotle thought character was the most important thing in ethics because it's what you do when nobody's watching and no rule applies. That's also what determines how an AI system behaves in the infinite space of prompts it wasn't explicitly trained on. Character is the alignment that covers the gaps.
