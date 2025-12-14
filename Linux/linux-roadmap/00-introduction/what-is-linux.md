# What Is Linux

## Purpose
This section explains what Linux actually is and clears common misconceptions,
especially the idea that Linux is a full operating system by itself.

## Core Concept
Linux is a kernel, not a complete operating system.
The kernel is responsible for managing hardware resources such as CPU, memory,
processes, and devices.

What people usually call “Linux” is actually a Linux distribution.
A distribution bundles the Linux kernel with system libraries, userland tools,
a package manager, and default configurations to form a usable operating system.

Linux is designed from the ground up to support multi-user and multi-tasking
environments, which makes it suitable for servers, cloud systems, and infrastructure workloads.

## Engineer Notes
Understanding that Linux is a kernel helps explain why different distributions
behave differently while still sharing the same core principles.
As an engineer, you interact mostly with userland tools, but system behavior
is ultimately controlled by the kernel.

This distinction becomes important when troubleshooting performance,
hardware compatibility, and system-level issues.

## Summary
- Linux is a kernel, not a full operating system
- Distributions package the kernel with tools and libraries
- Linux is built for multi-user, multi-tasking systems
