---
type: Reference
title: "When Small Mistakes Compound: Building Systems That Survive Imperfect AI"
resource: "https://www.devlinliles.com/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai/"
author: "Devlin Liles"
published: '2026-07-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every AI system your organization deploys makes mistakes. That is not a knock on the technology. It is a property of it. The question that separates a successful deployment from an expensive embarrassment is not whether the model errs. It is what happens to a small error once it is made, and whether your processes are built to catch it before it becomes a large one.

Most organizations are not built for this. They evaluate an AI tool the way they would evaluate a calculator: does it get the right answer. That framing works when the tool does one discrete thing. It breaks the moment you let AI run a process, because in a process each output becomes the next step's input, and a small error early in the chain becomes the foundation everything after it is built on. A 1% mistake rate per step sounds trivial. Across a fifty-step workflow it means roughly two of every five runs contain a compounded error. Across a hundred steps, the majority do. The arithmetic of long-running automation is unforgiving, and it does not care how impressive the demo was.

This is a leadership problem before it is a technical one. The engineers can tell you why errors compound. Only the business can decide where that risk is acceptable, who is accountable when it lands, and what the organization will spend to contain it. This piece is about those decisions and the systems they require.

## The core risk: drift you cannot see

A compounding error is dangerous precisely because it is quiet. The system does not crash. It does not throw a red alert. It produces a confident, fluent, professional-looking result that happens to be built on a mistake made forty steps ago. By the time anyone notices, the error is woven through everything downstream of it, and untangling which parts are real becomes its own project.

Picture an AI agent processing invoices. It misreads one vendor's payment terms early in a batch. Nothing breaks. It keeps working, applying that wrong assumption to every related record, generating a clean report that looks exactly like a correct one. The failure surfaces weeks later in a reconciliation, after the wrong payments have gone out. The model was 99% accurate. The 1% compounded silently through the rest of the run, and the organization absorbed the cost.

This pattern repeats across every domain where AI runs a multi-step process: a research summary that subtly shifts its premise partway through and reaches a conclusion the source documents never supported, a customer-facing workflow that makes one wrong classification and then treats it as established fact, a code-generation pipeline that produces something that runs and is wrong. The common thread is that the output looks finished. Polish is not correctness, and AI is extraordinarily good at producing polish.

The strategic implication is direct. You cannot manage this risk by trusting the output to look right, because looking right is the one thing a compounding error reliably does. You manage it by building systems that assume errors happen and are designed to catch and contain them.

## Decide where autonomy is allowed

The first and most important decision is not technical. It is a judgment about where you are willing to let AI run unsupervised, and that judgment should be governed by two questions: how expensive is a mistake here, and how easily can it be reversed.

Those two questions define a simple map. Work that is cheap to get wrong and easy to undo is where autonomy belongs. Draft an email, summarize a meeting, generate a first pass at a document, propose a categorization. If the AI errs, a human notices in seconds and the cost is a few wasted minutes. Let it run. Demand speed, accept the occasional miss, and move on.

Work that is expensive to get wrong or hard to reverse is where autonomy is a liability no matter how good the model looks in testing. Moving money, sending communications to customers under your brand, changing production systems, making decisions with legal or regulatory weight, anything that touches someone's health, safety, or livelihood. Here a single compounded error can cost far more than the entire efficiency gain the automation was supposed to deliver. These steps need a human in the loop, and the human needs to be positioned at the decision, not rubber-stamping a batch after the fact.

The mistake organizations make is treating autonomy as all-or-nothing. They either keep a human reviewing everything, which destroys the efficiency case, or they automate end to end, which exposes them to compounding risk on the high-consequence steps. The right design is selective. Automate the cheap, reversible majority of the work. Place human judgment precisely on the few steps where an error is expensive or permanent. The art of deploying AI well is largely the art of drawing that line in the right place and revisiting it as the system earns or loses trust.

## Build checkpoints into the process

A long automated process with no internal checks is a single point of failure stretched across many steps. One error anywhere in the chain can corrupt the whole result, and you find out at the end or not at all. The fix is to break the process into segments with verification between them, so an error gets caught close to where it happened rather than after it has propagated through everything downstream.

Think of it the way a manufacturing line uses quality gates. You do not inspect only the finished product. You check at stages, because catching a defect early is cheap and catching it after it is built into the final assembly is not. AI processes deserve the same treatment. After a meaningful chunk of work, the system should validate before it continues: does this output match the expected format, does it pass a basic sanity check, does an independent check agree with it, does it reconcile against a source of truth. A step that fails its gate stops the line before the error spreads.

