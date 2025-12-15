# MAC Address and ARP

## What is this
MAC identifies devices at Layer 2.
ARP maps IP addresses to MAC addresses.

## Why it matters in MikroTik
MikroTik bridges and routers rely heavily on ARP behavior.
Firewall, DHCP, and routing all depend on correct ARP resolution.

## Key concepts
- ARP request and reply
- Dynamic vs static ARP
- ARP timeout
- Proxy ARP

## Common mistakes
- Enabling proxy ARP without understanding
- Ignoring ARP table during troubleshooting
- Assuming IP issues are routing issues

## Real-world example
Client can ping gateway but not internet due to broken ARP entry.

## Related topics
- bridge-vlan-filtering.md
- dhcp-server.md
