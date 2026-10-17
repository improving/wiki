---
type: Reference
title: "Multiple Environments with Terraform"
resource: "https://www.improving.com/thoughts/multiple-environments-with-terraform/"
author: "Paul Hassinger"
published: '2025-06-13'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

## DRY IaC Configurations

[Terraform](https://developer.hashicorp.com/terraform) is a fantastic tool for creating Infrastructure as Code (IaC) solutions. Don’t Repeat Yourself (DRY) configurations are ideal to prevent duplication of configuration settings by centralizing them. Common industry-standard DRY Terraform configuration approaches exist, but many options have caveats that make them less desirable. I am sharing a DRY IaC solution that I use, which addresses most of these issues by utilizing [Terragrunt](https://terragrunt.gruntwork.io/) to combine several approaches.

### Terraform Workspaces

Terraform [workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces) allow state to be independently stored per environment for a single IaC configuration. On its workspace page, Hashicorp states, “Workspaces are not appropriate for system decomposition or deployments requiring separate credentials and access controls. Refer to [Use Cases](https://developer.hashicorp.com/terraform/cli/workspaces#use-cases) in the Terraform CLI documentation for details and recommended alternatives.” The Use Cases page makes it clear that there are many limitations and not recommended for isolating environments.

HCP Terraform workspaces address some of the issues but require using its cloud platform and essentially separates these workspaces into its own independent configuration, causing plenty of room for drift and duplication of code.

### Terraform Modules

One industry best practice to achieve DRY configurations is to utilize [Terraform modules](https://developer.hashicorp.com/terraform/language/modules). By utilizing these modules using differing variables, IaC code can call the module repeatedly for various environments. This keeps settings that don’t change, global, within the module. Dynamic settings are kept outside of the module in the calling code.

This approach, however, still has several issues. Namely, state backend configuration needs to be repeated as well as having disjointed environment configurations that need to be updated independently and could cause drift in the stored configurations that are used.

### Terragrunt

Terragrunt was built to address many of the issues needed to obtain DRY Terraform IaC configurations. The use of Terragrunt has some controversy among some engineers in the industry, but I believe many of those arguments to be flawed, and in some cases, where it is a valid point, the DRY benefits of using Terragrunt often outweigh those points. This is especially true when the size and maintainability of IaC configurations become unwieldy, but can also provide benefits for smaller use-cases.

Utilizing Terragrunt addresses DRY Terraform IaC code issues in several ways. Dynamic configurations can be centralized for inputs, modules, providers, and state backends. In addition, the IaC code can include other IaC code without having to create a completely separate module.

Even while utilizing shared (I’ll call it global) code or settings, we can design our solution in such a way that we can add to that code or override it completely. In addition to overriding variables, we can also include modules with varying release versions if desired. This might especially be important if you have a sandbox environment where you want to test a new version of a module or settings without affecting any other environments using your global configuration. Expand these types of customizations into your CICD system, and code then becomes manageable instead of a spiderweb of duplicate code to be maintained.

## DRY Terragrunt Solution

Let’s build out the structure for a sample project that passes ACLs and a domain name to a module.

### Project Structure

We will end up with the following project structure:

multiple-environments-project

`├── dev `

`│ ├── acls.tf `

`│ ├── environment.auto.tfvars `

`│ ├── terragrunt.hcl `

`│ └── variables.tf `

`├── global `

`│ ├── global-acls.tf `

`│ ├── global-main.tf `

`├── prod `

`│ ├── acls.tf `

`│ ├── environment.auto.tfvars `

`│ ├── terragrunt.hcl `

`│ └── variables.tf `

`└── terragrunt-root.hcl `

### terragrunt-root.hcl

This file is used for shared root project settings. Typically, this would include remote state settings or provider configurations. For this demonstration, state is not needed, so this could be an empty file.

```hcl
locals { 
  environment_remote_backend = get_env("REMOTE_STATE_CREDENTIALS", "") != "" ? "remote_state_tbd" : "local" 
} 
generate "backend" { 
  path      = "backend.tf" 
  if_exists = "overwrite_terragrunt" 
  contents  = <<EOF 
terraform { 
  %{if local.environment_remote_backend == "local"} 
  backend "local" { 
    path   = "terraform.tfstate" 
  } 
  %{else} 
  backend "remote_state_tbd" { 
    bucket = "myproject-tfstate-${basename(get_terragrunt_dir())}" 
  } 
  %{endif} 
} 
  EOF 
} 
```

### terragrunt.hcl

This file is used in each environment directory to inherit terragrunt root settings. We also use it to include global code.

```hcl
terraform { 

  source = "${get_terragrunt_dir()}/../global" 

} 

 

include "root" { 

  path = find_in_parent_folders("terragrunt-root.hcl") 

} 
```

### variables.tf

This file is used in each environment directory to set environmental variables that could be dynamic per-environment, or credentials to be passed to the module.

```hcl
variable "environment_name" { 

  description = "Environment Name" 

  type        = string 

} 
```

### environment.auto.tfvars

This file is used in each environment directory to set environmental tfvars. This might commonly be the name of an environment.

```hcl
environment_name = "dev|prod" 
```

### global-main.tf

This file is used to globally call the primary module for all environments. This same functionality could be placed in each environment, but by keeping it in the global directory, it will automatically be used by the environments. The module uses an input for ACLs of the local ACLs defined for each environment.

```hcl
module "my_reusable_module" { 

  source               = "path-to-my-module" 

  domain               = var.environment_name 

  acls                 = local.acls 

} 
```

### global-acls.tf

This file is used to globally set ACLs to be used for any environment that chooses to do so.

```hcl
locals { 

  global_myobjects = [ 

    { 

      name = "Home" 

      entries = [ 

        { ip = "192.168.1.1" }, 

        { ip = "192.168.1.2" }, 

      ] 

    }, 

    { 

      name = "Office" 

      entries = [ 

        { ip = "192.168.2.1" }, 

        { ip = "192.168.2.2" }, 

      ] 

    }, 

  ] 

}
```

### acls.tf

This file is used in each environment directory to set a local ACL variable. In the prod example, we simply use whatever is in global ACLs. For dev, we add a third ACL that we desire to test, in addition to the global ACLs.

Prod:

```hcl
locals { 

  acls = concat( 

    local.global_acls, 

  ) 

} 
```

Dev:

```hcl
locals { 

  acls = concat( 

    local.global_acls, 

    { 

      name = "Dev Datacenter" 

      entries = [ 

        { ip = "192.168.3.1" }, 

        { ip = "192.168.3.2" }, 

      ] 

    }, 

  ) 

}
```

### Executing

Executing the Terraform code with Terragrunt becomes a simple matter:

```hcl
terragrunt init --all 

terragrunt plan --all 

terragrunt apply --all --queue-include-dir dev 

terragrunt apply --all --queue-include-dir production 

terragrunt destroy –all 
```

## Final Thoughts

While many solutions exist to manage multiple environments with Terraform, with the example provided, we end up with a flexible Terraform IaC solution that abstracts global functionality for reusability and ease-of-maintenance while still allowing the ability to override per-environment settings or functionality.

Implementing multiple environments to use DRY IaC Terraform configuration with Terragrunt provides manageable code, whether using just a few environments, many, or even ephemeral environments. Integrate this to simplify CICD workflows and let it accelerate your business.

These types of solutions and customizations allow for great flexibility and efficiency for your business needs. To learn more about how our customized solutions can drive your business success, [reach out to us](https://www.improving.com/contact)!
