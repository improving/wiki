---
title: "Your Coding Agent Doesn't Know What Your Last Three Engineers Knew"
type: "Source Summary"
description: "Coding agents lack the unwritten conventions in engineers' heads; a shared memory layer helps only if someone captures it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew.md"
---

# Your Coding Agent Doesn't Know What Your Last Three Engineers Knew — Summary

**Original source**: `references/devlinliles.com/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew.md`

## Summary

The post opens with a coding agent shipping a change that passed every lint rule and style check but would have taken down production in about four hours, because the bug lived in an undocumented convention — a pinned dependency whose reason was known to three engineers, two of whom had left. Coding agents read the repository correctly but miss the incident-channel conversations behind such decisions, and their clean-looking pull requests don't trigger the memory that makes a senior reviewer pause. The proposed organizational memory layer only works if someone does the human work of capturing that knowledge first.

## Key Claims

- The undetected bug was a convention nobody wrote down: a dependency pin from an incident eight months earlier, understood by three people, two already gone.
- The agent had the repo, style guide, lint config, and full commit history and read them correctly — but not the conversation that justified the pin.
- A junior's bad PR looks wrong and invites scrutiny; an agent's bad PR looks clean and idiomatic, so reviewers have no reason to slow down.
- A shared memory layer surfaces only knowledge that was written down first, in language specific enough to still mean something eighteen months later.
- Building it is a people problem in systems-design clothing: exit conversations and retros must capture actual decisions, which most organizations don't budget time for.

## Relevance

Informs [tacit knowledge](/concepts/tacit-knowledge.md) and the design of organizational memory layers for coding agents.

## Quality

Practitioner blog post by Devlin Liles, built on a single illustrative anecdote. The anecdote is compelling but undocumented, and the argument is reasoned rather than empirically measured.

## Entities Mentioned

- None.

## Concepts Covered

- [Tacit Knowledge](/concepts/tacit-knowledge.md) — the unwritten conventions agents cannot retrieve
