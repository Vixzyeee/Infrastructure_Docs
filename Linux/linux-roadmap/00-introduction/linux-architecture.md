# Linux Architecture

## Purpose
This section introduces the high-level architecture of a Linux system
to help understand how different components interact.

## Core Concept
Linux uses a layered architecture.

At the lowest level is the hardware, which includes the CPU, memory,
storage devices, and network interfaces.

Above the hardware sits the Linux kernel.
The kernel is responsible for process scheduling, memory management,
device drivers, file systems, and system calls.

On top of the kernel is user space.
User space includes system libraries, background services (daemons),
shells, and user applications.
Applications interact with hardware indirectly through the kernel.

The separation between kernel space and user space is fundamental
to system stability and security.

## Engineer Notes
Most engineering work happens in user space, but system issues often
originate in kernel-level behavior.
High CPU usage, memory pressure, or I/O bottlenecks usually involve
kernel resource management.

Understanding which layer a problem belongs to helps reduce
guesswork and speeds up troubleshooting.

## Summary
- Linux follows a layered architecture
- The kernel manages hardware and system resources
- User space contains applications and services
