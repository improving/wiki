---
title: "HashiCorp Packer"
type: "Entity"
description: "HashiCorp's tool for building golden machine images as code across cloud platforms."
created: '2026-10-17'
updated: '2026-10-17'
tags: [infrastructure-as-code, hashicorp, cloud]
sources:
  - "/sources/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer.md"
---

# HashiCorp Packer

HashiCorp's image-building tool, used in this corpus to build a golden Amazon Machine Image (AMI) as code. Only one summary in the corpus covers it in depth, so this page is deliberately short: Packer is the [golden-image](/concepts/golden-image.md) builder in the [infrastructure-as-code](/concepts/infrastructure-as-code.md) toolchain.

## How It Is Used

- An AMI is a master image or template for launching EC2 instances, categorized by region, OS, architecture, launch permissions, and storage backing.
- Common golden-AMI tools are HashiCorp Packer and AWS Image Builder; the corpus uses Packer.
- Packer builds images for multiple platforms (AWS, Azure, GCP, Docker) from the same configuration, integrates with [ci-cd](/concepts/ci-cd.md), and supports Ansible, Chef, Puppet, shell, and PowerShell provisioners.
- It ships as a lightweight CLI binary; the example installs it on CentOS 7 via the official HashiCorp yum repository.
- The dev.pkr.hcl template uses the amazon-ebs builder and a shell provisioner to update the kernel and install httpd, PHP, and WordPress, plus a breakpoint provisioner for verification.
- The example build took 8 minutes 5 seconds on a t2.micro and produced an AMI visible under EC2 > Images > AMIs.

## Related

- [HashiCorp](/entities/hashicorp.md) — Packer's maker
- [golden-image](/concepts/golden-image.md) — the artifact Packer produces
- [infrastructure-as-code](/concepts/infrastructure-as-code.md) — template-driven builds
