# OSI vs TCP/IP

## What is this
OSI and TCP/IP are conceptual models that describe how data moves from an application to the network and back.
OSI has 7 layers, TCP/IP simplifies them into 4 layers.

They are not configurations. They are mental models.

## Why it matters in MikroTik
MikroTik features map directly to layers:
- Firewall filter works mostly at L3/L4
- NAT works at L3/L4
- Bridge and VLAN work at L2
- Wireless lives at L1/L2

If you don’t know the layer, you debug the wrong menu.

## Key concepts
- OSI is descriptive, not implementative
- TCP/IP is what actually runs on networks
- One problem = one dominant layer
- Don’t debug Layer 7 when Layer 1 is broken

## Common mistakes
- Thinking OSI layers are strict boundaries
- Blaming firewall for physical or ARP problems
- Debugging from Winbox menus instead of packet flow

## Real-world example
Internet down because wrong MTU.
People check firewall rules.
Actual issue: Layer 2/3 mismatch, not firewall.

## Related topics
- packet-flow.md
- firewall-architecture.md
