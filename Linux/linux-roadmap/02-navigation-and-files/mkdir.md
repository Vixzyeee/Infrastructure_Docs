# mkdir

## Purpose
Create directories.

## Core Concept
The `mkdir` command creates one or more directories.

The `-p` option creates parent directories automatically.

## Engineer Notes
Always use `mkdir -p` in scripts.
It prevents failures when directories already exist.

## Summary
- Creates directories
- `-p` enables safe directory creation
