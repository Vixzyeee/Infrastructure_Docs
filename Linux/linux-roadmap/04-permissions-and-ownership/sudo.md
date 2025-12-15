# sudo

## Purpose
Execute commands with elevated privileges.

## Core Concept
The `sudo` command allows permitted users
to run commands as another user, typically root.

It provides controlled administrative access
without logging in as the root user.

## Engineer Notes
Using sudo leaves an audit trail.
Direct root access does not.

Never run sudo commands blindly.
You are bypassing safety mechanisms.

## Summary
- Executes commands with elevated privileges
- Preferred over direct root login
- Powerful and dangerous if misused
