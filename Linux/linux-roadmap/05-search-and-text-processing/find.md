# find

## Purpose
Search for files and directories by attributes.

## Core Concept
The `find` command searches the filesystem
based on name, type, size, time, and permissions.

Examples:
- `find /etc -name "*.conf"`
- `find . -type f`

## Engineer Notes
`find` is precise and powerful but slow on large filesystems.
Use it when accuracy matters.

Never run `find /` blindly on production systems.

## Summary
- Searches files by attributes
- Extremely flexible
- Powerful but potentially expensive
