---
type: Reference
title: "The Auto-Send Button Nobody Had Earned Yet"
resource: "https://www.devlinliles.com/the-auto-send-button-nobody-had-earned-yet/"
author: "Devlin Liles"
published: '2026-10-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a sales-proposal drafting tool with two modes. The first, suggest mode, drafts a proposal section and waits for the account executive to approve it before anything moves forward. The second, auto-send mode, drafts a proposal and sends it straight to the client with no review step at all. When I shipped the tool, both modes were available to every user from day one, regardless of whether a given account executive had ever actually used suggest mode, let alone built up a track record of catching the tool's mistakes.

I ran twenty synthetic client scenarios through a set of seeded user accounts, including one account with a completely clean slate: zero prior approvals, zero history of any kind. That new-user account had the exact same access to auto-send as an executive who had been running the tool for months. Nothing in the system distinguished them. The zero-history account flipped on auto-send on its very first scenario, because nothing told it not to, and a proposal with a pricing error went straight to a client with no human anywhere in the loop.

What bothered me about this was that the mistake was entirely predictable from the access model. The access model handed a brand-new account the exact same auto-send capability as a veteran user, and the pricing error that reached the client was the direct, foreseeable result of that design choice. Auto-send had been exposed as a feature flag, available to whoever wanted to click it, when the thing that should have gated it was something completely different: whether this specific person had actually built up a reason to trust the tool's suggest-mode output on their own accounts. Feature availability and earned trust measure different things, and the tool was tracking only the first one.

## The pattern

The fix hides auto-send per user until a reveal gate confirms that specific user has approved at least ten suggest-mode drafts. Below that threshold, the auto-send control is removed from the interface entirely. A user under the threshold sees only suggest mode; auto-send simply doesn't appear as an option. The new-user account stays locked to suggest-only mode from its first scenario, and it stays there until it clears the threshold on its own approval history.

Rerun the same twenty scenarios under that gate and the zero-history account can't trigger an auto-send incident, because auto-send isn't reachable yet for that account. The unearned-autonomy incident rate goes to zero because the option that caused the incident is no longer available to the account that would have misused it. Users who had actually cleared ten approvals still had auto-send available exactly as before. The gate leaves the faster path fully open for anyone who has earned it and closes the path only for accounts that haven't cleared the threshold yet.

The idea underneath this is that autonomy access should track something an individual person has actually demonstrated. A feature flag that makes a capability available to everyone the moment it ships tracks only whether the code shipped. It has no way to track whether any given person has earned it. A team can be perfectly justified in believing its tool is ready for higher autonomy in the aggregate, based on its overall track record, while still having individual users on the roster who have never personally verified that the tool works the way the aggregate numbers say it does. Uniform rollout treats those two situations as identical. Progressive reveal treats them as what they are: different accounts with different track records, each granted access on its own evidence.

## Design considerations

The approval count this pattern gates on is a proxy, and a proxy has clear limits on what it can actually tell anyone. Ten approvals is a real number and it's cheap to measure. What it actually measures is how many times a user clicked approve. It has no way to measure how carefully that user read what they were approving before clicking. A user can clear the threshold by rubber-stamping ten drafts without reading any of them closely, and a counter built to track approval count has no way to distinguish that user from one who read every draft with real scrutiny. The gate makes autonomy access individually earned in name. Whether it's earned in substance depends entirely on something the counter was never built to check.

That limitation changes how much weight the approval count alone should carry. The pattern is still worth running; the count just needs a second signal alongside it to mean what people assume it means. A team relying on this gate as its only signal of readiness is trusting a metric that can be satisfied by exactly the behavior the metric was supposed to screen out. Pairing the approval count with some occasional spot-check of approval quality, or with a second signal like how long a user actually spent looking at a draft before approving it, closes at least part of that gap, though it adds real overhead to a mechanism that was appealing partly because it was cheap to run.

The other calibration question is where to set the threshold itself, and ten isn't a number to treat as universal. A threshold that's right for a low-stakes internal tool is very likely wrong for something that sends client-facing communication with real financial exposure attached to a mistake, and the right number depends on how expensive a single bad instance of the higher-autonomy mode actually is. Set the threshold too low and the gate opens before trust is real. Set it too high and users who have genuinely earned faster access spend longer than they should in the slower mode, which has its own cost even if it's quieter than the failure this pattern exists to prevent.
