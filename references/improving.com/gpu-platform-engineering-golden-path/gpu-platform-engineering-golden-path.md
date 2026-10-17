---
type: Reference
title: "Why Kubernetes GPU Scheduling Keeps Breaking Your Golden Path"
resource: "https://www.improving.com/thoughts/gpu-platform-engineering-golden-path/"
author: "Atulpriya Sharma"
published: '2026-10-06'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

A platform team gets a request to enable GPU support. They provision a node pool, wire up a self-service request flow, and add it to the internal developer portal (IDP). The problem looks solved as the developers got what they needed, and platform team successfully closed the ticket.

Then an ML engineer submits a four-node training job. Three pods come up while the fourth sits pending. Nobody gets paged, and nothing crashes. The node just sits there, quietly burning time, capacity, and the training run's deadline, while the platform team tries to figure out whether this is a quota issue, a scheduling issue, or something they didn't know they needed to design for.

Good abstractions remove complexity, but only after the underlying problem is stable. GPU platform engineering isn't there yet. Scheduling, tenant isolation, and driver coordination are all still moving. If you abstract over something that's still moving, then you're hiding a decision your team hasn't actually made.

## Platform Engineering for GPUs

Platform engineering for GPUs is the discipline of building self-service infrastructure, most of it running on Kubernetes today, that lets application teams request and run GPU-backed workloads (training jobs, inference services, batch ML pipelines) without needing to understand the underlying scheduling, driver, and hardware layers themselves. It's the same golden-path model platform teams already use for CPU and memory, applied to a resource that behaves nothing like CPU and memory.

The difference between CPU and GPU platform engineering is:

