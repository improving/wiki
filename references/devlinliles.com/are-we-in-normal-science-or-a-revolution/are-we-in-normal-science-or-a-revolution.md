---
type: Reference
title: "Are We in Normal Science or a Revolution?"
resource: "https://www.devlinliles.com/are-we-in-normal-science-or-a-revolution/"
author: "Devlin Liles"
published: '2026-08-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Thomas Kuhn's insight, from his 1962 "The Structure of Scientific Revolutions," was that science doesn't progress as a smooth accumulation of knowledge. It proceeds through long stretches of "normal science" — incremental puzzle-solving within an accepted framework — punctuated by paradigm shifts, where the framework itself breaks and a new one takes over. The Copernican revolution wasn't just a new data point. It reorganized what every prior data point meant.

The AI field is in the middle of an unresolved argument about which mode it's in. The answer to that question determines whether your investment thesis, your safety architecture, and your capability forecasting are built on solid ground or sand.

Scaling laws, formalized in the 2020 Kaplan et al. paper from OpenAI, looked like the announcement of a normal science era. The finding was clean: you could predict model performance from three variables (compute, data, and parameters) with reliable mathematical relationships. More of each, better model. The curve was smooth, the exponents were stable, and for several years the field behaved accordingly. Every major lab scaled up. Investment followed the curve.

Then two things complicated the picture. First, the Chinchilla paper in 2022 showed that prior models had been significantly compute-suboptimal. The scaling law didn't break, but the constants shifted meaningfully. That's normal science handling an anomaly: update the coefficients, keep the framework.

Second, the emergent capabilities literature started documenting behaviors that the scaling law curve didn't predict. In-context learning, multi-step reasoning, code generation at production quality: these didn't appear to interpolate smoothly from smaller models. They appeared to phase-transition. If accurate, it means the scaling law framework doesn't capture the dynamics at the most important moments: the jumps.

The 2023 Schaeffer et al. challenge to emergence suggests these jumps might be measurement artifacts, not real phase transitions. But the meta-point holds regardless: the field is currently arguing about whether its primary predictive framework is adequate. That's not normal science. That's the early turbulence of a paradigm under pressure.

Several anomalies are accumulating that a purely normal science frame struggles to absorb. Hallucinations persist despite scale and RLHF. Models are brittle to small input perturbations. Multi-agent systems surface emergent behaviors that weren't visible in single-agent eval suites. Capability gains appear task-specific in ways the general scaling law doesn't predict. These aren't fatal to the scaling framework. But they're the kind of persistent anomalies that, in Kuhn's model, precede a shift.

The investment implication is immediate. In normal science, the planning model is extrapolation: more compute, proportionally better capabilities, predictable ROI. Roadmaps make sense. In revolutionary science, or even late normal science where anomalies are piling up, extrapolation is dangerous. The next capability jump might not be on the curve. The safety property designed for the current paradigm might not apply to the next one.

For practitioners, the actionable response isn't to bet on one camp or the other. Build planning and governance structures that work under both. Hedge extrapolation with conservative capability estimates, not just optimistic ones. Build evaluation infrastructure that can detect unexpected capability changes, not just measure expected ones. Keep safety architecture updated with each major model generation rather than assuming the prior version's safety properties transfer forward.

The normal science frame produces tight roadmaps and confident forecasts. The paradigm-shift frame produces scenario planning and optionality. Given that the field itself doesn't have consensus, the organizations that build for uncertainty will navigate both phases better than the ones that committed to a single prediction. Right now, the answer is genuinely unclear. That's where the planning sits.
