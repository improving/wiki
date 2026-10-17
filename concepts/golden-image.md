---
title: "golden image"
type: "Concept"
description: "A prebuilt, hardened machine image used as the consistent basis for launching servers or containers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, platform, infrastructure]
sources:
  - "/sources/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer.md"
  - "/sources/security-the-thing-that-everyone-loves-to-hate.md"
---

# golden image

A golden image is a prebuilt, standardized machine image — an AWS AMI, for example — that teams launch from instead of configuring servers by hand. It is the artifact form of immutable infrastructure: the base operating system, kernel, and installed software are baked once, versioned, and reused, which makes deployments reproducible and lets security teams harden a single starting point rather than every running host.

## Key Claims

- An AMI is a master image or template for launching EC2 instances, categorized by region, OS, architecture, launch permissions, and storage backing.
- HashiCorp Packer and AWS Image Builder are the common golden-image tools; Packer builds images for multiple platforms (AWS, Azure, GCP, Docker) from one configuration and supports Ansible, Chef, Puppet, shell, and PowerShell provisioners.
- The image is defined as code: a `dev.pkr.hcl` template with the `amazon-ebs` builder and a shell provisioner updates the kernel and installs httpd, PHP, and WordPress; the example build took 8 minutes 5 seconds on a t2.micro.
- Because Packer templates integrate with CI/CD, image builds can be reviewed, versioned, and automated like any other infrastructure change.
- Security practice favors simple, hardened base images as a supply chain control, so a golden image is both a consistency mechanism and a place to reduce attack surface.

## Related

- [infrastructure as code](/concepts/infrastructure-as-code.md) — defining the image build in version-controlled templates
- [CI/CD](/concepts/ci-cd.md) — where image builds run automatically
- [software supply chain security](/concepts/software-supply-chain-security.md) — hardening the base you build from
- [Packer](/entities/packer.md) — HashiCorp's image-building tool
- [HashiCorp](/entities/hashicorp.md) — Packer's maker
