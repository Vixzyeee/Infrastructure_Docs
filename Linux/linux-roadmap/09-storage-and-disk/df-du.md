# df and du

## Purpose
Check disk space usage.

## Core Concept
`df` shows disk usage by filesystem.
`du` shows disk usage by directory or file.

They answer different questions:
- df: where is the disk space going overall
- du: which directory is consuming space

## Engineer Notes
Disk full issues are often solved
by combining df and du intelligently.

Never guess where space went.

## Summary
- df shows filesystem usage
- du shows directory usage
- Used together for troubleshooting
