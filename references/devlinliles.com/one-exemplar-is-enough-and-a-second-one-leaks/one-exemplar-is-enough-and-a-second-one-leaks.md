---
type: Reference
title: "One Exemplar Is Enough, and a Second One Leaks"
resource: "https://www.devlinliles.com/one-exemplar-is-enough-and-a-second-one-leaks/"
author: "Devlin Liles"
published: '2026-10-09'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a receipt-digitization tool that pulls line items, name, quantity, unit price, total, out of OCR'd restaurant receipt text and into structured JSON. The prompt I started with included five few-shot examples of the target schema, all using plausible, real-sounding restaurant items. Caesar Salad. House Burger. The idea was that more examples would help the model lock onto the pattern more reliably, which felt like a reasonable instinct going in.

I tested it against twenty seeded receipts, several of which happened to contain item names that closely resembled the exemplars' item names, not because I engineered a trap but because restaurant menus genuinely overlap that much. A burger place has a house burger. A lot of places have a Caesar salad. And on those receipts, something started happening that had nothing to do with the actual OCR text in front of the model. The output occasionally echoed an exemplar's specific value, an item name, sometimes a price, that wasn't present anywhere in the actual receipt being processed. The model was pattern-matching to the exemplar it had seen five times in a row and pulling a value from there instead of reading the actual receipt, especially on the noisier OCR input where the actual receipt text was harder to parse cleanly.

The five repeated examples weren't adding five times the guidance. Every one of them conveyed the identical structure, the identical field names, the identical shape, and once the model has seen that shape once, seeing it four more times doesn't teach it anything new about the shape. What it does teach, unintentionally, is that "Caesar Salad" and "House Burger" are the kind of value that belongs in this field, strongly enough that under noisy input, the model sometimes reaches for a familiar-sounding answer instead of the actual, messier one sitting in the receipt.

## The pattern

I stripped the prompt down to exactly one exemplar. Not zero, because the model still benefits from seeing the target structure once, but one, and I deliberately swapped the example's item name for a generic placeholder, "Item Name," a value with no restaurant-menu plausibility at all, nothing a real receipt could ever accidentally resemble.

Extraction accuracy held on the same twenty receipts. Sit with what that means: four of the five original examples were contributing nothing measurable to the model's ability to produce the correct structure. One example was already sufficient to convey a repeated structure. The other four were pure token cost with an actual downside attached, since token cost went down by roughly the cost of the four removed examples, and the leakage that had shown up on receipts with menu-adjacent item names dropped to zero. There was nothing left for the model to latch onto, because the exemplar's own value was a placeholder specifically chosen to have no real-world echo.

The mechanism underneath this is a distinction I hadn't fully separated in my head before running the test: showing structure and showing content are two different jobs, and repeating an example does almost nothing for the first while actively hurting the second. One example demonstrates the shape completely. A structure doesn't get clearer by seeing it five times instead of once. What does change with repetition is how strongly a specific value inside that example gets reinforced as a plausible answer, and that reinforcement is exactly what you don't want when the model's job is to read an actual, specific input rather than recall a memorized pattern.

## Design considerations

The obvious question is whether one example is really always enough, and I don't think the honest answer is a flat yes. One exemplar conveys structure reliably when the structure itself is simple and consistent, a flat object with a handful of fields, the kind of thing this receipt schema actually was. If the target structure has meaningful internal variation, optional fields that only sometimes apply, nested objects whose shape changes based on some condition in the input, one example might not show enough of that variation for the model to generalize correctly, and a second exemplar chosen specifically to demonstrate the variation the first one didn't cover earns its token cost back. The failure mode I tested against was repetition of the same structure, not genuine structural diversity, and those are different problems with different right answers.

The placeholder choice matters more than it looks like it should. I picked "Item Name" specifically because it reads as obviously generic, a value no real receipt would produce and no model would mistake for a plausible answer. A placeholder that's still somewhat plausible, something like "Chicken Sandwich" instead of an actual, common restaurant item, reintroduces a smaller version of the same leakage risk, because plausible-sounding placeholder values can still get echoed even when they're meant as filler. The safest placeholders are the ones that are obviously structural rather than obviously content, "Item Name" rather than any actual food, a numeric field showing "0.00" rather than a price that could plausibly appear on a real receipt.

I'd also flag that this pattern's benefit scales with how much the exemplar's domain overlaps with the actual input domain. The receipt case is a strong example precisely because restaurant menus genuinely repeat common items across different establishments, so a real-sounding exemplar value has a real chance of resembling something in the actual data. A domain with less overlap, extracting structured data from wildly varied technical documents where no two inputs share vocabulary, carries less leakage risk from a second real-sounding example in the first place, simply because there's less chance the exemplar's specific value resembles anything in the actual input. The token-cost savings from dropping extra examples apply everywhere. The leakage risk this pattern specifically closes is sharper in domains where inputs cluster around common, repeatable values, which is exactly the condition that made the receipt case a good one to test in the first place.
