# IP Addressing

## What is this
IP addressing defines how devices identify themselves and communicate on a network.
Includes IPv4, subnet mask, gateway, and DNS.

## Why it matters in MikroTik
Almost every RouterOS feature depends on correct IP logic:
- Routing
- DHCP
- Firewall
- VPN
Wrong IP design = unstable network.

## Key concepts
- Network vs host address
- Gateway logic
- Public vs private IP
- RFC1918
- CGNAT awareness

## Common mistakes
- Using overlapping subnets
- Wrong gateway assumption
- Mixing management and user subnets
- Forgetting IP scope when routing

## Real-world example
Two WANs with same subnet cause routing ambiguity.
Router chooses wrong exit path.

## Related topics
- subnetting.md
- dhcp-client.md
