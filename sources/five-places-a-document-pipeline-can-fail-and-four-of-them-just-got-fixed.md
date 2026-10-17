---
title: "Five Places a Document Pipeline Can Fail, and Four of Them Just Got Fixed"
type: "Source Summary"
description: "Decomposes a document AI pipeline into five failure points, reviews 2026 fixes for four, and flags graph-structured content as unresolved."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/five-places-a-document-pipeline-can-fail-and-four-of-them-just-got-fixed/five-places-a-document-pipeline-can-fail-and-four-of-them-just-got-fixed.md"
---

# Five Places a Document Pipeline Can Fail, and Four of Them Just Got Fixed — Summary

**Original source**: `references/devlinliles.com/five-places-a-document-pipeline-can-fail-and-four-of-them-just-got-fixed/five-places-a-document-pipeline-can-fail-and-four-of-them-just-got-fixed.md`

## Summary

A document AI pilot that answers three test questions looks like working retrieval until it meets a real regulatory filing, invoice, or engineering drawing and turns confidently wrong. Liles decomposes the pipeline into five failure points and reviews 2026 research that fixes four: the vision-to-LLM connector, single-encoder limits, vision-token compute cost, and multi-vector index cost. The unresolved fifth is graph-structured content — tables, forms, and drawings where meaning lives in relationships between elements.

## Key Claims

- Connector: AlignVLM maps visual features to a weighted average of the LLM's own text embeddings instead of a naive MLP projection, most improving document understanding.
- Encoder: CoME-VL combines contrastive and self-supervised encoders, beating a single encoder by ~4.9 points on visual understanding and ~5.4 on grounding.
- Compute: HiDrop prunes ~90% of visual tokens at matched performance with training 1.72x faster, making a second encoder affordable.
- Index: attention-guided clustering (Multi-Vector Index Compression) matches or beats an uncompressed multi-vector index under a fixed vector budget.
- GraphVLM finds all three ways of using a VLM over graph-structured content help, but the best still falls short of solved.

## Relevance

Informs [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) pipelines and the [knowledge graph](/concepts/knowledge-graph.md) gap for graph-structured enterprise documents.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced against named arXiv/ICLR/CVPR papers; the "four fixed" framing rests on a single paper per fix.

## Entities Mentioned

- None.

## Concepts Covered

- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the pipeline whose five failure points are analyzed
- [knowledge graph](/concepts/knowledge-graph.md) — graph-structured content the pipeline still handles poorly
