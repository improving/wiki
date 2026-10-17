---
type: Reference
title: "The Gateway Layer: Getting RTSP Cameras Onto WebRTC"
resource: "https://www.devlinliles.com/the-gateway-layer-getting-rtsp-cameras-onto-webrtc/"
author: "Devlin Liles"
published: '2026-08-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every one-to-many live video system that starts with IP cameras needs a layer between the camera and whichever SFU handles fan-out to viewers. That layer's job is narrow: take RTSP in, put WebRTC out, and do it without adding latency or CPU cost you didn't need to pay. Call it the gateway layer. It's the piece that does the passthrough work I described earlier in this series, and it deserves its own deliberate architectural decision, separate from whatever media server you're already running.

## Why this needs its own layer

It's tempting to ask your SFU to handle RTSP ingest directly, since it's already handling media on the WebRTC side. Resist that. An SFU is built and optimized for one job: receiving WebRTC streams from publishers and forwarding them efficiently to many subscribers. RTSP ingest, ONVIF camera control, ONVIF discovery, RTSP-specific reconnection and stream-recovery logic, all of that is a different problem domain with its own edge cases. Asking a general-purpose SFU to also own that is asking one tool to be excellent at two unrelated jobs.

A purpose-built gateway sitting in front of the SFU is a thinner, more purpose-fit layer for exactly this translation problem. It does one thing, RTSP-to-WebRTC (and often a few other protocols) translation with passthrough where possible, and it does it well because that's the only thing it's designed to do. Your SFU stays focused on fan-out. Your gateway stays focused on ingest and protocol translation. That separation of concerns pays off the first time you need to debug a camera connectivity issue without touching your fan-out logic, or scale your camera ingest independently of your viewer count.

Two open-source tools are purpose-built for exactly this passthrough problem, and they're worth knowing by name, each suited to a different situation.

## go2rtc

go2rtc is WebRTC-first. It restreams on demand, meaning a camera stream only actually runs through the gateway when a viewer is connected and asking for it. Nothing gets forwarded or transcoded for streams nobody's watching. That on-demand model ties resource usage to actual viewership, not camera count, which matters a lot once you're running hundreds of cameras where only a fraction have someone actively watching at any given moment.

It does RTP passthrough without re-encoding whenever the camera's codec profile allows it, which, as covered in the last two posts, is the single biggest performance lever available in this pipeline. Latency is sub-second in the common case, because there's no transcode step and no unnecessary buffering added at the gateway.

go2rtc's real strength is where it grew up. It's the gateway underneath most of the camera and NVR ecosystem right now, most visibly inside Frigate-style NVR tooling. That's not a small detail. It means go2rtc has already been battle-tested against exactly this camera-ingest problem, at real scale, across a huge range of camera manufacturers and firmware quirks, by a community that cares deeply about exactly the failure modes you'll hit. You're not the first person to point a flaky consumer or commercial IP camera at go2rtc and try to get a clean WebRTC stream out the other side.

## MediaMTX

MediaMTX, formerly rtsp-simple-server, takes a broader approach. It speaks RTSP, RTMP, HLS, WebRTC, and SRT, both in and out. Where go2rtc is built around the WebRTC-first, on-demand model, MediaMTX is built to be a general-purpose streaming server that happens to support all of these protocols well, and it's mature and actively maintained.

That protocol breadth is the actual differentiator, and it matters if your product needs to keep serving clients that aren't WebRTC. RTMP is an older streaming protocol, not WebRTC-compatible without a gateway, but still common as an ingest format into recording and processing systems, and still required by some third-party integrations you may not control. HLS delivers video as small HTTP-fetched segments, which makes it trivially easy to scale through any CDN, but at the cost of latency, often 6 to 30 seconds or more end to end, a common fallback path for viewers who don't need true real-time viewing. SRT is a newer protocol built for reliability over lossy networks, increasingly showing up as a contribution feed format from remote or bandwidth-constrained sources.

