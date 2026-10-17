---
type: Reference
title: "Keyframes and Latency: The Cheapest Win Most Teams Never Touch"
resource: "https://www.devlinliles.com/keyframes-and-latency-the-cheapest-win-most-teams-never-touch/"
author: "Devlin Liles"
published: '2026-08-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Glass-to-glass latency is the number that actually matters. It's the total delay from a photon hitting the camera sensor to a pixel appearing on the viewer's screen, and it's the only measurement that captures what a user actually experiences. Not the network round-trip time, not any single-hop benchmark, the full path.

Most teams debugging latency in a live video system start by measuring network transit. That's understandable. Network latency is easy to visualize, easy to instrument, and it's the layer everyone's trained to suspect first. It's also, in most RTSP-to-WebRTC setups, not where the time is actually going.

## Break the path into stages

To find where latency accumulates, it helps to walk the full glass-to-glass path stage by stage, breaking down what's otherwise one opaque number:

- Capture and encode, where the camera sensor produces a frame and the onboard encoder compresses it
- Camera-to-gateway transit over RTSP
- Gateway processing, where the stream gets repackaged for WebRTC delivery
- Gateway-to-viewer transit over ICE and the rest of the WebRTC stack
- Client decode and render, where the browser turns bits back into pixels on screen

Add up realistic numbers for each stage in a typical setup and one stage dwarfs the rest. This is illustrative rather than measured from a specific deployment, but the shape holds across most systems I've looked at.

Network transit, both camera-to-gateway and gateway-to-viewer, tends to be tens of milliseconds. Gateway processing itself, when passthrough is in play, is close to nothing. The two stages that actually eat the latency budget are capture/encode, specifically the wait for a usable keyframe, and client-side jitter buffering. Neither of those is a network problem. Both are configuration problems, and both are fixable without touching your architecture.

## What a keyframe actually is and why new viewers wait for one

A GOP, or Group of Pictures, is the span between two keyframes in an encoded video stream. A keyframe, also called an I-frame, is a complete, independently decodable frame. Every other frame in the GOP only encodes the changes since the previous frame, which is what makes video compression efficient, but it also means those frames are useless on their own. You can't decode frame 40 of a GOP without having already decoded frames 1 through 39.

That has a direct consequence for anyone joining a live stream mid-GOP, which is every new viewer, every time: they cannot render anything until the next keyframe arrives. If your camera's GOP is four seconds long, a new viewer can be staring at a black screen for up to four seconds before the first frame paints. That's not a network delay, a decode delay, or a WebRTC negotiation delay. It's a pure function of how far into the GOP the viewer happened to connect.

## Why cameras ship configured wrong for this

IP cameras are, by default, tuned for recording and storage efficiency, not live viewing. Longer GOPs mean fewer keyframes, and keyframes are the most expensive frames to store because they carry full image data, where most frames carry only deltas. A 2 to 4 second GOP is common on out-of-the-box camera firmware, and for a system built around continuous recording and later playback, that's a completely reasonable tradeoff. Storage cost drops, video quality holds steady, nobody's waiting for anything because nobody's watching live.

The moment you put that same camera feed in front of a live viewer, the tradeoff flips. The exact setting that made recording efficient is now the single biggest contributor to glass-to-glass latency in the entire pipeline. This is why teams building live-view features on top of an existing NVR or recording-focused camera fleet run into latency complaints that have nothing to do with their WebRTC implementation. The bottleneck was configured into the camera before the WebRTC pipeline was ever built.

## The fix, and why it's the cheapest one available

Forcing a shorter keyframe interval, something in the 0.5 to 1 second range, is usually the fastest latency win you can get, and it's cheaper than any server-side optimization you could apply afterward. You have two places to make this change. Ideally, you configure it directly on the camera, using ONVIF, the industry-standard protocol for configuring and controlling IP cameras independent of manufacturer. Most IP cameras support ONVIF for exactly this kind of setting, and pushing the GOP shorter at the source is the cleanest fix because it changes the actual encoded stream at its origin, the most direct fix available.

