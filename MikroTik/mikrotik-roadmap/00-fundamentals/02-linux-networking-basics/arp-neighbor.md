## What this covers

ARP maps IP to MAC on local networks.<br>
Without ARP, Layer 3 is blind.

## Key concepts

- ARP request vs reply
- Neighbor cache
- Timeout and refresh

## Why it matters in MikroTik

Most “routing” issues are actually ARP issues.<br>
Especially on bridges and VLANs.

## Common mistakes

- Blaming firewall for ARP failure
- Ignoring duplicate IP addresses

## Real-world example

Gateway unreachable.<br>
Actual issue: ARP conflict.
