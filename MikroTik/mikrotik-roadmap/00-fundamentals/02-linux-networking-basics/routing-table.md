## What this covers

Routing table decides where packets go.<br>
Not firewall. Not NAT.

## Key concepts

- Destination prefix
- Gateway / next-hop
- Distance and metric
- Longest prefix match

## Linux vs MikroTik

Linux uses `ip route`.<br>
MikroTik uses `/ip route`.

Logic is identical.

## Common mistakes

- Assuming default route always wins
- Forgetting more specific routes override defaults

## Real-world example

Packet exits wrong WAN.<br>
More specific route beats default.
