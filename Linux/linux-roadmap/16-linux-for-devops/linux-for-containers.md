# Linux for Containers

## Purpose
Explain why containers depend on Linux.

## Core Concept
Containers rely on Linux kernel features:
- namespaces
- cgroups
- filesystem isolation

Docker and container runtimes
are interfaces over these kernel capabilities.

Containers are not virtual machines.

## Engineer Notes
Understanding Linux isolation
makes container behavior predictable.

If you don’t understand the kernel features,
containers look like magic.

## Summary
- Containers rely on Linux kernel features
- Isolation is provided by namespaces and cgroups
- Containers are not VMs
