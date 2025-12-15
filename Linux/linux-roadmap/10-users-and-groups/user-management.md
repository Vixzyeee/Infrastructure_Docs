# User Management

## Purpose
Manage user accounts on a Linux system.

## Core Concept
Users are created, modified, and removed
using commands such as:
- `useradd`
- `usermod`
- `userdel`

Each user has:
- a UID
- a home directory
- a default shell

## Engineer Notes
Never share user accounts.
Auditability disappears when everyone is “admin”.

Service accounts should be separate
from human users.

## Summary
- Users have unique identities
- Accounts include home and shell
- Separation improves security
