# MTU and MSS

## What is this
MTU defines maximum frame size.

MSS defines TCP payload size.

## Why it matters in MikroTik
VPNs, tunnels, and PPP links often break due to MTU issues.

MikroTik will forward broken packets unless told otherwise.

## Key concepts
- Fragmentation
- Path MTU Discovery
- TCP MSS clamping
- Tunnel overhead

## Common mistakes
- Ignoring MTU on VPN interfaces
- Blaming firewall for packet drops
- Not adjusting MSS on PPPoE or VPN

## Real-world example
Website loads partially because large packets are dropped silently.

## Related topics
- vpn-design.md
- firewall-mangle.md
