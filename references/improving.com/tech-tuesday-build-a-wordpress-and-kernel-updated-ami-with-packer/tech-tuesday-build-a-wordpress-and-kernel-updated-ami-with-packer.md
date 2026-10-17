---
type: Reference
title: "Tech Tuesday: Let’s Build a WordPress & Kernel Updated AMI with Packer"
resource: "https://www.improving.com/thoughts/tech-tuesday-build-a-wordpress-and-kernel-updated-ami-with-packer/"
author: "Emir Koroglu"
published: '2022-03-29'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

## What is an AMI?

An **Amazon Machine Image **(AMI) is a master image for the creation of virtual servers in an AWS environment. The machine images are like templates that are configured with an operating system and other software, which determines the user’s operating system. AMI types are categorized according to region, operating system, system architecture (32- or 64-bit), launch permissions, and whether they are backed by Amazon EBS or backed by the instance store. AMIs provide the information required to launch an Amazon EC2 instance, which is a virtual server in the AWS Cloud.

Each AMI includes the following:

- **A template for the instance’s root device volume**
- **Set up permissions that control which Amazon Web Services (AWS) accounts can use the machine images to spin up an instance**
- **The block devices that specify the root device volume to attach to the EC2 instance once it’s launched**

## How to Build AMI

There are various tools available for building the golden AMIs and some of the most used ones are

- **Hashicorp’s Packer**
- **AWS Image Builder**

We will use Hashicorp’s Packer to create our Golden AMI.

Let me tell you about Packer also:

- **Packer allows you to build images for multiple platforms like AWS, Azure, GCP, Docker, etc. using the same configuration files.**
- **Packer is simple in terms of logging and debugging as the output is clearly shown in the command-line when the image is built.**
- **Packer uses JSON files to build the components which are simple commands and can be easily integrated with CI/CD pipelines.**
- **Packer has built-in support for using various configuration management tools like Ansible, Chef, and Puppet along with Shell and PowerShell script support for installing software.**
- **Packer is distributed as a lightweight binary and it is controlled using CLI.**

## Installing Packer on AWS EC2 Centos

**First**, you need to have an EC2 instance running on AWS with admin IAM role attached for testing purposes. I will be using an EC2 instance with CentOS 7 AMI. We also need to get the ssh public key for the instance and save it as packer on AWS key pairs which is located in EC2.

For your operating system you can check the HashiCorp Packer official installation page right from here; https://learn.hashicorp.com/tutorials/packer/get-started-install-cli

Below I have installation commands for Linux CentOS 7.

**Second**, we will install yum config manager to manage our repositories then we will add the official HashiCorp Linux repository then install Packer.

- **sudo yum install -y yum-utils**
- **sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo**
- **sudo yum -y install packer**
- **packer --version**

Now we can start creating a template. Let’s first create a folder called WordPress then we need to create a file inside that which will be called **dev.pkr.hcl**

Copy the following into the file `dev.pkr.hcl`

Below code will create an updated CentOS 7 Kernel and WordPress installed AMI.

`packer { required_plugins { amazon = { version = ">= 0.0.1" source = "github.com/hashicorp/amazon" } } } variable "ssh_private_key_file" { default = "/home/centos/.ssh/id_rsa" } // save your local machine ssh public key to aws then replace the ssh keypair name below. variable "ssh_keypair_name" { default = "packer" } variable "source_ami_name" { default = "CentOS Linux 7 x86_64 HVM EBS ENA 1901_01-b7ee8a69-ee97-4a49-9e68-afaee216db2e-*" } variable "instance_type" { default = "t2.micro" } variable "ssh_username" { default = "centos" } variable "ami_name" { default = "bastion_wordpress_kernel_updated" } variable "region" { default = "us-east-1" } variable "owners" { default = "679593333241" } source "amazon-ebs" "image" { ami_name = "${var.ami_name} {{timestamp}}" ssh_private_key_file = "${var.ssh_private_key_file}" ssh_keypair_name = "${var.ssh_keypair_name}" instance_type = "${var.instance_type}" ssh_username = "${var.ssh_username}" region = "${var.region}" source_ami_filter { most_recent = true owners = ["${var.owners}"] filters = { name = "${var.source_ami_name}" virtualization-type = "hvm" root-device-type = "ebs" ` ` } } run_tags = { Name = "Packer instance for ${var.source_ami_name}" } } build { sources = [ "source.amazon-ebs.image" ] provisioner "shell" { inline = [ "echo Installing Telnet", "sudo yum update kernel -y", "sudo yum install telnet -y", #Change for ubuntu ` ` "sudo yum install elinks -y", #Change for ubuntu "sudo yum install httpd -y", "sudo yum install php -y", "sudo systemctl restart httpd", "sudo systemctl enable httpd", "sudo yum install wget -y", "sudo wget https://wordpress.org/wordpress-4.0.32.tar.gz", "sudo tar -xf wordpress-4.0.32.tar.gz -C /var/www/html/", ` ` "sudo mv /var/www/html/wordpress/* /var/www/html/", "sudo yum install php-mysql -y", "sudo systemctl restart httpd", "sudo chown -R apache:apache /var/www/html/", "sudo systemctl restart httpd" ] } provisioner "breakpoint" { note = "Waiting for your verification" } } `

Inside our WordPress folder let’s run some packer commands to start building our AMI.

**packer init .**

**packer validate .**

**packer build .**

Packer will start an EC2 instance to build our AMI and you can verify if the tools are installed by ssh to the packer-created instance from our EC2 instance. If tools are installed correctly please verify and continue for packer build in our terminal.

Build ‘amazon-ebs.image’ finished after 8 minutes 5 seconds.

==> Wait completed after 8 minutes 5 seconds

==> Builds finished. The artifacts of successful builds are: –> amazon-ebs.image: AMIs were created: us-east-1: ami-055afae0b53a0262e

For me, it took 8 minutes 5 seconds to complete and make an AMI. You can make this faster by changing the instance type at the above packer code. Created WordPress & Kernel updated AMI will be located under EC2 > Images > AMI’s > Owned by me
