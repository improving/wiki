---
type: Reference
title: "Load Testing WebRTC at Scale: The Two Axes Most Test Plans Miss"
resource: "https://www.devlinliles.com/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss/"
author: "Devlin Liles"
published: '2026-09-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most WebRTC load tests answer a question nobody asked. They ramp up a connection count, watch CPU and bandwidth climb together, declare a ceiling, and call it capacity planning. The number they produce is real. It's also almost useless, because it collapses two independent stress patterns into one line on a graph.

Here's the test matrix I actually want to see: 1,000 viewers watching one stream, and 1,000 viewers spread across 200 streams. Same total connection count. Completely different system under test.

## Two axes, two failure modes

The first scenario stresses egress bandwidth. One source stream, transcoded into however many renditions your ABR ladder needs, fanned out to a thousand simultaneous viewers. Every one of those viewers pulls packets off the same handful of encoded renditions sitting in memory on the gateway serving that stream. The bottleneck is how much you can push out the door: NIC throughput, SFU forwarding overhead, TURN relay capacity if a meaningful slice of those viewers can't do a direct path. CPU barely moves. You're not encoding a thousand times, you're forwarding.

The second scenario stresses CPU and transcode density. Two hundred separate sources, each running through its own decode/encode pipeline if you're doing any server-side transcoding at all, each carrying its own keyframe cadence, its own jitter buffer, its own SFU session bookkeeping. Egress per stream is trivial, five viewers each. But now you're running 200 independent transcode pipelines on whatever instance density your placement logic decided was reasonable, and the constraint is compute, not pipe.

A test plan that only varies "total connections" walks straight past this distinction. It'll tell you the system handled 1,000 connections fine, without telling you whether it handled 1,000 connections that look like scenario one or scenario two, and those two scenarios break different components in different ways. I've watched a team pass a load test with a number that looked great on paper, then get paged the first time a real deployment put 200 low-viewership camera streams on a single instance and the CPU-bound transcode pipeline choked long before bandwidth was ever a concern. The test wasn't wrong. It was answering a question that didn't match the failure that actually happened.

Build your test matrix around both axes independently. Vary viewers-per-stream while holding streams-per-instance flat, then vary streams-per-instance while holding viewers-per-stream flat. You'll get two very different curves, and both of them are load-bearing information you need before you go to production.

This maps directly onto the sharding decisions I covered earlier in this series. If your placement logic packs streams onto instances by round-robin or by whatever capacity was free at ingest time, you have no guarantee that a given instance ever sees the 200-low-viewership-streams pattern in staging before it sees it in production. Your load test needs to deliberately construct both worst cases: one instance holding a single stream with a viewer count near your platform's ceiling, and one instance holding as many low-viewership streams as your placement logic could plausibly stack onto it. Testing the average case tells you nothing about the instance that gets unlucky.

## Simulating viewers: how real does the client need to be

Once you've decided what you're testing, you need something to generate the viewer side of the load. There are two broad approaches, and the tradeoff between them is realism versus scale.

A headless-browser swarm, Puppeteer driving real Chrome instances that actually join rooms and pull real media, is the most realistic option available. It exercises actual decode, actual jitter-buffer behavior, actual browser WebRTC stack quirks, the same code path a real viewer's browser runs. A choppy-playback failure mode on the client side won't show up in a server dashboard at all, and a browser swarm is the only approach that will reliably surface it, because it's the only approach running a real decoder against real network jitter. The cost is weight. Each simulated viewer is a full Chrome process with real memory and CPU overhead on whatever machine is generating the load. Simulating a few thousand viewers this way means provisioning a substantial load-generation fleet in its own right, which becomes an infrastructure problem layered on top of the problem you're actually trying to test.

