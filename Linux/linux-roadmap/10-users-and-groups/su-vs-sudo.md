# su vs sudo

## Purpose
Explain different privilege escalation methods.

## Core Concept
`su` switches to another user account.
`sudo` runs a single command
with elevated privileges.

Sudo provides better control
and auditing than su.

## Engineer Notes
Modern systems prefer sudo.
Root shells reduce accountability.

If everything requires root,
your system design is wrong.

## Summary
- su switches users
- sudo runs commands with privileges
- sudo is safer and auditable
