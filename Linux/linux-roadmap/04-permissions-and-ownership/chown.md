# chown

## Purpose
Change file or directory ownership.

## Core Concept
The `chown` command changes the owner and group of a file.

Examples:
- `chown user file.txt`
- `chown user:group file.txt`
- `chown -R user:group directory/`

## Engineer Notes
Ownership matters more than permissions in many cases.
If permissions look correct but access is denied,
ownership is often the problem.

Recursive ownership changes can break systems.
Know what you are touching.

## Summary
- Changes owner and group
- Ownership affects access control
- Recursive use is risky
