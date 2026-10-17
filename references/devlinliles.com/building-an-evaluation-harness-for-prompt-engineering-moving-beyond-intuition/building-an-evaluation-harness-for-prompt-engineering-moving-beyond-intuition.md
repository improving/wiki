---
type: Reference
title: "Building an Evaluation Harness for Prompt Engineering: Moving Beyond Intuition"
resource: "https://www.devlinliles.com/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition/"
author: "Devlin Liles"
published: '2026-07-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Prompt engineering in production AI systems has a measurement problem. The dominant workflow (iterate on the prompt, test it against a few representative inputs, judge the outputs by feel, deploy) produces prompts that work in the conditions they were tested in. It does not produce confidence about how they will behave across the full range of inputs they will encounter, or about whether they will continue to work as the models they run on are updated.

This is not a criticism of intuition-driven iteration as a starting point. For early-stage exploration, when the goal is understanding what a prompt can do, informal iteration is appropriate and efficient. The problem emerges when prompts move from exploration to production: when they are running at volume, when model updates can change their behavior without warning, and when the cost of silent quality degradation is meaningful.

An evaluation harness addresses this by providing a systematic, repeatable measurement of prompt performance. The components are not novel. They are the same components that make software testing reliable: a defined set of test cases, a scoring mechanism, and a gate that prevents regressions from reaching production. Applying these to prompt engineering requires adapting each component to the specific properties of LLM outputs.

## Why Prompts Degrade Over Time Without Measurement

Three mechanisms cause prompt quality to change without any modification to the prompt itself.

**Model updates** are the most common and least visible. Providers update models on schedules that do not align with prompt development cycles. These updates generally improve average performance but can shift behavior for specific prompt patterns that the previous model handled in particular ways. A prompt that was calibrated against the previous model's instruction-following behavior may produce degraded outputs after an update, and without systematic measurement, the degradation accumulates across many queries before it becomes visible in user feedback.

**Context drift** affects prompts that reference the state of an evolving system. A prompt that correctly frames a coding task in terms of the current architecture conventions becomes incorrect as those conventions change. The prompt is unchanged; the ground truth it was calibrated against has moved. This is particularly common in development automation contexts where prompts reference codebase structure, team conventions, or API specifications.

**Input distribution shift** is gradual and difficult to observe. A prompt developed against a sample of representative inputs will encounter a different distribution of inputs as usage grows. New user populations may phrase requests differently. New use cases may fall at the edges of what the prompt was designed for. Inputs that were rare in the development sample may become common in production. The prompt's average performance across the production distribution may be meaningfully lower than its performance across the development sample, and without distribution-aware measurement, this gap is invisible.

None of these mechanisms produce failures that are immediately obvious. Quality degrades gradually, and the questions for which degradation is most significant may not be the ones generating the most feedback. Systematic evaluation is what makes the degradation detectable before it has accumulated to a level that produces noticeable user impact.

## The Four Components of an Evaluation Harness

**The golden dataset** is a curated collection of input-output pairs that represent the range of behavior the prompt is expected to produce. The quality of the golden dataset largely determines the quality of the evaluation. A dataset that overrepresents the easy cases produces optimistic scores that do not reflect production performance. A dataset that is representative of the actual input distribution, and that includes the edge cases where the prompt is most likely to fail, produces scores that are predictive.

Constructing a useful golden dataset requires deliberate selection across several dimensions: examples from the happy path, examples from edge cases that have historically caused problems, examples from high-stakes input categories where incorrect outputs have meaningful consequences, and examples that probe the boundary conditions of the prompt's intended scope. The size needed depends on the variance in the prompt's outputs; high-variance prompts require larger datasets to produce stable scores.

**The scoring rubric** defines what constitutes a good output in measurable terms. The most natural automated metric, output similarity to the reference output, is often a poor indicator of actual quality. A high-similarity output might be technically different but semantically equivalent; a low-similarity output might be exactly correct but worded differently. Similarity scores also fail to distinguish between the dimensions of quality that matter differently for different applications.

