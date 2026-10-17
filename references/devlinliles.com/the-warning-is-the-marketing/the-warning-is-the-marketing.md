---
type: Reference
title: "The Warning Is the Marketing"
resource: "https://www.devlinliles.com/the-warning-is-the-marketing/"
author: "Devlin Liles"
published: '2026-09-25'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

OpenAI told its own safety team that Astra, the model it hasn't released yet, might cross "Critical" capability on cybersecurity, the threshold where a model can find and exploit a zero-day on its own with no human in the loop. That disclosure did two jobs at once, and only one of them was about safety.

The first job is the stated one. Naming a capability threshold before release, in public, on the record, is what a responsible scaling commitment looks like when it's actually followed rather than filed away. Frontier labs made these commitments under real pressure, and a disclosure like this is evidence the commitment has teeth. That part deserves credit, not cynicism.

The second job runs in the opposite direction. Telling the world its unreleased model might independently discover and exploit a zero-day is also telling the world that unreleased model is extraordinarily capable. Nobody has to say that second sentence out loud. The first sentence already said it. A lab announcing its model might be dangerous and a lab announcing its model is powerful are, in this instance, the same announcement, read by two different audiences at the same time.

Industrial safety reporting has run on this exact double meaning for a long time. A chemical plant that publishes a near-miss report showing its process nearly exceeded a critical threshold is doing real safety work, naming a risk and building a record that invites more scrutiny than silence would. The same report also tells every competitor and every customer watching how much throughput that plant is capable of pushing through the line before it gets dangerous. The regulator reads risk. The market reads capacity. Both readings are accurate, and the plant doesn't get to publish one without the other.

Anthropic's cyber-defense expansion landed the same week, from the opposite direction. Where OpenAI disclosed a danger threshold on a model that isn't out yet, Anthropic widened public access to a dangerous capability on a model that already is: Claude Security now runs vulnerability scans on Mythos 5 itself, billed as standard usage, no separate tier required. One company's message is "our next model might be too capable to release without more safeguards." The other's is "our current model is capable enough that we're now selling access to that exact capability, carefully packaged." Different postures, same underlying fact both companies are working from: frontier cybersecurity capability has crossed a line worth talking about publicly, and talking about it publicly is good for business either way.

I treat a vendor-reported benchmark score as a claim, not a fact, until a second party has looked at it, because I've watched enough vendor-reported numbers fail to replicate to know the pattern. A self-reported capability threshold deserves exactly the same treatment, danger claims included. "Critical" is OpenAI's own label, scored against OpenAI's own eval, disclosed by OpenAI about OpenAI's model. That claim still earns the same evaluation baseline I'd insist on for any other capability claim before letting the label decide what the model is allowed to touch.

That's the actual pathway forward here, and it cuts against how most organizations currently make this decision. Gating what a model can do by the vendor's self-reported risk tier is governing by label, the same failure mode that sank a decade of data governance programs run on policy documents nobody's system actually enforced. The fix is the runtime layer that catches a model doing something it shouldn't, independent of what tier the vendor assigned it going in.

The stakes sit at three different altitudes. For the security or compliance lead deciding what a given model gets to touch inside their environment, taking "Critical" or "not yet Critical" at face value means outsourcing a risk decision to a competitor's marketing calendar. For the organization, a runtime enforcement layer that doesn't care which capability tier a model claims is worth more than any amount of vendor-supplied reassurance, because it's the only control that holds regardless of which lab's disclosure turns out to be accurate. For the industry, safety disclosure has become a competitive signal, which means every regulator currently calibrating "responsible AI" requirements against what labs voluntarily disclose is partly grading a marketing document, whether anyone involved intends it that way or not.
