# Linux Permission Model

## Purpose
Explain how Linux controls access to files and directories.

## Core Concept
Linux permissions are based on three entities:
- User (owner)
- Group
- Others

Each entity can have three types of permissions:
- Read (r)
- Write (w)
- Execute (x)

Permissions are enforced by the kernel to protect the system
from unauthorized access and accidental damage.

## Engineer Notes
Most permission problems come from misunderstanding
who the owner is versus which group is applied.

Never “fix” permission issues by blindly using chmod 777.
That is not a fix. That is surrender.

## Summary
- Permissions apply to user, group, and others
- Read, write, and execute control access
- Permissions protect system integrity
