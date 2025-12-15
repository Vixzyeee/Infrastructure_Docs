# /etc/passwd and /etc/shadow

## Purpose
Explain where Linux stores user information.

## Core Concept
User account information is stored in `/etc/passwd`.
Password hashes are stored in `/etc/shadow`.

The separation improves security
by limiting access to sensitive data.

## Engineer Notes
Never edit these files casually.
User management commands exist for a reason.

Understanding these files helps
when recovering broken systems.

## Summary
- passwd stores user metadata
- shadow stores password hashes
- Separation improves security
