---
type: Reference
title: "The Watched Workforce"
resource: "https://www.devlinliles.com/the-watched-workforce/"
author: "Devlin Liles"
published: '2026-08-11'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Jeremy Bentham designed a prison in 1791 where a single guard in a central tower could observe all prisoners in surrounding cells, but the prisoners couldn't see into the tower. They couldn't know if the guard was there. Bentham's insight was that you didn't need to actually watch people to control their behavior. You needed them to believe they might be watched. The behavior change was the point. The architecture was the mechanism.

Michel Foucault, writing two centuries later, identified the panopticon as the core technology of modern power: not force, but the internalization of surveillance. When people believe they might be observed, they police themselves. Compliance doesn't require enforcement. It requires the possibility of enforcement.

This is not a historical curiosity. It is the functional description of what enterprise AI monitoring systems are building, often without the designers realizing it.

AI-powered workplace monitoring has scaled fast. As of 2025, 78% of US employers use online monitoring tools and 61% deploy AI-powered analytics to measure employee productivity or behavior, according to ExpressVPN's 2025 survey of 1,500 employers. In corporate environments, this includes keystroke logging with AI analysis, communications monitoring for tone and sentiment, productivity metrics derived from application activity, and AI-assisted review of meeting transcripts and collaboration tool usage. The stated purpose is usually productivity, compliance, or security.

The panopticon problem is that the stated purpose and the actual effect operate on different mechanisms. A compliance monitoring system designed to catch actual violations has a specific scope: it activates when violations occur. A panoptical system, by contrast, affects behavior before any violation. The employee who believes their communications are being analyzed for sentiment doesn't change behavior when they get flagged. They change behavior because they might get flagged. This is a meaningful distinction for what actually happens inside the organization.

Research on surveillance and behavioral effects documents patterns that should inform how organizations think about AI monitoring design. Studies on monitored environments consistently find increased self-censorship, reduced creativity in ideation tasks, decreased willingness to raise concerns or dissent, and higher cognitive load from continuous privacy management. One 2024 study framing AI surveillance as a socio-technical system found that individuals who perceive higher psychological pressure due to surveillance exhibit heightened behavioral vigilance and restraint even when no violations are occurring or expected.

The practical consequence: AI monitoring systems designed for compliance may be systematically reducing the organizational behaviors you most need. The employee who won't raise concerns in a monitored Slack channel. The team that stops brainstorming freely in a meeting-transcribed video call. The manager who edits their written feedback to appear unambiguously positive under sentiment analysis. The loss here isn't just personal freedom. It's organizational signal. The information that monitoring was supposed to surface gets suppressed by the monitoring itself.

Foucault called this disciplinary power: not the overt exercise of force but the structuring of an environment so that subjects discipline themselves according to assumed norms. AI systems are extremely efficient disciplinary mechanisms because they're constant, scalable, and perceived as objective. A human manager who spots-checks communications creates a panopticon. An AI that monitors continuously and produces behavioral analytics creates a more complete one.

The design question for organizations deploying AI monitoring is not just "is this system accurate?" That's the question about the enforcement mechanism. The more important question is "what behavior does the possibility of this system induce?" These are different questions with different answers. A highly accurate monitoring system can still produce more behavioral suppression than a less accurate one, because the perceived certainty of detection amplifies the panoptical effect.

This has concrete governance implications. Scope matters enormously. A narrowly scoped system monitoring for specific, enumerated compliance violations in specific high-risk contexts creates a defined perimeter of potential observation. Employees know what's in scope and what isn't. A broadly scoped system with AI analyzing "all communications for risk signals" creates an effectively unbounded perimeter. The behavioral modification from the second is orders of magnitude larger than the first, even if the actual enforcement rate is similar.

Transparency reduces the most damaging panoptical effects. When employees know exactly what's being monitored, by what criteria, reviewed by whom, and with what consequences, the uncertainty that drives maximal self-censorship drops. This doesn't eliminate behavioral modification; visibility still changes behavior. But it limits the effect to the scope of actual monitoring rather than the scope of imagined monitoring.

The metrics you use to evaluate the system matter just as much. If you measure the monitoring system by detections and interventions, you'll optimize for detection sensitivity. If you measure by organizational health metrics (psychological safety scores, willingness to raise concerns, innovation output) you'll capture the second-order effects the panopticon imposes.

The organizations that deploy AI monitoring thoughtfully will narrow its scope, maximize its transparency, and measure its second-order effects. The ones that deploy it broadly and opaquely will get compliance theater: a workforce that looks compliant under the monitoring lens while the organizational dynamics that actually produce risk (suppressed concerns, concealed problems, risk-avoidant communication) get stronger rather than weaker.

Bentham's guard doesn't need to be watching. The design is the control. Make sure you're designing what you intend.
