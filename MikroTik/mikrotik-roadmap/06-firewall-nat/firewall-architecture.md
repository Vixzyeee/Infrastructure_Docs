## What this covers

Firewall processes packets in defined chains.<br>
Order matters more than rule count.

## Key concepts

- INPUT, FORWARD, OUTPUT
- Packet direction
- First-match logic

## Why it matters in MikroTik

Wrong chain means rule never hits.<br>
Most firewall bugs come from this.

## Common mistakes

- Filtering LAN traffic in INPUT
- Assuming NAT affects firewall order

## Real-world example

Rule looks correct.<br>
Placed in wrong chain.
