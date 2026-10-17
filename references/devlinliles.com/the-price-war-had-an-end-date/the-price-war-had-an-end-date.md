---
type: Reference
title: "The Price War Had an End Date"
resource: "https://www.devlinliles.com/the-price-war-had-an-end-date/"
author: "Devlin Liles"
published: '2026-10-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I used to write "open-weight tokens get cheaper every quarter" into cost models the way people write "assume 3% inflation." On August 6, 2026, DeepSeek proved that line was always a bet dressed up as a law. The company told its own developers that API prices were about to rise "significantly." No percentage attached. No date attached. Just the warning.

Eighteen months of watching DeepSeek drag the entire market down in price is what made that line feel safe to write. The R1 release in January 2025 kicked off the pattern, and every quarter since ran the same script: DeepSeek cut prices, the rest of the market matched or got undercut, and my spreadsheet got a little more comfortable treating the floor as permanent.

Model quality kept climbing across R1, V3, and V4. Each release did more per token than the last, and the price per token kept falling anyway. Eighteen consecutive quarters of that pattern is a long enough streak to stop looking like a promotion and start looking like physics.

OpenCode's usage numbers on DeepSeek V4 Flash, published August 1, point at a different explanation. Adoption had reached a scale that only makes sense if a real share of the open-weight coding-assistant market had started routing through DeepSeek's API by default. Cheap tokens are how a company buys that kind of share. The strategy works until the volume it wins costs more to keep serving than the price charged for it, and then the subsidy has to end somewhere.

A price war ends one of two ways. The competitor with the worse cost structure runs out of runway and drops out, or the competitor that won the volume runs out of margin to keep subsidizing it. Eighteen months of falling prices read like the first story: a lab whose infrastructure and training costs were genuinely lower than everyone else's, passing the savings through. The August 6 warning reads like the second story. Usage grew past what the price could carry, and the correction had no scheduled date because nothing scheduled it. Growth triggered it.

A low price backed by a genuinely lower cost structure is a durable advantage. A low price backed by a willingness to absorb losses for market share is a subsidy, and subsidies get revoked the moment the subsidizing party can't carry them. From outside the company, the two look identical: same API, same benchmark scores, same invoice. The only way to tell them apart is to ask why the price sits where it does, and a spreadsheet with one column for current price has no room for that question.

Any architecture decision that priced in a specific vendor's rate as a long-term constant was making an unstated bet on which of those two stories was true. The R1-era collapse in prices felt like a fact about where compute economics were permanently heading. It functioned more like a promotional rate tied to a growth target, and promotional rates end once the target is hit.

DeepSeek's eighteen months of cheap tokens turned out to be a subsidy with an unpublished size limit. August 6 is the day the market found out where that limit sat.
