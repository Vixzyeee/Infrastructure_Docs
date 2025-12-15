## What this covers

Packet flow shows how traffic moves inside RouterOS.<br>
Understanding order is critical.

## Key concepts

- Prerouting
- Input vs forward
- Postrouting

## Why it matters

Firewall and NAT depend on flow.<br>
Wrong assumption breaks rules.

## Common mistakes

- Expecting NAT before filter
- Misplacing mangle rules

## Real-world example

Firewall rule never hits.<br>
Placed in wrong chain.
