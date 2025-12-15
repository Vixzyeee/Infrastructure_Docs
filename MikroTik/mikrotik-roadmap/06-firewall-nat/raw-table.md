## What this covers

Raw table processes packets before conntrack.<br>
Used for early drops.

## Key concepts

- Prerouting only
- No connection state
- Performance optimization

## Why it matters in MikroTik

Dropping early saves CPU.<br>
Essential under attack.

## Common mistakes

- Expecting logging in raw
- Using raw for policy filtering

## Real-world example

DDoS saturates CPU.<br>
Raw rules missing.
