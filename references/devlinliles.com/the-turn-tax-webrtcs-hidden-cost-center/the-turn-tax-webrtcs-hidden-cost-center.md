---
type: Reference
title: "The TURN Tax: WebRTC&#x27;s Hidden Cost Center"
resource: "https://www.devlinliles.com/the-turn-tax-webrtcs-hidden-cost-center/"
author: "Devlin Liles"
published: '2026-08-27'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every cost model I've seen for a WebRTC media platform starts in the same place: SFU capacity, egress bandwidth per viewer, maybe some CPU headroom for encoding. Almost none of them start with the line item that actually blows the budget in production. That line item is TURN relay bandwidth, and if you haven't budgeted for it explicitly, you haven't budgeted for your real cost.

I want to spend this post on why that happens, because it's not an edge case. It's a structural fact about how networks work, and it shows up in every deployment at some meaningful rate.

## Why WebRTC needs any of this in the first place

Most devices on the internet don't have a direct, publicly routable address. They sit behind NAT (Network Address Translation), which lets many devices on a private network share one public IP. That's great for conserving IP addresses and adding a layer of protection, and it's also the reason two WebRTC endpoints can't just connect to each other directly the way you might assume. Neither one necessarily knows its own public-facing address, and even if it did, the NAT and firewall in the path might not let an unsolicited connection through.

ICE (Interactive Connectivity Establishment) is the process WebRTC uses to solve this. It tries a sequence of approaches to find a path that actually works between two endpoints: try a direct connection first, then use STUN to help each side discover its public IP and port so a direct path might still be possible, and if that fails, fall back to relaying media through a TURN server.

STUN (Session Traversal Utilities for NAT) is lightweight by design. It's a quick query-response service: a device asks a STUN server what its public IP and port look like from the outside, and uses that information to attempt a direct connection to the other peer. STUN itself doesn't carry any media. It just helps the two sides find each other.

TURN (Traversal Using Relays around NAT) is what happens when STUN-assisted direct connection isn't possible at all, which happens more often than most people expect, particularly against symmetric NAT configurations or restrictive corporate firewalls. When that happens, WebRTC falls back to relaying every packet of media through a TURN server sitting between the two peers. Neither peer talks to the other directly anymore. Every byte of that session's audio and video flows through the relay.

Walk through what that ICE negotiation actually looks like in practice. Each side gathers candidate addresses: a host candidate (its own local address), a server-reflexive candidate (its public-facing address as seen through STUN), and, if it's configured, a relay candidate through TURN. Both sides exchange candidates and try pairs of them in priority order, host-to-host first because that's cheapest and fastest, then anything STUN made possible, and only falling back to the TURN relay candidate if nothing better connects. This ordering is deliberate. ICE always prefers the cheapest working path and only pays for TURN when it has no other option. The problem isn't that ICE makes a bad choice. It's that "no other option" happens on a meaningful fraction of real-world connections, often because of network configurations neither side controls.

For completeness on the security side: none of this negotiation or relay changes the fact that WebRTC encrypts everything it sends. DTLS (Datagram Transport Layer Security) handles the handshake that sets up encryption keys before any media flows, and SRTP (Secure Real-time Transport Protocol) is the encrypted media format that actually rides on the wire afterward. Even a TURN-relayed session stays encrypted end to end in this sense: the relay server just forwards the encrypted packets it receives. I mention DTLS and SRTP here for completeness. The cost surprise lives elsewhere, in TURN.

## Where the bandwidth actually goes

Here's the detail that catches teams off guard. When a connection relays through TURN, that traffic isn't costing you bandwidth once. It's costing you twice: once for the media arriving at the TURN server from the sender, and again for the TURN server forwarding it on to the receiver. A single relayed viewer connection consumes twice the bandwidth of a direct or STUN-assisted one, because the relay server is both a receiver and a sender for every packet.

Now scale that across a real viewer base. Any viewer behind a symmetric NAT, a restrictive corporate firewall, or certain carrier-grade NAT configurations on mobile networks is going to end up relaying through TURN, simply because that's what their network environment allows. In a video security platform with viewers logging in from office networks, VPNs, and cellular connections, a meaningful chunk of your total viewer sessions will land on TURN by default. That's not a failure mode. It's the expected outcome of how ICE is designed to behave, and it's happening on every deployment I've seen at real scale.

There's a latency cost bundled in here too, and it matters for a series organized around glass-to-glass latency specifically. A TURN relay is a physical detour. Media routes through wherever the relay server sits, then back out to the destination, adding distance on top of the direct path between sender and viewer. Depending on where that relay is placed relative to the two endpoints, that detour can add meaningful delay on top of whatever the direct path would have cost. So TURN is a bandwidth line item and a latency line item both, which is exactly why relay infrastructure deserves deliberate, planned placement on the network layer.

## Why this breaks cost models that don't see it coming

If your cost model only accounts for SFU egress, the bandwidth a viewer consumes pulling their stream straight from the media server, you've modeled the cheap path and ignored the expensive one. The teams that get surprised are the ones who size their infrastructure spend around SFU forwarding costs, ship it, and then watch their actual bandwidth bill come in well above projection once a real, geographically and organizationally diverse viewer base hits the system and a chunk of them land on TURN.

The fix isn't complicated, it just has to happen before you commit to a number. Budget TURN bandwidth as its own explicit line item with its own weight in the model. Estimate what fraction of your viewer base is likely to need relay based on where they're actually connecting from (corporate networks and certain mobile carriers push that fraction up), and price that fraction at double the bandwidth of a direct connection. That estimate won't be exact on day one, and it doesn't need to be. What it needs to do is exist as a line item you're watching, so that when real traffic tells you the actual relay rate, you're adjusting a number you already planned for.

If you're running your own relay layer, coturn is the software most teams reach for. It's the most widely used open-source TURN and STUN server implementation, and there's a good chance it's the literal software sitting at this layer in any WebRTC deployment you've touched, including managed platforms that don't advertise it by name. Whether you run coturn yourself or lean on a managed TURN provider, the budgeting discipline is the same: treat relay bandwidth as a first-class cost driver, size it against your actual viewer network mix, and revisit that estimate once real traffic gives you a number to measure against.

## The takeaway

The SFU is not usually where a WebRTC deployment's bandwidth budget breaks. TURN is. It's invisible until you go looking for it, it doesn't show up in a topology diagram the way the media server does, and it scales with exactly the users you have the least control over: the ones behind restrictive networks you didn't choose and can't change. Model it explicitly, price it at double, and you won't be the team explaining a bandwidth bill nobody predicted.

Every layer in this series so far has had the same shape: a decision that looks small in isolation but compounds hard once real traffic and real networks get involved. Topology decides how cost scales with viewers. The control plane and data plane split decides how the system scales at all. TURN decides whether your bandwidth model survives contact with the networks your actual users sit behind. None of these are exotic problems. They're ordinary consequences of how the internet is actually built, and the teams that plan for them upfront spend a lot less time explaining surprises later.
