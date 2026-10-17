---
type: Reference
title: "Same Model, Different Outcome — Who&#x27;s Responsible?"
resource: "https://www.devlinliles.com/same-model-different-outcome-whos-responsible/"
author: "Devlin Liles"
published: '2026-08-10'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Two drivers run the same red light. One gets home safely. One kills a pedestrian. The action was identical. The moral judgment is not. The second driver is held to a different standard, faces different legal consequences, and is likely to carry the moral weight differently for the rest of their life. Same choice. Different luck. Philosophers call this moral luck, and it's one of the most uncomfortable concepts in ethics.

Thomas Nagel wrote the definitive paper on it in 1979. Bernard Williams wrote a companion piece the same year. Their argument: we routinely judge people based on outcomes partially outside their control. This violates intuitions about fairness, but it's how human moral communities actually work. The tension is real, the problem has no clean solution, and it has arrived in the AI liability debate with full force.

Here's the AI version. A model is deployed in a medical context. A user submits an adversarial prompt, carefully constructed to elicit dangerous medical advice. The model, following its training exactly, produces an output that harms someone. The model behaved identically to how it would behave on a thousand similar-looking but benign prompts. The harm came from the adversarial input, which was specifically engineered to exploit a known failure mode. The developer, the deployer, and the user all played a role. The harm happened.

The question of who bears responsibility is a moral luck problem. The model behavior was the same as the baseline. The outcome was catastrophic. The causal chain running from developer to deployer to user to adversarial input author has different link lengths, and the EU AI Act, extended U.S. product liability frameworks, and legal scholarship from 2024 and 2025 are all grappling with how to distribute responsibility across that chain.

Directive (EU) 2024/2853, published in November 2024, replaces the original 1985 product liability framework and explicitly includes software and AI systems in the definition of "product," establishing strict liability for AI-caused physical or property damage. This shifts the argument from negligence to strict liability: you made the thing, the thing caused harm, here's the accountability. The problem is that "strict liability for the developer" doesn't map cleanly onto the actual causal structure. The deployer chose the deployment context, the user population, the absence or presence of monitoring. Four different parties made choices. Anchoring liability to the developer simplifies the legal question but doesn't resolve the moral one.

Nagel's point was that moral luck is unavoidable because we can't fully separate the agent from their circumstances. The question isn't whether to account for outcomes outside the agent's control. It's how much weight to give them.

For enterprise AI deployment, the moral luck problem has three practical consequences. First, deployers carry more liability than they typically claim. "We're just using a vendor model" doesn't reduce causal proximity to harm. The deployer chose the model, defined the deployment context, set the user access policy, and decided what monitoring to run. When harm occurs from a model behavior the deployer could have caught with monitoring, the deployer's causal distance is not as great as a vendor-blame posture suggests.

Second, monitoring converts moral luck into moral agency. A deployer without output monitoring is flying blind on a luck-dependent outcome. Adversarial inputs will arrive; the question is whether the deployer detects them. When you build monitoring, you're not just improving system quality. You're exercising the agency that substitutes for luck. You're changing your causal position.

Third, incident response documentation matters morally, not just operationally. When harm does occur, the question courts and regulators will ask is whether you exercised reasonable care given what you could have known. That question is answered by your records: what monitoring you had, what it detected, what you did about it. A company with a mature incident response process around AI failures can demonstrate agency. A company with no documentation is at the mercy of moral luck in both the philosophical and legal senses.

Nagel concluded that moral luck creates irreducible friction in our ethical frameworks. We can't reason our way out of the discomfort by declaring that only controlled actions matter. We live with the tension. AI liability is the engineering version of that same tension. You can control the monitoring, the escalation paths, the audit trails, and the response protocols. The outcomes partially outside your control will still vary. That's moral luck. The question is how much of your situation you left to it.
