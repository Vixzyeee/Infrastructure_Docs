# journalctl

## Purpose
Query logs managed by systemd.

## Core Concept
`journalctl` reads logs from the systemd journal.
Logs are indexed and structured,
not plain text files.

Common usage:
- `journalctl`
- `journalctl -u service`
- `journalctl -f`

## Engineer Notes
Journal logs persist across reboots
unless configured otherwise.

Filtering logs by service
saves massive amounts of time.

## Summary
- Reads systemd logs
- Supports filtering and follow mode
- Central log access tool
