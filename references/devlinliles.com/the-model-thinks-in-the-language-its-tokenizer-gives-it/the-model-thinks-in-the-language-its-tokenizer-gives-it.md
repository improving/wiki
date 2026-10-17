---
type: Reference
title: "The Model Thinks in the Language Its Tokenizer Gives It"
resource: "https://www.devlinliles.com/the-model-thinks-in-the-language-its-tokenizer-gives-it/"
author: "Devlin Liles"
published: '2026-08-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

If a language model can't represent a concept as tokens, it can't reason about it. That sentence sounds philosophical. It's an engineering constraint.

The Sapir-Whorf hypothesis (linguistic relativity) holds that the language you speak shapes the thoughts available to you. Hopi has no tense structure equivalent to English; speakers conceptualize time differently. Mandarin has a richer vocabulary for familial relationships; its speakers parse those relationships with more precision than English speakers who reach for "uncle" and stop. The claim isn't that language makes certain thoughts impossible. It's that language makes certain thoughts easier or harder, more or less natural, more or less likely to surface.

Every modern large language model has a version of this problem baked into its architecture. It's called tokenization, and most teams deploying AI systems don't think about it until something breaks in a way that seems inexplicable.

Byte-pair encoding, the dominant tokenization approach in GPT-style models, works by iteratively merging the most frequent character pairs in a training corpus until a target vocabulary size is reached. The result is a vocabulary where common English words get their own tokens, while unusual words, foreign-language strings, code, and structured data get fragmented into whatever subword chunks happened to be frequent enough during training.

This is not a neutral engineering choice. It encodes a prior about what the model will be asked to process. English prose, where BPE was implicitly optimized, gets treated efficiently. Numbers don't.

The number "2024" might be encoded as a single token or as "20" and "24" depending on the model. The IP address "127.0.0.1" fragments into four or more tokens with no structural relationship to the actual dot-separated octets. A phone number becomes an arbitrary sequence of subword fragments that obscure the positional structure a human uses to parse it.

This fragmentation isn't just inefficient. It actively impedes reasoning. Arithmetic requires understanding positional structure: the "2" in "2024" is in the thousands place. A tokenizer that bundles "20" and "24" together obscures exactly that structure. The model doesn't get to see the number as a sequence of meaningful digit positions. It gets whatever chunks frequency analysis produced.

In 2024, Singh and Strouse published work on how tokenization impacts arithmetic in frontier LLMs and made this concrete. They showed that right-to-left digit tokenization — processing numbers from least significant to most significant digit — improved arithmetic accuracy on multi-digit addition tasks by over 22 percentage points on GPT-3.5, taking it from roughly 75% to roughly 98%. GPT-4 showed a smaller but still significant improvement. Same model, same training data. Different tokenizer. Twenty-two points.

That's not a rounding error or a benchmark quirk. That's the tokenizer functioning as a cognitive constraint on what the model can do. The model's "reasoning ability" on arithmetic is partly a property of the tokenizer, not just the weights.

Google Research confirmed the pattern: manipulating digit-grouping tokenizations produces substantial accuracy shifts and altered error distributions in state-of-the-art models. The core finding: model reasoning "frequently adheres to tokenizer-imposed structure rather than learned abstract computational principles." The model isn't doing math in an abstract representation. It's pattern-matching in the space its tokenizer created.

I see this in enterprise AI deployments more than clients expect. The most common manifestation is financial data. A model that handles natural-language questions about business strategy brilliantly will produce unreliable arithmetic when asked to reason over tabular financial data inline. The team concludes the model "isn't good at math." Sometimes that's true. Often they've handed the model numbers in a format that the tokenizer fragments in ways that make positional reasoning unnecessarily hard.

Date parsing is another common failure point. "Q3 2025" might be tokenized as ["Q", "3", " 202", "5"] or some other arbitrary chunk depending on the model. The model has no reliable structural access to the year, the quarter separator, or their relationship. Ask it to sort by date or compute time deltas and you get inconsistent results that look like reasoning failures but are partly tokenization failures.

Code is a third domain. Python code tokenizes reasonably because BPE was trained on GitHub. But domain-specific languages, configuration files with unusual syntax, or custom identifiers that don't appear in training data get fragmented in ways that impede the model's ability to understand them structurally.

Pre-processing is the lowest-cost intervention. Transforming numbers, dates, and structured strings into a format the tokenizer handles well before they reach the model — digit-by-digit representation of numbers, explicit delimiters, normalized date formats — is low-tech and high-leverage.

Model selection is the medium-term lever. Newer tokenization approaches address some of these structural limitations. Meta's Byte Latent Transformer uses entropy-based dynamic patching. BoundlessBPE achieves improved bytes-per-token efficiency and reduced FLOPs per byte. For numerically intensive use cases, tokenizer architecture is a selection criterion alongside parameter count and benchmark performance.

Evaluation design closes the loop. Evaluation harnesses built to catch tokenization-sensitive failure modes explicitly — tested against the actual data formats, number representations, and date conventions in the deployment — expose failures that general benchmarks don't surface. The failure mode is systematic, not random. It's findable if the evaluation is designed to find it.

The deeper point is that tokenization is not infrastructure. It's a design choice with cognitive consequences. The 20th-century linguists were debating whether Inuit languages have more words for snow. The 21st-century version of that debate is about whether a tokenizer has the right vocabulary structure for the conceptual domain the model is being asked to navigate. The model thinks in the language its tokenizer gives it.