Lighter-weight synthetic clients built on Pion, a Go WebRTC library, or GStreamer's webrtcbin element, can simulate viewer density an order of magnitude higher on the same hardware. They speak the WebRTC protocol correctly, negotiate ICE, receive media, and can report loss and jitter stats, without the overhead of a full browser and a real decoder underneath. That's the right tool when the question is "can the server side hold up under N concurrent connections," a pure protocol and forwarding stress test. It's the wrong tool if the question is "does playback actually look good," because a synthetic client that never renders a frame will never surface a jitter-buffer misconfiguration or a decoder that struggles on lower-end hardware. It reports clean stats while a real browser sitting on the same network conditions might be visibly stuttering.

Neither approach is sufficient on its own. Synthetic clients scale the connection count you need to stress the server. Browser swarms tell you what the viewer actually experiences. You need both questions answered, so you end up needing both tools.

There's a middle layer worth building regardless of which client-simulation approach you pick: network condition injection. Real viewers sit behind cable modems with bufferbloat, cellular connections that drop and reacquire, and corporate networks with asymmetric upload caps. A load test run entirely on a clean data-center network between your load generators and your media server will pass every time and tell you almost nothing about how the system behaves for the viewer on a flaky hotel Wi-Fi network. Whichever client tool you use, pair it with a network-conditioning layer, tc/netem on Linux is the standard option, that injects realistic packet loss, jitter, and bandwidth constraints into the path. That's where jitter-buffer and packet-loss-concealment problems actually surface. A perfect network hides them every time.

## Two tools worth naming

If you're building this practice from scratch, don't build the harness yourself before checking whether an existing tool already does what you need.

- **Loadero** is a commercial platform that simulates thousands of concurrent viewers using real browser behavior, across multiple geographies and network conditions, with WebRTC stats built in. It's the fastest path to testing real client experience, decode, jitter buffer, actual browser quirks, at meaningful scale, without standing up your own browser-swarm infrastructure and instrumentation from nothing.
- **webrtcperf** is open source and considerably lighter weight, purpose-built for WebRTC performance and quality testing with multiple concurrent connections. It's not trying to be a full browser-fidelity platform. It's trying to be fast, scriptable, and cheap enough to run constantly.

## Use both, for different jobs

Don't treat this as a choice between the two. They answer different questions, and a mature load-testing practice needs both answers on a regular cadence.

Run webrtcperf in CI, on every build. It's light enough to run continuously without turning your pipeline into a bottleneck, and its job is catching regressions cheaply before they ship: a jitter-buffer change that quietly degrades quality, a gateway update that adds latency, a config drift in your SFU that nobody meant to introduce. Cheap, continuous, and narrow in scope. That's exactly what CI-integrated testing should be.

Run something closer to Loadero, or a full browser-swarm exercise if you've built one, on a periodic cadence, separate from continuous CI: before major releases, ahead of capacity planning cycles, whenever you're about to make a real claim about how many concurrent viewers your product can hold. This is where you validate the client experience at the concurrency your product actually expects, with real decode and real browser behavior in the loop, not just clean server-side stats.

The mistake I see most often is teams picking one of these and stopping there. A CI-only shop catches regressions but never validates real-scale client experience, and gets surprised at launch when server metrics looked perfect and viewers were still seeing stutter. A team that only runs periodic large-scale exercises catches real-experience problems, but catches them weeks after they were introduced, buried in a pile of other changes, on the day of a release review, days too late to fix cheaply. Run both. They're not competing for the same budget line. They're covering two different failure surfaces, and you need coverage on both before you find out the hard way, during an incident, which one you skipped.

Whichever cadence you land on, log the same core metrics both ways so the numbers are comparable: connection setup time, time to first frame, packet loss and jitter per stream, CPU per stream (host-level averages hide the one saturated instance holding a hot stream), and egress throughput per instance. Run the CI numbers and the periodic numbers through the same dashboard. If the CI-scale test and the real-scale test start drifting apart on the same metric over a few release cycles, that's your early warning that something in the gap between the two, usually scale-dependent contention that only shows up above a certain connection count, is quietly building toward a problem the CI test will never catch on its own.
