# locate

## Purpose
Quickly find files using an index.

## Core Concept
The `locate` command searches a prebuilt database
instead of scanning the filesystem live.

Results may be outdated until the database is updated.

## Engineer Notes
`locate` is fast but not always accurate.
Use it for quick guesses, not audits.

## Summary
- Fast file lookup
- Uses an index
- May return outdated results
