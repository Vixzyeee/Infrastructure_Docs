# /etc/fstab

## Purpose
Configure persistent filesystem mounts.

## Core Concept
The `/etc/fstab` file defines
which filesystems are mounted at boot.

Entries include:
- device or UUID
- mount point
- filesystem type
- mount options

Incorrect fstab entries
can prevent the system from booting.

## Engineer Notes
Always test fstab changes carefully.
One typo can drop you into recovery mode.

Use UUIDs instead of device names.

## Summary
- Controls automatic mounts
- Processed at boot
- Errors can break startup