If your product's viewer base is entirely WebRTC clients, none of that breadth buys you anything. If it isn't, if you've got older viewers on HLS players, third-party systems expecting RTMP, or contribution feeds coming in over SRT, MediaMTX handles all of that inside one tool, saving you from stitching together separate gateways per protocol.

The latency gap between these delivery protocols is real enough to shape which one you reach for by use case, not just by preference. WebRTC's sub-second latency is why it's the right choice for true live viewing, the kind where a security operator is reacting to what's happening on screen right now. HLS's 6-to-30-plus-second latency is a real tradeoff, not a flaw, and it's the right choice for viewers who need a live-ish feed and easy CDN scaling more than they need sub-second responsiveness. RTMP and SRT sit in between, serving contribution and integration pipelines, separate from end-viewer delivery. Knowing which protocol your actual viewers need is part of getting this layer right, and defaulting to "WebRTC for everything" without checking is how teams get this wrong.

## How the gateway actually connects to your SFU

It's worth being concrete about where this layer sits in the overall pipeline, since "gateway in front of the SFU" can sound more abstract than it is. In practice, the gateway terminates RTSP from the camera on one side, and on the other side it acts as a WebRTC publisher into your SFU, or exposes its own WebRTC endpoint that viewers connect to directly for smaller deployments. Either pattern keeps the SFU doing exactly what it's good at: receiving a published stream and fanning it out to however many viewers are watching, without needing to know anything about ONVIF, RTSP session management, or camera reconnection logic.

This also gives you a clean place to handle the ugliest part of any camera-based system: cameras going offline, rebooting, or dropping connections at unpredictable times. That reconnection and retry logic belongs in the gateway layer, close to the protocol it's managing, kept out of your SFU and your application logic. Both go2rtc and MediaMTX handle RTSP reconnection natively, which is one more reason not to reinvent this piece yourself. Camera reconnect handling looks simple until you've watched a fleet of cameras drop and reconnect during a network blip, and discovered how many edge cases exist around partial reconnects, stale sessions, and stream state that didn't clean up correctly.

## Deployment shape matters too

One more practical point: where you run the gateway relative to your cameras affects both latency and reliability. Running the gateway close to the cameras, on local infrastructure or at a network edge near the camera fleet, keeps the RTSP hop short and shields the rest of your pipeline from camera-side network instability. Running it centrally, alongside your SFU and application infrastructure, simplifies operations at the cost of a longer RTSP hop back to each camera site, which matters more for geographically distributed camera deployments than for a single-site installation.

Neither go2rtc nor MediaMTX forces a particular topology on you. Both are lightweight enough to run at the edge, close to the cameras, or centrally alongside the rest of your infrastructure. That flexibility is part of why treating this as its own layer, kept separate from your SFU's ingest logic, pays off: you can make the topology decision independently for your camera-facing infrastructure and your viewer-facing infrastructure, free from whatever your SFU's deployment model assumes.

## Which one to reach for

Recommend go2rtc if your product is WebRTC-only and you want the simplest possible on-demand model: streams run when someone's watching, passthrough keeps CPU cost near zero, and you're leaning on a tool that's already proven itself inside the NVR ecosystem against the exact camera-compatibility problems you'll hit.

Recommend MediaMTX if you need to keep serving non-WebRTC clients alongside your WebRTC path: HLS for older or CDN-distributed viewers, RTMP for third-party integrations, SRT for contribution feeds. The broader protocol support costs you nothing in the WebRTC path itself, and it saves you from running multiple gateway tools side by side.

Both are real options, purpose-built for this exact translation problem, and both are a better fit than asking a general SFU to do this work directly. The decision between them comes down to one question: does anything downstream of your gateway need a protocol other than WebRTC? If the answer is no, go2rtc's simplicity wins. If the answer is yes, MediaMTX's breadth saves you from building a second gateway later.
