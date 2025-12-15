# pwd

## Purpose
Show the current working directory.

## Core Concept
The `pwd` command prints the absolute path of the directory
you are currently working in.

Linux always operates relative to a working directory.
Understanding your current location prevents mistakes
such as modifying or deleting the wrong files.

## Engineer Notes
Running `pwd` is a quick sanity check before executing
destructive commands like `rm` or `mv`.

Never assume where you are. Verify.

## Summary
- Displays the current directory
- Helps avoid operating in the wrong location
