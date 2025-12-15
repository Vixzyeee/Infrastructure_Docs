# chmod

## Purpose
Change file and directory permissions.

## Core Concept
The `chmod` command modifies permission bits on files and directories.
Permissions can be set using symbolic or numeric notation.

Examples:
- `chmod u+x script.sh`
- `chmod 644 file.txt`
- `chmod 755 directory/`

## Engineer Notes
Numeric notation is concise but dangerous if you don’t understand it.
Symbolic notation is safer and more readable.

Avoid recursive chmod unless you are absolutely sure.

## Summary
- Changes permissions
- Supports symbolic and numeric modes
- Use carefully
