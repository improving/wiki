---
type: Reference
title: "Your AI Benchmark Is Not Science Until It Can Fail"
resource: "https://www.devlinliles.com/your-ai-benchmark-is-not-science-until-it-can-fail/"
author: "Devlin Liles"
published: '2026-08-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Karl Popper's central contribution to philosophy of science was a deceptively simple criterion: a claim is scientific if and only if it's falsifiable. Not "true." Falsifiable. There must be a possible observation that would prove the claim wrong. Astrology fails this test not because its predictions are inaccurate, but because every failed prediction gets reinterpreted rather than refuted. A theory that can absorb any evidence is not a theory. It's a narrative.

Most AI capability claims are in the same position as astrology right now.

The claim "this model reasons well" or "this model achieves state-of-the-art performance" rests on benchmark scores. Benchmarks are supposed to be Popper's falsifying test: a structured evaluation where the model either demonstrates the capability or doesn't. The problem is that the benchmark ecosystem has developed two failure modes that together undermine the Popperian framework almost completely.

The first failure mode is saturation. MMLU, the Massive Multitask Language Understanding benchmark that became a standard measure of general knowledge and reasoning, has been effectively neutralized as a discriminator. Frontier models cluster above 88-90% accuracy, making score differences statistically meaningless for procurement decisions. The range is narrow enough to be within measurement noise. A 2025 systematic study found that contaminated static QA and reasoning datasets plateau within two years of release. When a benchmark saturates, the falsification test breaks. A model that fails at 91% while a competitor scores 93% tells you almost nothing. Both pass. The benchmark can no longer generate the refutation that scientific methodology requires.

The second failure mode is contamination. Benchmark data ends up in training corpora. The model doesn't reason through the questions; it recalls training exposure to similar items. Research has detected a 57% exact match rate for ChatGPT predicting masked choices in the MMLU test set, and inference-time decontamination removes roughly 23% of MMLU score inflation in affected models. A 2025 paper "AI Evaluation Should Require Standardized Item-Level Data Releases" puts it directly: without item-level inspection, it remains unknown whether observed improvements reflect genuine capability gains, benchmark saturation, or data contamination.

This is Popper's demarcation problem, instantiated in your procurement process. When an AI vendor presents benchmark scores, the structurally relevant questions are: Could this model have failed this benchmark? What would failure look like? What score would constitute evidence that the claimed capability doesn't exist? If neither you nor the vendor can answer those questions concretely, the benchmark score is marketing, not evidence.

The 2026 benchmark landscape reflects some awareness of this problem. ARC-AGI-1, designed specifically to resist training data contamination through novel visual reasoning tasks, was saturated quickly: frontier models now exceed 96%. ARC-AGI-2 launched in March 2025 with every frontier model scoring 0%; by April 2026, top models reached 73-85%. ARC-AGI-3 dropped in March 2026 and best frontier systems currently score below 0.4% while humans score 100%. The field is on a treadmill: every benchmark built to survive contamination becomes a training target for the next generation.

The structural response is evaluation governance inside each deploying organization. When selecting a model for a production use case, the vendor's published benchmark scores answer the wrong question. The right question is: does this model perform adequately on the specific tasks in a given workflow, under the specific failure conditions that matter for that deployment? That requires building an internal evaluation suite, with tasks drawn from actual use cases and failure modes explicitly identified. An organization-specific eval suite is falsifiable — it reflects actual requirements, and a model either meets them or it doesn't.

The AI evaluation field is in an early replication crisis. Published capability claims fail to reproduce across evaluation setups, prompt variations, and independent research groups at rates that should alarm practitioners. The underlying mechanism is identical to the psychology replication crisis: publication bias toward positive results, underspecification of methodology, and metrics selected to show performance rather than test it.

"This model achieves 92% on our benchmark" is not a scientific claim if the benchmark saturated, if the model was trained on similar data, and if you don't publish the prompts alongside the score.

Popper's test applies here. An eval that every model passes isn't a test. It's a participation trophy.
