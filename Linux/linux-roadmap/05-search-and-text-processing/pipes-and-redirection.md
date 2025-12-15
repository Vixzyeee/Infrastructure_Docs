# Pipes and Redirection

## Purpose
Combine commands and control input/output.

## Core Concept
Pipes (`|`) send output from one command
directly into another command.

Redirection:
- `>` overwrite output
- `>>` append output
- `<` use file as input

Example:
`grep error app.log | less`

## Engineer Notes
Pipes are the core of Unix philosophy.
Small tools combined become powerful workflows.

Once this clicks, Linux stops feeling clumsy.

## Summary
- Pipes connect commands
- Redirection controls input/output
- Enables powerful command chains
