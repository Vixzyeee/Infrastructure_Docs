# Crontab

## Purpose
Explain how cron jobs are configured.

## Core Concept
Crontab files define scheduled jobs
for users and the system.

Commands:
- `crontab -e`
- `crontab -l`
- `crontab -r`

Each line represents a scheduled task.

## Engineer Notes
Redirect output to logs.
Silent failures are common without logging.

Version control cron configurations
whenever possible.

## Summary
- Defines scheduled jobs
- User and system crontabs exist
- Logging is critical
