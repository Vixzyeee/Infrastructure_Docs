# Globbing

## Purpose
Match multiple files using patterns.

## Core Concept
Globbing allows the shell to expand patterns such as:
- `*` matches any characters
- `?` matches a single character
- `[]` matches character ranges

Example:
`rm *.log`

## Engineer Notes
Globbing is handled by the shell, not commands.
Always verify expanded paths before destructive actions.

## Summary
- Enables pattern-based file matching
- Performed by the shell
