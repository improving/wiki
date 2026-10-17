---
type: Reference
title: "Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline"
resource: "https://www.devlinliles.com/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline/"
author: "Devlin Liles"
published: '2026-08-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

If your RTSP-to-WebRTC pipeline is burning CPU, the fix usually isn't a faster transcoder. It's no transcoder at all.

That sounds too simple to be the headline of a post, but I've watched enough teams throw hardware at this problem to know it's the one nobody checks first. They see CPU pegged on the media server, they assume the encode settings need tuning, they look at GPU acceleration, they price out bigger instances. All of that can help. None of it beats removing the operation entirely.

## Why passthrough is even possible

Start with a fact that's easy to miss because it's buried in protocol details: RTSP and WebRTC don't actually disagree about how media is packaged. Both carry their audio and video payloads over RTP, the Real-time Transport Protocol. RTSP uses RTP to move packets from camera to client. WebRTC uses RTP too, wrapped in SRTP for encryption, negotiated over DTLS. The wire format for the actual media data is the same underlying protocol in both cases.

That's why passthrough works. A gateway sitting between an RTSP camera and a WebRTC viewer doesn't need to decode a video frame, understand its content, and re-encode it into something new. It can take the RTP packets coming off the camera and repackage them into SRTP for the WebRTC side, still carrying the exact same encoded bytes. No decode. No encode. No frame ever gets touched as pixels. It's a packaging change, not a media operation.

This is the single biggest lever available in this class of pipeline, and it's available more often than people assume.

## The condition that has to hold

Passthrough isn't free of requirements. It depends entirely on codec profile compatibility between what the camera sends and what the browser's WebRTC stack can decode.

Codec profile is a constrained subset of a codec's full feature set. H.264 defines baseline, main, and high profiles, each enabling progressively more sophisticated encoding tools. Baseline and main profiles are the safe targets for broad WebRTC decoder compatibility. Every browser's WebRTC implementation can decode them without complaint. High-profile H.264 streams sometimes need transcoding to play in-browser, because not every decoder implementation handles every high-profile feature the same way.

Check what profile your cameras are actually shipping before you assume you need a transcode step. Most IP cameras default to something WebRTC-compatible, or can be configured to. That single settings check is worth more than any downstream optimization you could apply after the fact.

Codec choice matters here too, and it splits cleanly. H.264 has near-universal browser and WebRTC decode support. It's the safe default and the one to target if you have any control over camera configuration. H.265, or HEVC, is more efficient per bit, meaning better quality at the same bandwidth. But its browser support is spottier. That gap is exactly why transcoding becomes "necessary" in a lot of these pipelines: someone picked H.265 for its bandwidth efficiency and then discovered half their target browsers can't decode it directly. The source content never demanded re-encoding. The transcode step exists to paper over a codec compatibility decision made earlier in the pipeline, a patch on a choice, not a response to any inherent property of the video itself.

If you're specifying camera hardware or firmware settings for a new deployment, this is worth deciding early. H.264 baseline or main profile buys you passthrough almost everywhere. H.265 buys you bandwidth savings on the wire and a transcoding bill on the server, unless you're certain of your client population's decode support.

## Why this is the CPU number that matters

Transcoding means decoding a compressed stream back into raw frames and re-encoding those frames, often into a different codec, resolution, or bitrate. It is the single most CPU-expensive operation you'll find anywhere in an RTSP-to-WebRTC pipeline. Decode and encode are both computationally heavy on their own. Doing both, per stream, continuously, for every camera feed you're ingesting, is where server costs spiral.

The relative cost is illustrative rather than a benchmark from a specific deployment, but the shape of the problem holds up consistently: passthrough carries close to zero CPU cost relative to any form of transcoding, and the cost climbs further still once you're changing codec and resolution on top of the baseline cost of re-encoding at all.

This is why "eliminate transcoding" beats "speed up transcoding" as a design principle. A faster encoder, a GPU-accelerated codec path, a beefier server tier, all of these reduce the cost of an operation you didn't need to perform in the first place. Every one of them still leaves you paying a CPU tax per stream that scales with your camera count. Passthrough doesn't scale that way. It scales the way pure packet forwarding scales, which is to say, cheaply.

Transcoding only becomes genuinely necessary when the codec or profile coming off the camera isn't compatible with browser decoders. That's a real constraint, and when you hit it, you transcode and move on. But it should be the fallback path, triggered by an actual incompatibility you've confirmed, not the default architecture you build because nobody checked whether passthrough would work.

## How to actually check this before you build anything

None of this requires guesswork. Every RTSP camera advertises its stream parameters, and you can inspect them directly. Pull the SDP that the camera returns during RTSP setup, or use a tool like ffprobe against the RTSP URL, and you'll see the codec and profile spelled out. If it says H.264 baseline or main, you're clear for passthrough on the video side, assuming your gateway is built to do RTP repackaging directly, without falling back to blind transcoding. If it says high profile, or H.265, that's your signal to either reconfigure the camera, where the option exists, or plan for a transcode path deliberately, before CPU usage spikes in production turns it into an emergency.

This check takes minutes per camera model. Do it during procurement or initial deployment planning, not after the system is live and someone's asking why the media server needs a bigger instance type. A lot of camera firmware also lets you select the H.264 profile directly in the admin interface, which means the fix, when there is one, is often nothing more than a checkbox.

## What this means for how you size infrastructure

This isn't just an efficiency detail, it changes the shape of your capacity planning. A pipeline built around passthrough scales its CPU cost with connection and packet-forwarding overhead, which stays roughly flat per stream and grows gently with stream count. A pipeline built around transcoding scales CPU cost with the product of stream count and encode complexity, and that number grows a lot faster as you add cameras, especially if any of those streams need resolution changes for different viewer bandwidth tiers.

Concretely: if you're scoping server capacity for a deployment that might grow from 50 cameras to 500, the difference between "passthrough architecture" and "transcode-by-default architecture" isn't a rounding error in your infrastructure budget. It's the difference between horizontal scaling that tracks connection count and horizontal scaling that tracks a much steeper CPU curve. Get the codec profile question answered early, and you lock in the cheap curve from day one.

## A brief honest note on AV1

AV1 is worth a mention because it comes up in these conversations, usually pitched as the modern answer to the H.264/H.265 tradeoff. It's the successor to VP9, and it's genuinely more efficient than either H.264 or H.265 at a given quality level, meaning lower bandwidth for the same visual result.

It is not a free upgrade for this specific ingest problem today. AV1 encode is more CPU-expensive than H.264 encode, which matters if you're encoding anything server-side. And decode support on older devices and lower-end hardware is less universal than H.264's, which reintroduces the same compatibility gap that makes H.265 tricky, just with a newer face. If your cameras aren't already shipping AV1 natively, and most IP cameras in the field today aren't, adopting it means either transcoding into it (expensive) or waiting for camera hardware to catch up. Keep it on the radar. Don't restructure your ingest pipeline around it yet.

## The practical takeaway

Before you optimize a transcoding pipeline, check whether you need one. Confirm the codec profile your cameras are actually sending. If it's baseline or main H.264, you likely have a passthrough path available, and taking it removes the most expensive operation in the entire system entirely, which beats making that operation faster. That's a bigger win than anything you'll get from tuning the transcoder itself, and it's usually sitting in a camera configuration screen, not a server optimization backlog.
