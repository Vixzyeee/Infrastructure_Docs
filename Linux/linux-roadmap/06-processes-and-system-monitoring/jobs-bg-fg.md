# Job Control (bg, fg, jobs)

## Purpose
Manage foreground and background jobs.

## Core Concept
The shell allows processes
to run in the background or foreground.

Commands:
- `jobs` list active jobs
- `bg` resume a job in background
- `fg` bring a job to foreground

## Engineer Notes
Job control is useful during long-running tasks
without opening new terminals.

This is shell-level control,
not system-wide process management.

## Summary
- Controls background and foreground jobs
- Managed by the shell
- Useful for interactive work
