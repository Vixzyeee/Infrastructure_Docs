## What this covers

Bridge VLAN filtering enables hardware switching.<br>
It defines which VLAN passes which port.

## Key concepts

- Bridge VLAN table
- Tagged vs untagged ports
- PVID behavior

## Why it matters in MikroTik

Without VLAN filtering, traffic hits CPU.<br>
With it, ASIC does the work.

## Common mistakes

- Enabling VLAN filtering without planning
- Forgetting management VLAN access

## Real-world example

Router becomes unreachable.<br>
Management VLAN not allowed on CPU port.
