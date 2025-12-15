# Storage Basics

## Purpose
Introduce how Linux handles disks, partitions, and filesystems.

## Core Concept
Linux treats storage devices as block devices.
Disks can be divided into partitions,
and partitions are formatted with filesystems.

Filesystems are mounted into a single directory tree.
There are no drive letters like in Windows.

## Engineer Notes
Most storage issues come from misunderstanding mounts.
A disk can exist and still not be accessible
if it is not mounted.

## Summary
- Disks are block devices
- Partitions hold filesystems
- Filesystems must be mounted
