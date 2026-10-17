---
title: "DORA"
type: "Entity"
description: "DevOps Research and Assessment, whose delivery metrics expose how AI-generated code degrades stability and how IDPs shift productivity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [research, devops, metrics, delivery]
sources:
  - "/sources/acceleration-whiplash-the-hidden-metric-ai-adoption-is-breaking.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-05-platform-engineering-idp.md"
---

# DORA

DORA (DevOps Research and Assessment) is the research program behind the delivery metrics — lead time, deployment frequency, change failure rate, and time to restore — used throughout this corpus to judge whether AI adoption is real. Its findings repeatedly show throughput rising while downstream stability falls.

## Overview

- Bugs per developer up 54%; incidents per PR up 242.7%; code churn up 861% as generation outpaces verification.
- 31.3% of pull requests now merge with no human review; mature DevOps teams are not insulated because the problem is structural.
- DORA found internal developer platforms lift individual productivity 8% but drop stability 14%.
- The 2019 "57% observability" figure described elite performers, not the industry median.

## Related

- [DevOps](/concepts/devops.md) — the practice DORA measures
- [Review Bottleneck](/concepts/review-bottleneck.md) — review capacity as a design constraint on generation velocity
- [verification tax](/concepts/verification-tax.md) — the downstream cost of faster generation
- [CNCF](/entities/cncf.md) — the adjacent standards ecosystem
- [Acceleration Whiplash: The Hidden Metric AI Adoption Is Breaking](/sources/acceleration-whiplash-the-hidden-metric-ai-adoption-is-breaking.md) — primary source