This changes the economics of failure entirely. Without checkpoints, a compounded error means redoing the whole run and absorbing whatever damage already escaped. With checkpoints, it means catching the problem at stage three and rerunning one segment. The same model with the same error rate produces a dramatically more reliable system, because the architecture refuses to let small errors travel far. Checkpoints are an operational investment, and on any high-stakes process they pay for themselves the first time they catch something.

## Ground the system in reality, repeatedly

AI systems drift because they reason from their own previous outputs, and each step carries forward whatever errors the last one introduced. The most effective antidote is to force the system to check itself against external reality at regular intervals rather than trusting its own accumulated picture.

In practice this means the system should pull fresh, authoritative data instead of relying on what it generated earlier. It should read the actual current state of a record before acting on it. It should cite and link to real sources a human can verify. The more often the process touches verified ground truth, the shorter the window in which any single error can compound undetected. A system that re-grounds every few steps simply has less room to drift than one that runs fifty steps on its own assumptions.

For leaders, the practical test is to ask of any AI deployment: where does this system get its facts, and how often does it check them against something authoritative. If the answer is that it generates a long result from a single starting prompt and never looks back at reality, you are carrying compounding risk whether you can see it or not. If the answer is that it continuously validates against trusted data, the risk is structurally contained.

## Make accountability explicit

Automation has a way of diffusing responsibility. When a human makes a costly mistake, ownership is clear. When an AI process makes one, the instinct is to treat it as a system glitch with no owner, which is exactly how a small error grows into a large unexamined one. Strong AI governance assigns a human owner to every automated process, accountable for its outcomes the same way they would be for a team's work.

That ownership has to come with the means to exercise it. The owner needs visibility into what the system is doing, the ability to stop it, and a clear escalation path when something looks wrong. They need to know the failure modes of the process they own and the conditions under which it should hand control back to a person. Accountability without visibility and control is a name on an org chart, not governance.

This also shapes how you talk about AI internally. A culture that treats AI output as authoritative because it came from the machine is a culture primed to let compounding errors through, because no one feels empowered to question a confident result. A culture that treats AI as a capable but fallible contributor whose work gets reviewed at the points that matter is a culture that catches problems early. The difference is set by leadership, in the expectations you establish and the questions you reward people for asking.

## Measure the right thing

Organizations routinely measure AI the wrong way and draw false confidence from it. They test the tool on isolated tasks, see strong accuracy, and conclude it is ready for a long automated process. The isolated-task score and the full-process success rate are different numbers, and the gap between them is the compounding tax. A tool that is 98% accurate per step is not 98% reliable across a fifty-step workflow. It is closer to 36%.

The metric that matters is end-to-end success across the full process at the length you actually run it, measured on realistic inputs rather than clean demo cases. Before you scale an AI workflow, run it at production length and count how often the complete result is correct, not how often each individual step is. Watch how that number falls as the process gets longer. That decay curve tells you where the safe horizon ends and where you need to break the process up, add checkpoints, or keep a human involved. It is the most honest picture of risk you can get, and it is the one most pilots never produce because they stop measuring at the step level.

Pair that with monitoring once the system is live. Log what the process does at each stage so that when something goes wrong you can find where it left the rails and fix that specific failure, rather than losing trust in the whole system. Observability turns a vague unease about AI reliability into a concrete, fixable list of failure points.

## The shape of a system that holds

The organizations that get durable value from AI are not the ones with the most advanced models. They are the ones that built processes around the assumption that the model will sometimes be wrong. They automate the cheap and reversible work aggressively and keep humans on the expensive and irreversible decisions. They break long processes into checked segments so errors get caught early. They ground their systems in verified reality at regular intervals. They assign clear human ownership and give those owners visibility and a stop button. They measure end-to-end success at real length and watch the decay curve instead of trusting single-step scores.

None of this requires waiting for a better model. It is process and systems work, and it is squarely a leadership responsibility, because the decisions it depends on are decisions about acceptable risk, accountability, and where the organization is willing to spend to contain a failure. The model will keep improving. The compounding problem will not disappear, because the moment a model gets good enough to trust with longer processes, you will hand it longer processes, and the arithmetic catches up again. The advantage goes to the organizations that learned to build for imperfection early, and kept building for it as the stakes rose.
