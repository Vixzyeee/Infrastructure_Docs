# apt (Basics)

## Purpose
Manage packages on Debian-based systems.

## Core Concept
APT (Advanced Package Tool) is used on Debian and Ubuntu.
It installs, updates, and removes software packages.

Common commands:
- `apt update`
- `apt install`
- `apt remove`
- `apt upgrade`

## Engineer Notes
Always run `apt update` before installing packages.
Installing without updating is asking for dependency problems.

Avoid `apt dist-upgrade` unless you know what it does.

## Summary
- Package manager for Debian-based systems
- Handles installation and upgrades
- Requires updated package lists