A useful rubric defines quality along multiple independent dimensions, each with a defined rating scale. For a coding task, these might include: correctness (does the code do what was requested?), completeness (does it address all components of the task?), style adherence (does it follow the conventions specified in the prompt?), and safety (does it avoid patterns that create security risks?). Each dimension gets a numeric rating, and the rubric is calibrated until two independent raters scoring the same output agree within one increment on each dimension.

Automated scoring works well for dimensions that can be checked programmatically: correctness of structured outputs, presence of required fields, adherence to a defined format. Dimensions that require judgment (code clarity, reasoning quality, tone appropriateness) require human scoring, at least for calibration and for the cases where automated scores fall in uncertain ranges.

**The automated runner** executes the prompt against the golden dataset on a schedule and on every change to the prompt or its configuration. It collects outputs, applies automated scoring for the dimensions that allow it, flags uncertain cases for human scoring, and aggregates results into a per-dimension score profile and an overall score.

Running on a schedule, and not only on prompt changes, is what catches the model-update and context-drift degradation mechanisms. A weekly automated run against the golden dataset will detect when a model update has shifted performance before users report it. The schedule frequency should be proportional to how quickly the model update and context drift mechanisms are expected to accumulate: faster for systems where model providers update frequently, slower for more stable configurations.

**The regression gate** connects the harness to the deployment pipeline. A prompt change that produces any dimension score below the current baseline does not deploy. A model update that shifts scores below a defined threshold triggers an alert before it reaches production traffic. The gate is what converts the harness from a reporting tool into an enforcement mechanism.

The gate threshold requires calibration. Setting the gate to block any score decrease will reject prompt changes that produce meaningful improvements on some dimensions while having noise-level decreases on others. Setting it too permissively allows real regressions through. The right calibration typically involves setting per-dimension thresholds rather than a single aggregate threshold, with critical dimensions (correctness, safety) having strict thresholds and peripheral dimensions (tone, verbosity) having looser ones.

## Using Scores to Direct Improvement

An evaluation harness that produces a single aggregate quality score tells you whether the current prompt is acceptable. A harness that produces per-dimension scores and per-input-category scores tells you where to invest improvement effort.

If the overall score is 3.7 and the dimension breakdown is correctness 4.4, completeness 2.6, format adherence 4.1, and safety 4.3, the improvement opportunity is in completeness. Prompt changes that increase token budget, add explicit instructions about completeness requirements, or provide more complete examples in few-shot context should be tested against the completeness dimension specifically.

If the overall score is acceptable on the standard input categories but falls significantly on a specific category (high-complexity inputs, inputs from a specific user population, inputs near the boundary of the prompt's scope), that category is the improvement target. Adding examples from that category to the prompt or adjusting instructions specifically for it are the interventions to test.

Tracking scores over iterations, keeping a record of the score profile after each significant prompt change, reveals whether the improvement process is producing consistent progress or cycling without net movement. A prompt score that oscillates between 3.3 and 3.7 over eight iterations, despite active improvement attempts, is a signal that the current prompt structure has a ceiling and a different structural approach is worth trying.

## Relationship to Model Selection

The evaluation harness produces a dataset that is useful beyond prompt quality tracking. Running the golden dataset against multiple model configurations (different model tiers, different model providers) with the same scoring rubric produces comparable quality scores across configurations. This is the empirical basis for the model selection optimization described in the companion post on matching model capability to task requirements.

Without the evaluation harness, model selection is based on benchmark performance and subjective impression. With it, model selection is based on performance on the specific tasks and inputs of the specific application. These are often different: benchmark-leading models are not always the best performers for specific use cases, and models that are competitive but not leading on benchmarks may perform equivalently on the tasks that matter while being substantially less expensive.

The harness is the shared measurement infrastructure that makes both prompt improvement and model optimization empirical decisions rather than intuition-driven ones.
