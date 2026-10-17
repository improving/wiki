---
type: Reference
title: "Prompt Engineering Is Just Wittgenstein With a GPU"
resource: "https://www.devlinliles.com/prompt-engineering-is-just-wittgenstein-with-a-gpu/"
author: "Devlin Liles"
published: '2026-08-10'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every time you write a system prompt, you are establishing the rules of a language game. Most teams don't think of it that way, which is why their prompts don't work the way they expect.

Ludwig Wittgenstein's late philosophy collapsed the idea that words have fixed meanings attached to them like labels on objects. In the Philosophical Investigations, he argued that words mean what they mean through use within a form of life — a shared social practice. "Game" doesn't refer to some essential property that chess, soccer, and poker share. It refers to a family of activities related by resemblance, and its meaning is constituted by how it's used in practice. A chess piece has its identity through the rules of the game it participates in. Move it to a Monopoly board and you have a funny-looking token, not a rook.

The practical implication Wittgenstein drew: language is not a system for encoding pre-existing thoughts. It's the medium in which thought occurs. Change the rules of the game, change what's thinkable.

This is not abstract. It's the most accurate description I know of how system prompts work.

When you write "You are a helpful AI assistant," you establish one language game. The probability distribution over the model's next tokens reflects the implicit rules of that game: be agreeable, be comprehensive, hedge uncertain claims, avoid conflict. The model hasn't been told any of those rules explicitly. They're constituted by the framing, just as the rules of chess are constituted by the arrangement of the board, the pieces, and the conventions players bring to it.

Write "You are a senior software engineer reviewing a pull request for correctness and security vulnerabilities" and you establish a different game. Technical precision becomes more probable than conversational hedging. Pointing out a flaw becomes more natural than softening the observation. The model doesn't need to be told "be specific" or "don't pad your response with reassurances." Those behaviors are downstream of the game you've instantiated.

Here's where this gets practically important. Most practitioners think of system prompts as instructions the model follows. That mental model leads to over-engineered prompts full of explicit rules, edge-case handling, and admonishments. "Do not X. Always Y. If the user asks about Z, respond by..."

The more accurate mental model is that a system prompt establishes a probability landscape. It makes certain responses more likely and others less likely. It doesn't guarantee outputs; it biases distributions. A prompt that instantiates the right language game doesn't need to enumerate rules because the game carries them implicitly. A prompt that establishes the wrong game can list all the rules it wants and still produce outputs that violate the spirit of what you intended.

This is why "act as a senior engineer reviewing a PR" outperforms "be specific and technically precise when reviewing code." The first establishes a game with implicit norms that include specificity and precision. The second states properties that the model then has to execute as instructions while operating in whatever default game your other context establishes. The game-based framing is more robust.

The Wittgensteinian frame predicts something testable: prompts that establish clear, coherent language games should generalize better to edge cases than prompts that enumerate rules. The game-based prompt handles the novel case through its implicit logic. The rule-enumeration prompt fails on cases the rule-writer didn't anticipate.

The pathology that follows from not thinking in language games is game contamination. You establish a technical-review game in your system prompt, then the user's message introduces a casual, conversational register, and the model starts hedging and softening in ways your technical game was supposed to prevent. The structural response is to make your game robust enough that it doesn't lose to contamination: strong persona framing, consistent register throughout the system prompt, explicit examples that demonstrate the game's norms.

This is also why few-shot examples work as well as they do. An example is not an instruction; it's a demonstration of the game in play. The model sees what kind of move is expected within this form of life. Wittgenstein's point about meaning-as-use applies directly: show the use, establish the meaning.

Prompt engineering isn't magic or art. It's the structured practice of establishing the right language game for the task. The relevant questions are: what game is this prompt establishing, whether its implicit norms match the intent, and whether it's robust enough to hold its shape when users push against it. That's the whole discipline.
