---
type: Reference
title: "Book Three, Cancel Two - The Saga Compensation Chain"
resource: "https://www.devlinliles.com/book-three-cancel-two-the-saga-compensation-chain/"
author: "Devlin Liles"
published: '2026-10-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a trip-booking agent that books a flight, then a hotel, then a car rental for a synthetic itinerary, each against its own mocked vendor API with its own cost and cancellation rules. I seeded a hundred synthetic itineraries with a fixed rate of car rental failures, inventory unavailable, landing after the flight and hotel had already succeeded and been charged.

With no compensation logic defined, a failure at the car rental step just stopped the process and threw an error. Nobody went back and undid the first two steps, because nothing in the system knew that canceling the flight and canceling the hotel were the correct response to a failure three steps later. The flight and hotel bookings stayed live and charged even though the trip as a whole never happened. Across the batch, the orphaned booking cost, money left committed on bookings tied to itineraries that never completed, ran past eight thousand dollars, and almost none of the failed sagas were unwound at all.

That is the saga problem stated plainly. A multi-step transaction that spans independent systems has no built-in atomicity. Nothing rolls back automatically just because a later step failed, and without something explicitly deciding what undoing the earlier steps means for each one, a partial success gets silently left in place as orphaned cost.

## The pattern

Saga Compensation Chain pairs every forward action with a compensating action, authored at the same time, before either one ever runs. Book a flight, and cancel_flight exists as a defined counterpart from the start. Book a hotel, and cancel_hotel exists the same way. As each forward action executes successfully, its compensating action gets pushed onto a stack. When a later step fails, the stack unwinds in strict reverse order, canceling the hotel, then the flight, and each cancellation gets confirmed against the vendor's own recorded state before the saga is marked fully compensated. A cancellation call that returns a success code but that the vendor's own state still shows as booked does not count as done.

The shift this forces is structural rather than reactive. Compensation gets decided in advance, as part of the same plan as the forward action, one paired inverse per step, instead of getting written after someone notices a failure in production. Running the same hundred itineraries through this version brought orphaned booking cost down to zero and brought the share of fully compensated failed sagas to one hundred percent.

I also required the controller to handle a second-order failure: what happens when the compensating action itself fails, when the cancellation endpoint is down at the exact moment the saga controller tries to call it. That case has to surface as its own distinct state, compensation attempted but unconfirmed, rather than getting folded silently into either fully compensated or left indistinguishable from a saga that never tried to compensate at all. A controller that only tracks two states, compensated or not, has nowhere to put a cancellation it attempted but could not confirm, and that gap is exactly the kind of ambiguity a saga is supposed to remove rather than reproduce one level up.

## Design considerations

The whole mechanism depends on something underneath it that has nothing to do with sagas specifically: idempotency. A compensating action, or a retried forward action, only behaves correctly if the vendor treats a repeated call as safe to repeat rather than as a second, distinct booking. Without a caller-supplied key and a real in-flight, absent, or complete model on the vendor's side, a retried cancel_hotel call can double-cancel, or worse, a retried book_hotel call after a timeout can quietly book a second room instead of confirming the first one went through. I treat this as a tool-call safety problem that a saga sits on top of, separate from the saga pattern itself. Build the saga without that foundation underneath it and the compensation logic is sitting on a floor that can double-book instead of cancel.

Every forward action needs a real compensating counterpart for this to work, and some actions do not have one. A sent email cannot be uncanceled. A saga built around a step like that is picking the least-bad response to something already irreversible rather than actually compensating for it, which is a different problem with a different answer, closer to how I'd treat a true-side-effect action than something a saga can cleanly unwind.

The compensating-action stack, paired inverses registered as execution proceeds and unwound in strict reverse order on failure, is a genuinely old idea borrowed from distributed transaction processing, not something invented for agents. What changes here is that an agent, rather than a human engineer writing the workflow by hand, is the one deciding at runtime which stack entries exist and in what order they unwind, which means the stack itself has to be built correctly by something that can make mistakes in ways a hand-authored saga in a traditional service never had to account for. I'd rather build that verification in from day one than wait for the first orphaned booking to show up as a support ticket.
