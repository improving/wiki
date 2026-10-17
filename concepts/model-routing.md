---
title: "model routing"
type: "Concept"
description: "Assigning each task or task segment to the cheapest model tier that meets its accuracy requirement."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cost, models, orchestration]
sources:
  - "/sources/checking-the-math-on-the-500-million-ai-spend-story.md"
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/direct-api-integration-for-ai-agents-lessons-from-removing-the-cli-layer.md"
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
  - "/sources/read-the-accuracy-number-next-to-the-cost-number.md"
  - "/sources/tiering-isnt-one-decision-its-five.md"
  - "/sources/using-evaluation-data-to-match-model-capability-to-task-requirements.md"
---

# model routing

Model routing sends each task — or each segment of a task — to the cheapest model tier that meets its accuracy requirement, instead of defaulting every request to a frontier model. Across this corpus, routing is framed as the difference between "agent capability gaps" and "routing gaps": most failures come from sending the wrong work to the wrong model, and savings claims are only half-measured without an accuracy number.

## Key Claims

- Roughly 80% of issue resolution is nearly free; premium tiers buy only the last 15 points of accuracy, so flagship-default teams can spend nearly double a loaded engineer.
- Splitting plan and execution across models cut cost 35–41% at equal performance, and tiering applies at five layers: team design, message pruning, function calls, LoRA routing, and model choice.
- Routing accuracy is a property of a *router paired with a specific workload*; a savings percentage without an accuracy delta on your own data is half an experiment, and aggregate accuracy can hide worse failure rates on the hardest requests.
- Task segmentation by context window and reasoning depth, evaluated on a golden dataset, produces a versioned routing map that should be re-evaluated quarterly and monitored for about 30 days after each change.
- A thin API adapter enables routing and stable interfaces across provider updates, where subprocess CLIs risk prompt corruption and version coupling.
- Token spend stops converting to mergeable pull requests past roughly 30-minute tasks, so decomposing below that wall and routing execution to cheaper models beats upgrading.

## Related

- [token cost](/concepts/token-cost.md) — the spend routing controls
- [Model selection](/concepts/model-selection.md) — choosing among candidates
- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — where spend stops converting
- [time horizon](/concepts/time-horizon.md) — task length limits on cheap tiers
- [Golden Dataset](/concepts/golden-dataset.md) — measuring routing accuracy
- [Tiering Isn't One Decision, It's Five](/sources/tiering-isnt-one-decision-its-five.md) — primary source
