---
type: Reference
title: "Black Box AI Fails Weber&#x27;s Test"
resource: "https://www.devlinliles.com/black-box-ai-fails-webers-test/"
author: "Devlin Liles"
published: '2026-08-17'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Max Weber's sociology of authority identified three types of legitimate power. Traditional authority derives from custom and precedent: we follow because it's always been this way. Charismatic authority derives from the perceived exceptional qualities of an individual: we follow because the person is compelling. Rational-legal authority derives from rules applied transparently and consistently: we follow because the process is legitimate by virtue of being articulable, impartial, and subject to review.

Modern institutional governance is almost entirely rational-legal. Courts, regulatory bodies, HR processes, and credit systems derive their legitimacy not from tradition or personality but from articulated rules applied according to documented procedure. When you ask why a court ruled a certain way, you get a written opinion citing statutes and precedent. When you ask why you were denied credit, you get a letter citing specific factors. The decision is legitimate because it can be justified.

AI systems deployed in regulated contexts are asking for rational-legal authority. They're making consequential decisions in domains where that form of legitimacy is legally required. Most of them can't supply it.

The EU AI Act entered into force in August 2024, with obligations for prohibited AI systems applying from February 2025 and high-risk AI system requirements binding as of August 2026. It explicitly classifies AI systems used in HR, credit, healthcare triage, and law enforcement as high-risk, and mandates explainability, human oversight, and regular auditing. In the United States, regulators have been embedding explainability requirements into existing civil rights, consumer protection, and anti-discrimination frameworks. Healthcare providers must demonstrate how AI triage systems prioritize patients. Financial institutions are required to explain credit approvals and insurance pricing. Employers must justify automated hiring and promotion decisions.

These aren't technical suggestions. They're applications of Weber's rational-legal framework to AI decision-making. The demand is: this decision must be justifiable according to articulable rules. The AI system's authority to make the decision depends on meeting that demand.

The challenge is structural. Neural networks — the architecture behind virtually all frontier AI systems — are not inherently interpretable. The decision emerges from billions of parameters interacting through matrix operations. There is no path through the network that maps to a human-readable rule. You can build post-hoc explanations: SHAP values showing feature contributions, attention visualizations showing what the model attended to, saliency maps highlighting influential inputs. But these are approximations of an explanation, not the explanation itself. Research has documented a problem the field has been reluctant to face directly: post-hoc XAI methods can produce plausible-sounding explanations that don't accurately reflect the model's actual decision process, and only the full model weights can truly describe the complete mechanisms of a deep neural network.

This is the XAI legitimacy trap. An AI system that produces accurate decisions but cannot explain them fails Weber's test regardless of its accuracy. And an AI system that produces plausible explanations that don't reflect its actual reasoning process is failing a different, more dangerous test: it's producing the appearance of rational-legal legitimacy without the substance.

The structural response depends on the deployment context. For some regulated use cases, the appropriate answer is not to use black-box neural networks at all. Gradient-boosted decision trees, logistic regression on well-specified features, and rule-based systems are genuinely interpretable. The explanation is the model. They sacrifice some accuracy on some tasks, and that tradeoff needs to be made explicitly. For use cases where frontier model capability is genuinely required and a neural architecture is the only viable option, the XAI layer needs to be designed alongside the model, not bolted on afterward. That means establishing in advance what constitutes an adequate explanation for this specific use case, testing the XAI method against that standard, and auditing whether explanations remain accurate as the model updates.

The governance requirement that follows from this is simple but frequently missed: before deploying an AI system in a regulated context, the questions of legitimate authority need answers. What would a rational-legal explanation of this system's decisions look like? Who reviews it? What makes it adequate? Can the system provide that? Deploying without answers to these questions is deploying a system that lacks the form of authority required to operate in the context it's being put in.

The organizations that get this right treat explainability as an architecture requirement, not a compliance checkbox. They design for interpretability from the start of model selection, not as a retrofit after deployment. They test explanations for fidelity, not just plausibility. Weber's framework isn't an academic curiosity. It's the social contract that makes institutional decision-making legitimate. Black-box AI breaks that contract. The systems that don't break it are the ones designed from the start to honor it.
