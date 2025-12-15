# Linux Boot Process

## Purpose
Introduce how Linux starts up.

## Core Concept
The boot process includes:
- firmware (BIOS/UEFI)
- bootloader
- kernel initialization
- init system (systemd)
- service startup

Each stage must succeed
for the system to become usable.

## Engineer Notes
Boot failures often relate to:
- broken fstab
- failed services
- missing disks

Logs are available even during boot failures.

## Summary
- Boot happens in stages
- systemd manages startup
- Logs help diagnose boot issues
