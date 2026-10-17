---
type: Reference
title: "Tags Are a Promise Nobody Enforces"
resource: "https://www.devlinliles.com/tags-are-a-promise-nobody-enforces/"
author: "Devlin Liles"
published: '2026-09-04'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The project kicks off with real energy. Every document gets a tag. Client, project phase, document type, owner, review status. Someone builds a taxonomy diagram with clean parent-child boxes: Contracts under Legal, Legal under Corporate, Corporate at the root. For about six weeks, it works exactly as designed. Then a new project starts that spans two clients, someone tags a document "misc" because none of the categories fit, and the taxonomy starts its slow drift from description to decoration.

That drift isn't a failure of discipline. It's a structural property of the three ways organizations classify information, and each one breaks in a different, predictable place.

A taxonomy is a hierarchy: every item has exactly one home, nested under a parent category, nested under that category's parent, all the way to a root. It's the library card catalog model, and it works beautifully for exactly the kind of information a library holds, where a book genuinely belongs to one shelf. The enterprise version of this model breaks the moment a document belongs to two clients, or a project that got renamed mid-flight, or a category nobody anticipated when the tree was designed. A tree can't represent that a thing has two true parents. Something has to give, and what gives is usually the tagging discipline, quietly, one exception at a time.

An ontology is the other direction entirely: not a single hierarchy but a web of typed relationships. A document doesn't just belong to a category, it references a regulation, which was amended by a later regulation, which governs a process, which a specific team owns. That richness is exactly what makes an ontology powerful for reasoning and exactly what makes it expensive to build and maintain. Someone has to define the relationship types, populate them correctly, and keep them current as the underlying facts change. Few organizations invest at that level before they've proven the value of even the simple version, and a half-built ontology tends to be worse than a well-maintained taxonomy, because now there are relationship types nobody trusts on top of the classification nobody trusts.

A folksonomy skips the design problem entirely: no predefined categories, just whatever tag a person types when they save the file. It scales effortlessly, because nobody has to agree on a scheme in advance. It also produces exactly the mess anyone would predict from letting fifty people freely invent their own vocabulary. The same document gets tagged "onboarding," "new hire," and "employee-setup" by three different people, and a search for any one of those terms misses the other two. A folksonomy is what results by default when nobody builds anything, and most organizations have one whether they meant to or not.

## The real failure isn't the model, it's who's expected to maintain it

Every one of these three models can work. What breaks all three the same way is the assumption baked into the rollout: that a person will maintain the tags after the excitement of the launch fades. Tagging a document correctly takes real judgment and real time, and it's judgment and time spent on work that produces no visible output for the person doing it. The engineer who ships a feature has shipped something. The engineer who correctly tags the documentation describing that feature has done invisible maintenance that nobody notices unless it's missing, and work that's only noticed when it's missing is work that gets skipped the first time a deadline gets tight.

This is the exact pattern that showed up in enterprise data governance years before anyone was talking about AI. In data platform engagements, the original catalog typically depends on a human updating it after the fact, separate from the pipelines actually moving the data, and it degrades the moment shipping a pipeline and documenting that pipeline stop being the same act. The fix that actually holds is a governance tool like Collibra wired directly into the pipeline architecture, so metadata gets populated as a side effect of the pipeline running rather than a separate curation task someone has to remember. I've written elsewhere about how that shift, from passive to active metadata, played out across the data governance industry more broadly. The short version that matters here is narrower: a tag that a system generates as a side effect of work happening survives. A tag that depends on someone remembering to add it decays on a schedule predictable enough to set a watch to.

## What this sets up

None of the three classification models, taxonomy, ontology, or folksonomy, solves the vocabulary-mismatch problem from the last piece in this series either. A perfectly maintained taxonomy still requires someone to know which category a question implies before a tag filter can help them. That's a search problem sitting on top of a classification problem, and it's the reason the next fix organizations reach for isn't better tags. It's a different retrieval method entirely, one that promises to find things by what they're about instead of what they're labeled. That promise is real, and it comes with its own blind spot, which is where this series goes next.

---

*Sources: Hedden Information Management, "Taxonomies vs. Ontologies"; OvalEdge, "Ontology vs Taxonomy: Data Governance and AI Guide" (2026); Improving client engagement practice observations, 2024-2026; "Governance as the Control Plane for AI" (Devlin Liles, 2026, on active vs. passive metadata).*
