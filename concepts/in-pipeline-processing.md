---
title: "In-pipeline processing"
type: "Concept"
description: "Running media work such as mixing, recording, or computer vision inside a pipeline while the stream is in flight."
created: '2026-10-17'
updated: '2026-10-17'
tags: [media, webrtc, architecture]
sources:
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/migrating-off-a-legacy-media-server.md"
---

# In-pipeline processing

Processing media inside the pipeline while it is in flight, rather than simply relaying it. It matters because it is the deciding factor between a heavyweight pipeline framework and a lean [selective forwarding unit](/concepts/selective-forwarding-unit.md): pipelines earn their weight only when media actually needs mixing, recording, or computer vision mid-stream.

## Key Claims

- [Kurento](/entities/kurento.md) is a [GStreamer](/entities/gstreamer.md)-based pipeline framework with a WebRTC-facing API; [OpenVidu](/entities/openvidu.md) is the higher-level room framework teams build against.
- A lean SFU is better for RTSP-in, WebRTC-out fan-out with no media processing.
- Re-verify why a heavyweight pipeline framework was chosen before proposing a swap.
- Migrating off a legacy media server means rebuilding session, room, and client signaling logic against the new platform.
- Still-needed in-pipeline processing can move to a separate service beside the SFU.
- Cutover should be sequenced as a parallel run with a rollback path, like a database migration.

## Related

- [selective forwarding unit](/concepts/selective-forwarding-unit.md) — the alternative when no in-flight processing is needed
- [media relay](/concepts/media-relay.md) — the simpler pass-through case
- [Kurento](/entities/kurento.md) — pipeline framework
- [GStreamer](/entities/gstreamer.md) — underlying media graph
- [Kurento and the Pipeline Approach](/sources/kurento-and-the-pipeline-approach.md) — primary source
- [Migrating Off a Legacy Media Server](/sources/migrating-off-a-legacy-media-server.md) — primary source
