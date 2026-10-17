---
type: Reference
title: "Parallel Decode Is the Inference Bet Nobody&#x27;s Marketing Yet"
resource: "https://www.devlinliles.com/parallel-decode-is-the-inference-bet-nobodys-marketing-yet/"
author: "Devlin Liles"
published: '2026-09-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Google DeepMind spent real training compute this summer on a bet that has nothing to do with parameter count. The question behind it: can a language model write output in parallel instead of one token at a time. The paper, titled the DiffusionGemma Technical Report, posted to arXiv on July 31, answers with a number that stopped me mid-scroll. On a single H100, the model generates roughly 1,500 tokens per second. Compare that against a well-optimized autoregressive model running the same class of hardware, where throughput tops out in the low hundreds of tokens per second once the KV cache and the sequential dependency chain take their cut. That gap is the whole story.

Every serving framework built in the last three years argues for how to make autoregressive decoding faster without touching the architecture underneath it. vLLM's continuous batching, TensorRT-LLM's kernel fusion, and the speculative decoding schemes that guess several tokens ahead and verify them in one pass all accept the same premise: a model produces one token, looks at it, and produces the next one, and the serving stack's job is to hide the cost of that chain as well as it can. DiffusionGemma attacks the chain directly. It generates a full span of tokens at once and refines them together, so there's nothing sequential left to hide.

The analogy is image diffusion. Those models start from noise spread across the whole canvas and denoise all of it together, pass by pass, instead of building a picture pixel by pixel from one corner. Apply that idea to text and you get a model that proposes a whole block of tokens at once and iteratively cleans it up, committing to token one and token forty in the same pass. That trade gives up the guarantee autoregressive models get for free, each token conditioned on everything that came before it, in exchange for raw parallel throughput. It's a different computational bet than a faster version of the same one.

For that bet to pay off past a single benchmark, a few things have to hold. Quality has to stay competitive with autoregressive models of the same size once generations run long, past a paragraph, into the length where reasoning chains and multi-step outputs actually live. A short completion is the easy case for any parallel scheme. The hard case is a document or a function that has to stay internally consistent for two thousand tokens without the left-to-right guardrail autoregressive models get built in.

The tooling has to catch up too, and that's not a small ask. Every serving framework in production today assumes a KV cache, assumes speculative decoding's verify-and-accept loop, assumes batching logic built around variable-length sequential generation. None of that transfers cleanly to a model that wants to denoise a block of tokens at once. Someone has to build the vLLM equivalent for parallel decode. Until they do, DiffusionGemma's 1,500 tokens per second lives in a research paper's benchmark harness, out of reach of any startup with an API key.

That gap between benchmark and endpoint is what turns 1,500 tokens per second into a signal worth naming. Google DeepMind spent training compute, the scarcest resource a frontier lab has, on an architecture that abandons the autoregressive assumption every competitor's roadmap is still built on. Labs do not burn training runs on curiosities; they burn them on bets they think will matter in eighteen months, once the marketing has caught up to the research.

Nobody is marketing parallel decode yet because there is nothing to sell. A serving vendor can't put an architecture the ecosystem can't yet serve at scale on a keynote slide, and speculative decoding, quantization, and smarter KV cache management are already generating revenue today. Parallel decode is a bet on next year's story, made quietly, while everyone else's marketing budget stays pointed at squeezing more out of the token-by-token model that has run this industry since GPT-3. The quiet bets are usually the ones worth watching.
