# File Encoding and Line Endings

## Purpose
Explain why text files sometimes behave unexpectedly.

## Core Concept
Text files use character encodings such as UTF-8.
Different operating systems also use different line endings.

Linux uses LF (`\n`), while Windows commonly uses CRLF (`\r\n`).

## Engineer Notes
Encoding and line-ending issues often cause script failures.
Understanding this prevents subtle and frustrating bugs.

## Summary
- Text files use character encodings
- Line endings differ across operating systems
