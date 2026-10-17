---
type: Reference
title: "Design Your AI Like You Don&#x27;t Know Who You Are"
resource: "https://www.devlinliles.com/design-your-ai-like-you-dont-know-who-you-are/"
author: "Devlin Liles"
published: '2026-08-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

John Rawls asked one of the most useful questions in the history of political philosophy: what principles would rational people choose for organizing society if they didn't know what position in that society they would occupy? Behind the "veil of ignorance," you don't know whether you'll be born rich or poor, majority or minority, healthy or disabled. You choose principles that you'd find acceptable from any position because you might end up in any of them.

It's a thought experiment designed to strip away the self-interest that corrupts institutional design. When you don't know which group you'll belong to, you have a strong incentive to make the rules fair for everyone.

Fair machine learning has been applying this framework for several years. The question becomes: what model behavior would you want if you didn't know which demographic group's queries you'd be submitting? If you wouldn't want the model to treat users differently based on race, gender, age, or national origin, and you don't know which of those you are, you have a strong incentive to design demographic parity into the system from first principles, not as a compliance afterthought.

This is harder than it sounds. A November 2025 paper operationalizing the veil of ignorance as a computational principle tried two approaches to removing demographic signal from a binary classifier. The naive approach — just removing demographic features from the input — worsened bias by 8.9%. The proxy-aware approach — identifying and pruning features that act as demographic proxies even when the explicit demographic attributes are absent — reduced the demographic parity gap by 32.6%. The naive approach made things worse because it didn't account for the fact that demographic information was still present in the remaining features, just encoded indirectly.

This is the Rawlsian lesson in practice: simply pretending not to know a person's demographic group, by removing obvious features, doesn't put you behind the veil of ignorance. It puts you behind a thin curtain with the information visible through it. Genuine ignorance requires actively designing out proxy signals, which requires knowing what they are.

A critique of Rawlsian ML fairness is also worth taking seriously. Research published in the Fudan Journal of the Humanities and Social Sciences identified what the authors called the fundamental paradox: systems that meet initial Rawlsian fairness criteria can create growing disparities over time through feedback loops. A healthcare resource allocation model that is demographically fair at deployment may systematically under-serve vulnerable groups two years later, because the model's outputs shape the data it's trained on next cycle. Healthcare case studies documented exactly this pattern. Rawlsian fairness is a static principle applied to a dynamic system. You can be behind the veil at deployment and gradually reveal the demographic landscape through feedback loops.

The practical question is how you operationalize this in enterprise AI work.

The first operationalization is reframing the fairness question at design time. Starting with "what are our demographic equity obligations?" positions fairness as compliance — a minimum. Starting with "what behavior would we want from this model if we didn't know which group we'd be in?" positions it as genuine design intent. The difference shows up in how ambitious the targets are and how much investment gets allocated to evaluation.

The second is disaggregated evaluation as standard practice. Aggregate metrics can't surface fairness failures. An overall accuracy of 87% can hide 94% accuracy for majority groups and 74% for minority groups. Disaggregated performance metrics by relevant demographic categories before deployment aren't a special fairness review — they're just what evaluation looks like when the veil-of-ignorance framing is taken seriously.

The third is longitudinal monitoring. Fairness metrics at deployment are necessary but insufficient because of the feedback loop problem. Re-evaluation at regular intervals against evolving population distributions requires instrumenting the system to capture the data needed for monitoring from day one. It can't be retrofitted after the fact.

The fourth is the hardest: the proxy problem. Removing demographic features doesn't remove demographic signal. Zip code encodes race and income. Browsing history encodes gender and interests. Vocabulary patterns encode education and regional origin. Genuine fairness requires modeling proxy pathways, not just removing protected attributes. This requires sustained technical investment, not a checkbox.

Rawls thought the veil of ignorance revealed what justice actually requires, stripped of self-interest. Applied to AI, it reveals what fairness actually requires, stripped of the majority group's natural tendency to design for itself. The veil-of-ignorance question — what would the system look like if designers didn't know which group they'd belong to — is a more demanding design prompt than demographic compliance, and a more honest one.
