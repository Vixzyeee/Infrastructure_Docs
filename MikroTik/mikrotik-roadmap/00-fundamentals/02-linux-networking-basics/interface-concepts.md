## What this covers

Linux networking is interface-based.<br>
Everything starts and ends at an interface.

## Key concepts

- Physical interfaces (eth0, ens18)
- Virtual interfaces (vlan, bridge, tunnel)
- Interface state: UP vs DOWN
- IP address is attached to interface, not device

## Why it matters in MikroTik

RouterOS uses the same model.<br>
No interface = no traffic.

## Common mistakes

- Expecting routing to work on DOWN interfaces
- Assigning IP without understanding interface role

## Real-world example

Interface is UP but not in bridge.<br>
Traffic never reaches firewall rules.
