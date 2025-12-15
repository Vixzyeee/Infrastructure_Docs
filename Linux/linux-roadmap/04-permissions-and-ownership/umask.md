# umask

## Purpose
Control default permissions for new files and directories.

## Core Concept
The `umask` value defines which permission bits
are removed when new files or directories are created.

It does not set permissions directly.
It subtracts permissions from defaults.

## Engineer Notes
Umask explains why new files are not executable by default
and why directories usually start with 755 instead of 777.

Understanding umask prevents confusion when permissions
do not match expectations.

## Summary
- Defines default permission masking
- Affects newly created files
- Does not modify existing files
