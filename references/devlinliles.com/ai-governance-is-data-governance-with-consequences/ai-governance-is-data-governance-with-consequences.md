---
type: Reference
title: "AI Governance Is Data Governance With Consequences"
resource: "https://www.devlinliles.com/ai-governance-is-data-governance-with-consequences/"
author: "Devlin Liles"
published: '2026-07-31'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The framing of AI governance as a separate discipline from data governance is a mistake. Most organizations making it will discover this the hard way, because the EU AI Act's high-risk obligations activate on August 2, 2026, and the first question regulators will ask isn't about the model. It's about the data.

Article 10 of the EU AI Act requires that training, validation, and testing datasets for high-risk AI systems be "relevant, sufficiently representative and, to the best extent possible, free of errors." That is a data governance requirement. Not an AI requirement. Not an algorithm requirement. A data governance requirement with fines up to €35 million or 7% of global turnover attached to it.

If you don't have data governance, you don't have AI governance. If your data governance is the bolt-on, passive, committee-driven variety that the last six posts have documented as structurally insufficient, you definitely don't have AI governance. The 63% of organizations that Gartner found either lacking or unsure about their data management practices for AI aren't underprepared for AI. They're underprepared for regulated deployment, and they have about three months of runway left before that matters in the EU.

## What NIST Asked and Didn't Answer

NIST released AI RMF 1.0 in January 2023. It organized AI risk management around four functions: Govern, Map, Measure, Manage. The framework is voluntary, thorough, and useful. It's also incomplete in a specific way that matters.

Forrester's analysis noted that data governance "does not have an explicit reference" in the AI RMF. Data stewards are missing from the defined roles. The framework describes what you should do with AI risk (identify, assess, monitor, respond) but doesn't prescribe the data governance infrastructure that makes those activities executable. CDOs and data leaders were left to extend their existing governance programs to cover AI without explicit guidance on what that extension should look like.

The gap is not theoretical. A model that surfaces in a bias assessment as producing disparate outcomes is only actionable if you can trace which training data it learned the pattern from. That trace requires lineage. Lineage requires a governance infrastructure that captures it. Without that infrastructure, the AI RMF's Map and Measure functions are aspirational rather than operational.

The EU AI Act is more prescriptive on the data side. The explicitness is the point: you can't claim to comply with Article 10 by asserting that your training data is probably fine. You need demonstrable evidence of data quality practices, representativeness assessments, and error mitigation processes. That evidence comes from data governance records, not from the model development process.

## What We Built at BCBSM

Blue Cross Blue Shield of Minnesota operates under HIPAA and HITRUST, which established the governance baseline before AI entered the picture. When Improving built out the AI/ML platform on Databricks, the governance architecture we'd already put in place for the data was what made governed AI deployment possible.

Unity Catalog was the mechanism. Every Gold-layer dataset that AI models trained on was governed by Unity Catalog: access-controlled, lineage-tracked, and audit-logged. When the data science team built a model, Unity Catalog recorded which data assets fed the training job. The MLflow Model Registry captured the model lineage: training data version, evaluation metrics, approver identity, and deployment stage. The combination gave BCBSM an auditable answer to "what data trained this model and who approved its deployment to production."

The AI governance framework we co-designed with BCBSM's AI Technical Sub-Committee formalized what approval required: a structured risk assessment covering data privacy, bias and fairness, transparency, compliance, and continuous improvement. Every AI use case that advanced to production went through a documented intake process with LOB sponsorship and data governance review. This wasn't a bureaucratic gate for its own sake. It was the mechanism that converted informal AI experimentation into a practice that the compliance and legal teams could stand behind.

The HIPAA AI enablement procedure was the operational version of that governance. Four steps: BAA confirmation, compliance profile verification, admin-level feature enablement, documented decision log. Every AI feature activation has a traceable approval record. When a regulator asks "how did you govern this," the answer is in the system, not in someone's memory.

That is what AI governance looks like when it's built on a real data governance foundation. Not aspirational framework alignment. Auditable operational practice.

## Feature Stores and the ML Data Problem

Classic data governance (tables, schemas, access controls) doesn't map cleanly to ML features. A feature store manages a different kind of data asset: derived attributes computed from raw data and used as inputs to models. Feast, open-sourced in November 2020, and Tecton, the commercial product from the team behind Uber's Michelangelo, added a data management layer specifically for ML features, with versioning and lineage built in.

The governance problem features introduce is point-in-time consistency. A model trained on features computed as of March 2024 needs to be served with features computed the same way in production. A governance failure here (serving features computed with different logic than the training features) produces a model that doesn't behave the way it was evaluated. The error is silent and hard to detect. Feature stores solve it by making the feature computation logic versioned and traceable.

If you're building ML systems without a feature store, you're managing this problem informally. That's workable at small scale. At the scale where regulated AI governance becomes necessary (multiple models, multiple teams, multiple versions in production simultaneously), informality is the source of exactly the kind of undocumented data governance failure that regulators are looking for.

## The Two Clocks

There are two regulatory clocks running on AI governance. The EU AI Act's high-risk obligations are the harder deadline: August 2, 2026. If you operate in or sell into the EU and your AI systems are in scope, the governance controls need to be in place before that date, not started on that date.

The longer-horizon risk is the Gartner prediction: through 2026, organizations will abandon 60% of AI projects that are unsupported by AI-ready data. That's not a regulatory consequence. It's an operational one. AI built on data that isn't clean, well-governed, or traceable produces AI that doesn't work reliably enough to trust in production. The business consequence is wasted investment and eroded confidence in AI as a capability.

The honest prescription: if you have data governance gaps, close them before you scale AI. Not because the regulators are coming (though they are), but because AI governance is data governance with the consequences turned up. The quality problems that cost organizations $12.9 million per year in poor data quality cost significantly more when they produce AI outputs that are wrong, biased, or legally non-compliant.

The window to build the foundation the right way is narrower than most organizations think.

---

*Sources: NIST AI Risk Management Framework 1.0 (January 26, 2023; Elham Tabassi); EU AI Act (Regulation 2024/1689; in force August 1, 2024; high-risk obligations August 2, 2026); Forrester analysis of NIST AI RMF and data governance; Gartner survey of 1,203 data management leaders (July 2024); Feast open-source (November 2020); Improving/BCBSM Xcelerate Health Data & AI Platform case study.*
