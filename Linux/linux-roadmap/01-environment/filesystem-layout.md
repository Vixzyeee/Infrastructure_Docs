# Linux Filesystem Layout

## Purpose
This section explains the standard Linux filesystem hierarchy
and the role of important directories.

## Core Concept
Linux uses a single-root filesystem starting at `/`.
All files and directories branch from this root.

Key directories include:
- `/` : Root of the filesystem
- `/home` : User home directories
- `/etc` : System configuration files
- `/var` : Variable data such as logs and caches
- `/bin` and `/usr/bin` : Essential user commands
- `/sbin` and `/usr/sbin` : System administration commands
- `/tmp` : Temporary files

This structure is defined by the Filesystem Hierarchy Standard (FHS),
which helps maintain consistency across Linux systems.

## Engineer Notes
Understanding where files live is critical for troubleshooting.
Configuration issues often involve `/etc`,
log-related problems usually involve `/var/log`,
and user-level issues often live under `/home`.

Randomly searching the filesystem without knowing the layout
is inefficient and error-prone.

## Summary
- Linux uses a single-root filesystem
- Each top-level directory has a specific purpose
- Filesystem knowledge speeds up troubleshooting
