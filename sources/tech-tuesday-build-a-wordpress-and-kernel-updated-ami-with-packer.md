---
title: "Tech Tuesday: Let's Build a WordPress & Kernel Updated AMI with Packer"
type: "Source Summary"
description: "Step-by-step walkthrough of using HashiCorp Packer to build a golden AWS AMI with an updated CentOS 7 kernel and WordPress."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, cloud, improving.com]
sources:
  - "references/improving.com/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer.md"
---

# Tech Tuesday: Let's Build a WordPress & Kernel Updated AMI with Packer — Summary

**Original source**: `references/improving.com/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer.md`

## Summary

A hands-on tutorial on using HashiCorp Packer to build a golden Amazon Machine Image (AMI) with an updated CentOS 7 kernel and WordPress installed. It defines an HCL template and runs packer init, validate, and build, ending with a created AMI in us-east-1.

## Key Claims

- An AMI is a master image or template for launching EC2 instances, categorized by region, OS, architecture, launch permissions, and storage backing.
- Common golden-AMI tools are HashiCorp Packer and AWS Image Builder; the post uses Packer.
- Packer builds images for multiple platforms (AWS, Azure, GCP, Docker) from the same configuration, integrates with CI/CD, and supports Ansible, Chef, Puppet, shell, and PowerShell.
- Packer is distributed as a lightweight CLI binary; the example installs it on CentOS 7 via the official HashiCorp yum repository.
- The dev.pkr.hcl template uses the amazon-ebs builder and a shell provisioner to update the kernel and install httpd, PHP, and WordPress, plus a breakpoint provisioner for verification.
- The build took 8 minutes 5 seconds on a t2.micro and produced an AMI visible under EC2 > Images > AMIs.

## Relevance

Informs [golden image](/concepts/golden-image.md) and [infrastructure as code](/concepts/infrastructure-as-code.md) via [Packer](/entities/packer.md) on [AWS](/entities/aws.md).

## Quality

Practitioner tutorial by Emir Koroglu; concrete commands and template code, though tied to an old CentOS 7 / WordPress 4.0.32 example.

## Entities Mentioned

- [Packer](/entities/packer.md) — the image-building tool used
- [HashiCorp](/entities/hashicorp.md) — Packer's maker
- [AWS](/entities/aws.md) — cloud target

## Concepts Covered

- [golden image](/concepts/golden-image.md) — main topic
- [infrastructure as code](/concepts/infrastructure-as-code.md) — template-driven builds
- [CI/CD](/concepts/ci-cd.md) — where Packer templates integrate
