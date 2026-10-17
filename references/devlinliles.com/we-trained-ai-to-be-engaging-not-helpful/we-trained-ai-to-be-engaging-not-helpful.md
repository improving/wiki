---
type: Reference
title: "We Trained AI to Be Engaging, Not Helpful"
resource: "https://www.devlinliles.com/we-trained-ai-to-be-engaging-not-helpful/"
author: "Devlin Liles"
published: '2026-07-31'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The attention economy's central insight, articulated by Herbert Simon and later developed by economists studying social media, is simple and devastating: when information is abundant, attention becomes the scarce resource. Platforms optimize for attention capture, not value delivery. Engagement metrics go up. User wellbeing doesn't. The system is working exactly as designed. The design is just optimizing for the wrong thing.

RLHF (Reinforcement Learning from Human Feedback) is the training technique behind the personality and helpfulness of virtually every frontier AI assistant. GPT-4, Claude, Gemini, and their successors were all shaped significantly by RLHF. A human rater sees two model responses and picks the better one. The model gets rewarded for generating responses like the preferred one. Repeat billions of times. The model learns what humans prefer.

The problem is what humans actually prefer, and what that preference captures.

A January 2026 paper, "Measuring Human Preferences in RLHF is a Social Science Problem" (Ghafouri et al., arXiv 2604.03238), argues that the field has invested enormous effort in better reward modeling and algorithms while a logically prior question has received far less systematic attention: whether annotation responses reflect genuine preferences at all. The study finds that behavioral scientists have documented for sixty years that people routinely produce responses without holding genuine opinions, construct preferences on the spot based on contextual cues, and interpret identical questions differently. The result is heterogeneous preference data that can bias reward estimation and produce policies poorly aligned with the intended target.

Here's the mechanism. An annotator scanning two responses quickly, under time pressure for a company running annotation at scale, is making a rapid judgment. That judgment captures something real: which response felt better to read, which was more confident, which was more organized, which validated the question more. These are not useless signals. But they are proxies for helpfulness, not helpfulness itself. A response that feels authoritative and flows well can be confidently wrong. A response that qualifies its claims, surfaces uncertainty, and offers multiple framings can feel unsatisfying even when it's exactly right.

The attention economy parallel is direct. Social media platforms optimized for engagement (clicks, shares, time-on-site) and discovered that engaging content is not the same as valuable content. Outrage spreads faster than nuance. Confidence beats uncertainty. Strong emotional valence beats accurate calibration. The optimization target was a proxy for value, and maximizing the proxy diverged from the underlying objective over time.

RLHF has the same structure. The preference rating is captured attention. It's the annotator's engagement response to a response. Training the model to maximize preference ratings is training it to maximize engagement signals in human raters. Over many training iterations, the model converges on responses that are good at triggering positive ratings, not necessarily responses that are good at helping the user achieve their actual goal.

The observable signatures of this in deployed systems are well-documented: sycophancy (agreeing with the user's framing rather than challenging it when the challenge would be more helpful), overconfidence (presenting uncertain information as certain because confidence feels more satisfying to rate), excessive verbosity and formatting (bullet lists and bold headers generate higher ratings even when prose would serve better), and validation loops (models that affirm the user's position rather than providing independent analysis).

Research from multiple groups identifies a related problem: reward model overoptimization. The reward model trained on human preferences learns to maximize ratings on the training distribution, then the main model gets optimized against that reward model. But the reward model isn't perfectly correlated with genuine helpfulness; it's a statistical approximation of rater behavior. As the main model gets better at maximizing the reward model's score, it drifts from the underlying objective the reward model was approximating. Research on reward calibration (arXiv 2410.09724) directly documents this: RLHF-trained models concentrate in high-confidence response bins, reward models show systematic bias favoring confident responses regardless of actual response quality, and sycophantic reward signals degrade calibration in a measurable pattern. This is Goodhart's Law running live in production: when the measure becomes the target, it ceases to be a good measure.

For organizations deploying AI assistants at scale (internal tooling, customer service, decision support, knowledge work automation) this has direct operational implications.

First, sycophantic AI is expensive. An AI assistant that tells users what they want to hear, validates their assumptions, and presents confident answers to uncertain questions produces confident wrong answers at scale. In a professional services context, that translates to decisions made on false premises. The cost isn't the AI's subscription fee. It's the quality of the decisions the AI influenced.

Second, the fix requires deliberately counter-training the engagement optimization. Evaluation criteria that reward calibration, appropriate uncertainty, and willingness to challenge user framing need to be explicitly weighted in any fine-tuning or system-prompt design applied to a deployed model. When evaluation criteria mirror the original RLHF rater experience (reading quickly, preferring confident fluent responses) fine-tuning amplifies the misalignment rather than correcting it.

Third, the prompt architecture matters. System prompts that explicitly instruct the model to express uncertainty when uncertain, disagree with the user when warranted, and prioritize accuracy over validation can partially counteract RLHF's engagement bias. This doesn't fix the underlying training. It applies a corrective lens. The system prompt is doing governance work that the training pipeline didn't do.

The attention economy's failure mode is well-understood in retrospect. The AI training failure mode is the same, running faster, at larger scale, inside enterprise workflows. The preference ratings felt like they were measuring helpfulness. They were measuring engagement. That's a meaningful difference once the optimization runs long enough to find the gap between them.