Where you don't control the camera directly, or where different camera vendors expose this setting inconsistently through ONVIF, you can sometimes force keyframe behavior at the gateway layer instead. It's a less clean fix than doing it at the source, but it's still far cheaper than any transcoding-based workaround, and it doesn't require touching every camera's firmware individually.

Either way, this is a configuration change, not an engineering project. Compare that to the alternative most teams reach for instead, which is trying to shave milliseconds off network transit or gateway processing, stages that were never the problem to begin with. You'll spend more engineering time optimizing a 30-millisecond hop than it takes to cut seconds off the GOP wait.

## The bandwidth tradeoff, and why it's worth taking

Shortening the GOP isn't a free change, and it's worth being direct about the cost. Keyframes carry full image data, so more of them per second means more bits on the wire and more storage consumed if you're recording the same stream. Moving from a 4-second GOP to a 1-second GOP roughly quadruples your keyframe frequency, which does increase bitrate, though the increase is typically a modest percentage of total stream bandwidth, well short of a multiple, since keyframes are still a minority of total frames even at a 1-second interval.

Weigh that against what you're buying: a live-view experience that goes from multi-second black-screen waits to near-instant rendering for every new viewer. For most live video security or monitoring use cases, that tradeoff is an easy call. A modest bandwidth increase on the camera-to-gateway link buys a materially better viewing experience for every operator who opens a feed. If you're bandwidth-constrained on the camera's uplink specifically, cellular-backed cameras in remote locations being the common case, you may need to test where the GOP setting stops being worth it for that particular link. But for anything on a normal wired or reliable wireless backhaul, this isn't a close decision.

## How to verify the fix actually worked

Don't just change the setting and assume it helped. Measure it. The simplest test is to open a fresh viewer connection against a live camera feed and time from connection request to first rendered frame, repeated a handful of times to account for the fact that where you land in the GOP is somewhat random relative to when you connect. Before the change, with a multi-second GOP, you should see meaningfully varying wait times, sometimes near-instant if you get lucky and connect right before a keyframe, sometimes multiple seconds if you connect right after one. After shortening the GOP to sub-second, that variance should collapse dramatically, because the maximum possible wait time is bounded by the new, much shorter interval.

If you're not seeing that improvement after making the change, confirm the setting actually landed on the camera itself, since a change visible only in your gateway configuration hasn't taken effect on the device, and some camera firmware silently ignores unsupported ONVIF parameters without raising an error. Confirming the change actually reached the camera is worth the five minutes it takes, because a setting that looks correct in your configuration management and never landed on the device will leave you debugging a latency problem that's already technically fixed on paper.

## Jitter buffer is the other lever, and it's a tuning problem, not a removal problem

The client-side jitter buffer is the other stage that shows up in that latency chart, and it deserves a more careful treatment than "turn it down." A jitter buffer is a small delay buffer on the receiving side that smooths out network timing variance, so video plays back steadily even when a packet arrives a little early or late. Tune it too tight and you get choppy playback whenever the network hiccups. Tune it too loose and you're adding latency that has nothing to do with the actual network conditions you're facing.

Unlike GOP length, you don't want to minimize jitter buffer delay to zero. You want it matched to your actual network conditions, tight enough to avoid unnecessary delay, loose enough to absorb the jitter your network actually produces. That's an ongoing tuning exercise, informed by real measurement of your delivery network, revisited as conditions change. It's never a single setting you flip once and forget.

One more piece worth a brief mention: SDP, the Session Description Protocol, is the text format both sides of a connection exchange during signaling to describe what codecs, formats, and capabilities they support. It's part of how a keyframe request or codec profile actually gets negotiated between camera-facing gateway and browser client. You don't need to hand-tune SDP exchanges to get the keyframe interval win. Just know it's the layer where these capabilities get agreed upon before any media flows.

## Where to start

If you're chasing latency complaints in a live-view feature, don't start with the network. Start with GOP length. Check what your cameras are actually configured to send, push it down to something in the sub-second range via ONVIF if you control the camera, and only then start looking at jitter buffer tuning for whatever variance is left. It's the cheapest fix in the entire glass-to-glass path, and it's the one most teams never touch because they assumed the problem lived somewhere more complicated.
