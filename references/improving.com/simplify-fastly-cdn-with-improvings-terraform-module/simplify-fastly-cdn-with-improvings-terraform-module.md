---
type: Reference
title: "Simplify Fastly CDN with Improving’s Terraform Module"
resource: "https://www.improving.com/thoughts/simplify-fastly-cdn-with-improvings-terraform-module/"
author: "Paul Hassinger"
published: '2025-06-20'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

### **TL;DR**

Managing CDN configurations manually can be complex and prone to errors. The [terraform-fastly-service](https://github.com/improving-minnesota/terraform-fastly-service/) module, from Improving, simplifies the process by leveraging Infrastructure as Code (IaC) principles with Terraform, enabling scalable, secure, and maintainable Fastly CDN configurations.

### **The Challenges**

**Manual Configuration Overhead**:

- Manually managing Fastly services can lead to inconsistencies and deployment errors.

**Duplicate Environments**:

- Environments share common features that must be repeated manually or through code.
- Environments often drift out of sync, causing unpredictable behavior.

**Security and Observability Gaps**:

- It’s easy to overlook critical configurations such as logging or DDoS protection when managing Fastly via the UI.

### **Solution**

Improving is releasing to the open-source community. Improving's [terraform-fastly-service](https://github.com/improving-minnesota/terraform-fastly-service/) module is a Terraform module that abstracts select Fastly configuration features via the Terraform Fastly provider. It introduces a clear, maintainable approach to managing CDN configurations across multiple environments. Combined with Terragrunt, multi-environment DRY configurations are simplified. See the Multiple Environments with Terraform blog for more information about multi-environment DRY configurations.

Find the module at:

[https://github.com/improving-minnesota/terraform-fastly-service/](https://github.com/improving-minnesota/terraform-fastly-service/)

#### **Key Features**

**Comprehensive CDN Configuration Management**:

- Domains, Backends, Load Balancing, and Health Checks
- Cache Logic, VCL, Snippets, and Dictionaries
- Network ACLs, WAF, Rate Limiting, and DDoS protection
- Gzip and Image Optimization Settings
- Logging Endpoints
- and more.

**Multi-Environment Support**:

- Deploy shared global configurations with custom overrides for dev, staging, production, ephemeral, or other environments.
- Create shared modules for use among various sites.

**Security Best Practices**:

- Source control access can be limited by CODEOWNER on a per-environment level.

**Logging Integrations**:

- Supports the standard [Fastly provider](https://registry.terraform.io/providers/fastly/fastly/latest/docs) logging integrations. See [Fastly’s Developer Guide for third-party-logging](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging/).

### **Getting Started**

#### **Prerequisites**

- Terraform
- Terragrunt (optional but recommended for DRY management)
- Fastly API Key

#### **Example Usage**

```hcl
module "fastly_service" { 
  source = " git::https://github.com/improving-minnesota/terraform-fastly-service/?ref=v1" 
  fastly_api_key = "your-api-key"  # Or use a variable 
  fastly_domain_names = [ 
    { 
      name = "example.com" 
    } 
  ] 
  fastly_backends = [ 
    { 
      name    = "origin" 
      address = "origin.example.com" 
      port    = 443 
      use_ssl = true 
    } 
  ] 
} 
```

### **Best Practices**

**Version Control**:

- Track changes using Git. Review and audit every change.

**Environment Separation**:

- Use Terragrunt to remove duplication and isolate environments cleanly using DRY configuration.

**Secure Secrets**:

- Never hardcode credentials. Use Github secrets, vaults, or similar secret manager

**Enable Monitoring**:

- Logging to observability platforms ensures issues are traceable.

### **Final Thoughts**

The [`terraform-fastly-service`](https://github.com/improving-minnesota/terraform-fastly-service/) module offers a structured, automated way to manage Fastly configurations. Whether you’re deploying for a startup or an enterprise, using this module ensures:

- Modular codebase for multiple environments, creating consistent environments, less risk for drift, and dynamically scalable to new services
- Flexibility to accommodate unique environment functionalities
- Provides mechanisms for separated and secure developer workflows

Easy-to-understand and maintainable developer experience

### **What’s Next?**

Implementing stored configuration via Terraform modules to drive your Fastly CDN services is only one aspect of a complete solution. Integrating CDN, WAF, certificate management, object storage, compute, bot detection, observability, security, and CICD automation all together can drive an efficient solution for your business needs.

Need help with your CDN automation? Reach out to [Improving](https://www.improving.com/).

Improving is a modern digital services company that provides enterprise [software consulting](https://www.improving.com/services/consulting/), [development](https://www.improving.com/services/development/), and [training](https://www.improving.com/services/development/) to Fortune 500 and Global 1000 enterprises across the world. Our innovative solutions have helped thousands of our clients realize their tactical and strategic business objectives, allowing them to achieve great new heights in a competitive and ever-changing market. [Reach out to us](https://improving.com/contact) to discover how we can transform your business.
