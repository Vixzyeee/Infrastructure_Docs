# ss and netstat

## Purpose
Inspect network sockets and connections.

## Core Concept
The `ss` command shows active sockets,
listening ports, and connection states.

`netstat` is older and often deprecated,
but still appears on some systems.

## Engineer Notes
Use `ss` whenever possible.
It is faster and more accurate than `netstat`.

This is how you check
"what is listening on this port?"

## Summary
- Shows network connections
- ss is preferred over netstat
- Useful for port diagnostics
