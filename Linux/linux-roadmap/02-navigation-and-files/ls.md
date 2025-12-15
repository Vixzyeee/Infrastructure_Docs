# ls

## Purpose
List the contents of a directory.

## Core Concept
The `ls` command displays files and directories
inside a given path or the current directory.

Common options:
- `-l` for detailed listing
- `-a` to show hidden files
- `-h` for human-readable sizes

## Engineer Notes
Hidden files often contain configuration.
Ignoring them leads to confusion.

Use `ls -la` when debugging filesystem issues.

## Summary
- Lists directory contents
- Options control detail and visibility
