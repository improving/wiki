---
title: "neural networks"
type: "Concept"
description: "Layered models that learn representations from data, whose weight dynamics can be studied but remain hard to interpret."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, data, engineering]
sources:
  - "/sources/exploring-the-learning-secrets-of-neural-networks.md"
  - "/sources/5-key-terms-when-talking-about-ai.md"
  - "/sources/key-fundamentals-of-ai-development.md"
  - "/sources/back-to-basics-the-value-of-statistical-machine-learning-today.md"
  - "/sources/improving-is-harnessing-the-power-of-ai.md"
---

# neural networks

Neural networks are brain-inspired layered algorithms that learn representations from data; deep learning refers to a network with more than three layers. They underpin speech recognition, translation, content generation, and computer vision, and this corpus treats their weight dynamics as both a route to understanding and a stubborn interpretability problem.

## Key Claims

- Neural nets are brain-inspired layered algorithms; deep learning is any neural net with more than three layers (at least two hidden layers).
- In an MNIST/fMNIST experiment, a three-layer network (28x28 input, two 512-neuron layers, 10-class output) trained over 10 epochs of 60,000 batches showed Shannon entropy falling while statistical complexity rose — weights moving from disorder to order.
- Weights start uniformly distributed and develop band-like patterns along columns; the third layer keeps refining even when entropy stays flat.
- Deep learning rests on convolutional neural networks for visual data and recurrent neural networks for sequential data like text and speech.
- Common languages are Python, Java, and C++; common frameworks are TensorFlow, PyTorch, and Keras.
- Interpretability remains the recurring challenge: deep-learning decisions are hard to explain, which is why statistical checks still matter.

## Related

- [statistical machine learning](/concepts/statistical-machine-learning.md) — classical methods that validate them
- [interpretability](/concepts/interpretability.md) — reading learning from weights and decisions
- [anomaly detection](/concepts/anomaly-detection.md) — a suggested application of entropy measures
- [AI bias](/concepts/ai-bias.md) — bias arising in data and training
- [AI literacy](/concepts/ai-literacy.md) — the vocabulary for talking about models
