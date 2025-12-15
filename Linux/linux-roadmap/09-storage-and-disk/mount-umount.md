# mount and umount

## Purpose
Attach and detach filesystems.

## Core Concept
The `mount` command attaches a filesystem
to a directory in the Linux filesystem tree.

`umount` safely detaches it.

Without mounting, data on a disk
is inaccessible to the system.

## Engineer Notes
Unmounting a busy filesystem will fail.
That is protection, not a bug.

Always ensure data is synced
before unmounting storage.

## Summary
- Mount attaches filesystems
- umount detaches them safely
- Required for disk access
