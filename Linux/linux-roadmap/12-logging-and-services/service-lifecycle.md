# Service Lifecycle

## Purpose
Explain how services start, stop, and fail.

## Core Concept
A service has a lifecycle:
- start
- running
- stop
- failure
- restart

Systemd manages dependencies
and restart behavior.

Understanding lifecycle
prevents endless restart loops.

## Engineer Notes
If a service keeps restarting,
it is failing.
Fix the cause, not the symptom.

Service logs explain the failure.

## Summary
- Services follow a lifecycle
- Failures are logged
- Fix root causes, not restarts
