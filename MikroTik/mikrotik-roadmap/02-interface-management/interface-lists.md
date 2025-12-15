## What this covers

Interface lists group interfaces by role.<br>
They simplify firewall and routing logic.

## Key concepts

- WAN vs LAN roles
- Dynamic membership
- Policy abstraction

## Why it matters in MikroTik

Firewall rules should target roles.<br>
Not specific interfaces.

## Common mistakes

- Writing firewall rules per interface
- Forgetting to update rules when interface changes

## Real-world example

New WAN added.<br>
Firewall ignores it due to missing list entry.
