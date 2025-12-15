# Subnetting

## What is this
Subnetting divides a network into smaller logical networks.
It controls broadcast domain size and routing behavior.

## Why it matters in MikroTik
Subnet size affects:
- DHCP performance
- ARP table size
- Firewall scalability
- Broadcast noise

MikroTik does not protect you from bad subnet design.

## Key concepts
- Network address
- Broadcast address
- Usable host range
- Prefix length

## Common mistakes
- Using /24 everywhere without thinking
- Oversized LANs
- Miscalculating usable IP range
- Forgetting point-to-point subnet efficiency

## Real-world example
Using /24 for point-to-point links wastes IPs and increases ARP noise.

## Related topics
- cidr-vlsm.md
- routing-concepts.md
