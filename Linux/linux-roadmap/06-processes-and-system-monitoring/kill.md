# kill

## Purpose
Send signals to processes.

## Core Concept
The `kill` command sends signals
to a process using its PID.

Common signals:
- SIGTERM (default)
- SIGKILL (force)
- SIGSTOP / SIGCONT

## Engineer Notes
Always try graceful termination first.
SIGKILL should be the last resort.

Killing the wrong process
can take down critical services.

## Summary
- Sends signals to processes
- Supports graceful and forceful termination
- Dangerous if misused
