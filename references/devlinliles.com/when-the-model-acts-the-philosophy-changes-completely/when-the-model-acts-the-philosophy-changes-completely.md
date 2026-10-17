---
type: Reference
title: "When the Model Acts, the Philosophy Changes Completely"
resource: "https://www.devlinliles.com/when-the-model-acts-the-philosophy-changes-completely/"
author: "Devlin Liles"
published: '2026-08-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most enterprise teams evaluating AI still think they're buying a very good search engine. They're not. They're potentially deploying an agent that acts in the world. That distinction matters more than anything else in how you govern these systems.

J.L. Austin laid out the foundation in 1955 in a series of lectures at Harvard. He called attention to a class of utterances that don't describe states of affairs; they create them. When a judge says "I sentence you to five years," nothing is being described. The sentence is being imposed. When two people say "I do" in a wedding ceremony, the marriage isn't being reported on; it's coming into existence. Austin called these performatives, and his student John Searle later developed the broader framework of speech act theory: language doesn't just represent the world, it does things in the world.

This distinction between saying and doing was philosophical when Austin first made it. Agentic AI has made it an operational design question.

A language model giving you a wrong answer is a problem. Depending on the use case it might be a serious problem. But it's recoverable. You read the output, you catch the error, you don't act on it.

A language model with tool access that sends an email, commits code, modifies a database record, or submits an API request is performing in Austin's sense. The utterance — the model's decision to invoke the tool — doesn't describe an action. It is the action. Incorrect is no longer recoverable the same way.

This isn't abstract risk management language. I've seen it concretize in production systems. A model with access to a ticketing system that creates duplicate tickets. An agent with calendar write access that books meeting conflicts. An orchestration workflow with file system access that overwrites the wrong file. These aren't hypothetical. They're the failure modes that show up when teams give models tools before they've built the governance architecture to constrain how those tools get used.

Austin actually distinguished three acts within any speech event: the locutionary act (what was said), the illocutionary act (what was done in saying it), and the perlocutionary act (the effect produced). For our purposes the relevant distinction is simpler: read-only versus world-changing.

A model that retrieves and summarizes information is almost entirely locutionary. Its outputs describe; they don't constitute. A model that drafts a message is still largely locutionary: the draft exists but nothing has been done with it. A model that sends the message has crossed into the performative. A model that sends the message, then updates a CRM record to reflect the outreach, then schedules a follow-up on the calendar is chaining performatives. Each action changes the state of a system that subsequent actions or human decisions will have to work around.

The governance implication is that your control architecture needs to match the performative depth of the agent. A read-only retrieval agent needs evaluation and output monitoring. An agent that chains write operations across multiple systems needs intent validation, tool permission scoping, confirmation gates on high-consequence actions, audit logging with rollback capability, and human escalation paths for edge cases.

Most teams build the evaluation for the locutionary case and then promote the system to performative use without revisiting the governance architecture. That's the specific failure pattern to prevent.

Anthropic's Constitutional AI approach — where models are trained with explicit principles about what they should and shouldn't do — is more interesting when you read it through Austin's framework. The constitution isn't a filter on outputs. It's an attempt to make certain performatives less probable at training time. The model is trained to treat certain action-types as out of bounds, not because the output is flagged after generation, but because the model's disposition toward those actions is shaped during training.

This is the right direction. Tool-use governance enforced only at runtime, through permission systems and output filters, is playing defense. Governance that shapes the model's dispositions — making it less likely to invoke a destructive tool without confirmation, more likely to surface uncertainty before acting — is a more robust architecture.

The question I ask at the start of every agentic AI engagement is: what is the worst wrong action this system could take, and how much would it cost to reverse it?

If the answer is "send a slightly off-tone email" and it costs 30 seconds of a human's attention to follow up, the governance overhead of confirmation gates might not be worth it. If the answer is "delete a production database record" or "expose a customer's data in a message to the wrong recipient," you need gates, logging, and rollback before you put the agent in front of users.

Austin's insight was that some utterances are actions. The engineering corollary is that some model outputs are events with real-world consequences that don't wait to be reviewed. The alignment stakes for an agent that sends emails and executes code are categorically different from the alignment stakes for one that summarizes documents. Governance architecture that doesn't reflect that difference isn't designed for the system it's governing.
