---
type: Reference
title: "Tech Tuesday: Single Node Kubernetes on Raspberry Pi 4"
resource: "https://www.improving.com/thoughts/single-node-kubernetes-on-raspberry-pi/"
author: "Dan Peterson"
published: '2022-02-22'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

In this post, I will go through the steps I used to create a single-node Kubernetes combination master and worker node on a Raspberry Pi 4. The heavy lifting in this post is done via the Rancher K3s (lightweight Kubernetes) binary.

Rancher K3s: https://rancher.com/docs/k3s/latest/en/

Pre-requisites:

- **Raspberry Pi 4 Model B Rev 1.4**
- **8 GB RAM**
- **64 Bit OS Debian ‘Buster’**
- **64 GB (or larger) SD Card**

## Installing 64 Bit Debian Buster

Using this tool, create an image of the 64 bit Buster OS

Once complete, and you have booted and connected to your new Pi image, verify the installation with the following

- **cat /etc/os-release |grep PRETTY_NAME**
- **uname -a**

You should see the ‘Buster’ and ‘aarch64’ in the respective outputs.

## Installing Rancher K3s

- **curl -sfL https://get.k3s.io | sh -s – –write-kubeconfig-mode 644**
- **sudo chmod 755 /etc/rancher/k3s/k3s.yaml**
- **sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config**

Next, verify with:

- **systemctl status k3s.service**
- **kubectl get pods**
- **k3s kubectl cluster-info**

Sample Python Pod Image for ARM64 Architecture

Copy the following into the file ‘python_pod.yaml’, and run the commands to create the pod, retrieve the logs showing the python version, then destroy the pod.

`apiVersion: v1 `

`kind: Pod `

`metadata: `

` name: python36-arm-demo `

` labels: `

` purpose: container-args `

`spec: `

` containers: `

` - name: python36-demo-container-args `

` image: arm64v8/python:3.6 `

` command: ["/usr/local/bin/python3"] `

` args: ["--version"] `

` restartPolicy: OnFailure `

- **kubectl apply -f python_pod.yaml**
- **kubectl get pods**
- **kubectl logs python36-arm-demo**
- **kubectl delete -f python_pod.yaml**
