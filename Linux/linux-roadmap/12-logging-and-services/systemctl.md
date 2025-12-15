# systemctl

## Purpose
Manage system services.

## Core Concept
`systemctl` controls services managed by systemd.

Common actions:
- start
- stop
- restart
- enable
- disable
- status

Services define how applications
run in the background.

## Engineer Notes
Always check service status
before restarting blindly.

Restarting without understanding
often hides the real issue.

## Summary
- Controls system services
- Shows service status
- Essential for operations