- CPU scheduling, isolation, and quota management were solved by the time [platform engineering](https://www.improving.com/thoughts/category/platform-engineering/) became a discipline.
- GPU scheduling and isolation are still being actively rebuilt inside Kubernetes itself, which means the golden path is still robust.

## Kubernetes GPU Scheduling is Changing

### **What the old model couldn't see**

Since 2017, Kubernetes has scheduled GPUs through the device plugin model, and that model has one job: tell the scheduler nvidia.com/gpu: 1. This was just a number and nothing more.

VRAM capacity, NVLink topology, and MIG profiles don't exist as far as the scheduler is concerned. Platform teams compensated for this with node labels for GPU type, tolerations to keep the wrong workloads off the wrong nodes, and affinity rules to nudge scheduling toward hardware that actually fits. It worked mostly. That compensation is now baked into golden paths as tribal knowledge disguised as YAML.

### **What's changing right now**

Dynamic Resource Allocation (DRA) or Kubernetes DRA [graduated to general availability in Kubernetes 1.34](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/), and it changes what the scheduler is allowed to know. Instead of a bare count, DRA lets the scheduler reason for real device attributes like GPU, topology, MIG profile, etc.

This is not an additive upgrade. The device plugin and Kubernetes DRA are [mutually exclusive on the same node](https://docs.cast.ai/docs/dra) because they expose GPU resources through conflicting allocation paths. Kubernetes 1.34 does add a compatibility shim, the DRAExtendedResource feature gate, that lets the scheduler translate old-style extended resource requests into DRA claims automatically. That softens the migration but every golden path built on the device plugin model still faces an architectural decision..

Scheduling isn't finished moving, either. Native gang scheduling, the ability to schedule a multi-pod training job as an all-or-nothing unit instead of pod by pod, is [alpha in Kubernetes 1.35](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/4671-gang-scheduling/README.md) and disabled by default, with beta targeted for 1.37. Until then, production gang scheduling means reaching for [Volcano](https://volcano.sh/en) or NVIDIA's [KAI Scheduler](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/), a second scheduler your platform team now owns, patches, and upgrades, sitting alongside the one that ships with the cluster.

⚠️ **Common mistake:** Gang scheduling is not a nice-to-have to add later. Without it, the pending-pod failure mode from the introduction is the expected outcome. You have to fill the gap of as Kubernetes' default scheduler has no concept of "these four pods are one unit."

Nobody could have waited for DRA to stabilize before shipping GPU support to their ML teams. If your GPU platform predates 2026, you built it on a model mid-migration and didn't know it.

## Every GPU Platform Has Already Made a Tenant Isolation Decision

Even if your team never sat down and discussed tenant isolation for GPUs, your platform has already made a decision. It's just not written anywhere.

### Compare the three Kubernetes GPU sharing strategies and their costs

Three strategies dominate GPU sharing in Kubernetes, and each one trades isolation for flexibility differently:

All three are legitimate in the right context. The problem is that the golden path doesn't surface which strategy is used by the platform team.

### MIG Reconfiguration cost in practice

NVIDIA's GPU Operator [takes roughly 30 to 60 seconds per GPU](https://run-ai-docs.nvidia.com/self-hosted/platform-management/aiinitiatives/resources/mig-profiles) to drain, reconfigure, and uncordon a node when a MIG profile changes.On a shared inference node with eight GPUs, a single profile change costs 4 to 8 minutes of node-wide drain time, during which every workload scheduled on that node is unavailable.

Most teams don't budget the operational cost when they pick MIG because it "does isolation properly." The isolation is per-GPU, but the reconfiguration cost is per-node.

### What isolation alone doesn't cover

Hardware and workload isolation aren't the only layers in play. GPUs typically sit on a shared interconnect fabric (NVLink, PCIe, or similar), and by default that fabric lets GPUs talk to each other across the whole node.

A scheduler that respects MIG or whole-GPU boundaries can still place two tenants' workloads on GPUs that share the same NVLink domain, which reintroduces a data-exposure risk that looks, from the scheduler's perspective, like a correctly isolated placement.

Fabric-level isolation, restricting which GPUs can communicate with which, is a fourth decision layered on top of the sharing strategy, and it's the one platform teams are least likely to know they need to make.

A developer requesting "a GPU" for a multi-tenant inference service, with no visibility into which sharing strategy sits underneath the request, is making a security assumption without knowing they're making it.

- On CPU workloads, tenant boundaries are close to automatic: cgroups isolate memory, namespaces isolate process visibility, and a developer requesting compute doesn't think about what's sharing the underlying core.
- On GPUs, tenant boundary requires an explicit architectural decision, and most teams haven't made it consciously.They've made it by default, usually time-slicing, because it's the fastest strategy to work on whatever hardware is already in the cluster. The default is fine for a proof of concept or internal experimentation. But it stops being fine the moment a second business unit, or a second client in a multi-tenant SaaS product, starts sharing that node pool. At that point, "we enabled GPU support" quietly became "we made a data isolation decision for regulated or sensitive workloads," and nobody signed off on that framing because nobody stated it that way to begin with.

Chargeback breaks for the same reason. If the platform can't tell you which sharing strategy a workload landed on, it can't tell you why one team's GPU bill is three times another team's for what looks, on paper, like the same workload.

## Driver and Firmware Lifecycle is its Own Isolation Layer

In a shared cluster, a driver upgrade affects every tenant on that node simultaneously, because tenants share the host kernel. If one team needs a newer driver version for a feature and another team's workload was validated against the older version, there's no way to give them different versions on the same node without containerized driver stacks (the NVIDIA GPU Operator for Kubernetes supports this) or per-tenant node isolation. If that decision is skipped, the first driver upgrade can quickly become an incident when a workload that worked yesterday breaks today, leaving the platform team to discover that “upgrade the driver” was never a documented or owned process.

💡 **Counterintuitively:** The fix here is treating the driver version as part of the workload class taxonomy from the start, the same way sharing strategy is, so a driver mismatch shows up as a scheduling constraint instead of a production outage.

## What a Durable GPU Golden Path Actually Looks Like

[Platform teams fail](https://www.improving.com/thoughts/how-to-fail-at-platform-engineering/) whenever they abstract a decision before it's actually stable, GPUs just make the failure mode more expensive and harder to reverse. The fix is to be deliberate about which layers are stable enough to hide.

- **Abstract fully**: Container packaging, CI pipelines, observability, access controls. These problems are solved. Hide them completely, because the complexity here is genuinely accidental, not load-bearing.
- **Keep visible**, because each cost strategy is an active architectural decision.
- **Workload class**: Training, inference, or development. Each carries different scheduling, isolation, and storage requirements. Collapsing them into one "GPU workload" category throws away information the scheduler and the platform both need.
- **Sharing strategy**: An explicit, documented decision per workload class.
- **Driver and firmware lifecycle**: A coordination policy the platform team owns on purpose.

## Build the Request Flow Around Workload Class

The self-service question has to change. Instead of "request a GPU," the intake flow should ask what kind of GPU workload this is: training or inference, multi-tenant or dedicated, latency-sensitive or batch.

Each answer routes to a different sharing strategy and a different set of guardrails, and the developer making the request understands what they're getting.

- A training job answers "training, dedicated, batch" and routes to whole-GPU exclusive automatically.
- A latency-sensitive inference endpoint serving a small model answers "inference, multi-tenant, latency-sensitive" and routes to MIG.

The developer never sees the word "MIG" or “whole-GPU.” They see a request that got the right hardware behavior because the platform asked the right question up front.

We worked with a services organization navigating exactly this shift, and one advantage came up repeatedly that platform teams often underestimate: services organizations see this failure mode across clients before any single product team hits it independently.

A training job stalling on pending pods, a time-sliced GPU getting OOM-killed by a noisy neighbor, and a MIG profile that doesn't match the workload it's serving show up as pattern when you're looking across multiple GPU platforms instead of just your own.

A platform team inside a single organization usually discovers a given failure mode the hard way, once, in production. A team that's rebuilt this same golden path for a dozen different clients has typically already seen it before the client asking for help has.

## Teams With Less GPU Platform Debt Aren't the Ones Abstracting Most

Eighteen months from now, the platform teams with the least AI infrastructure debt won't be the ones who hid the most complexity behind the nicest developer portal. They'll be the ones who knew, specifically, which layer underneath their golden path was still moving, and refused to paper over it.

Abstraction built on an unstable foundation amplifies the instability, because the instability becomes invisible until it fails in production. Right now, GPU platforms are sitting on two unstable foundations at once:

1. A scheduling model mid-migration between the device plugin and DRA
2. A tenant isolation model that requires an explicit choice most teams haven't gotten around to making

You don't need to solve both before you ship anything. You need to know, and be honest with your team about, which decisions you've actually made and which ones you've inherited by default.

This isn't the first time we've written about golden paths hiding decisions teams haven't made consciously. If this resonated, [Everyone Talks About Golden Paths. Nobody Talks About Building Them](https://www.improving.com/thoughts/building-golden-paths/) and [What Nobody Tells You About Golden Paths at Scale](https://www.improving.com/thoughts/what-nobody-tells-you-about-golden-paths-at-scale/) cover the same failure pattern outside the GPU context.

I'm always looking to compare notes on how teams are handling GPU platform decisions. Connect with me on [LinkedIn](https://www.linkedin.com/in/atulpriyasharma) if you're working through this. If your organization needs help figuring out where the debt actually lives in your AI platform, [reach out to our team](https://www.improving.com/contact-us/).
