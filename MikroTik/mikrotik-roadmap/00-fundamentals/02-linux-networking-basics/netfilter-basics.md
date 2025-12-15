## What this covers

Netfilter is Linux firewall engine.<br>
RouterOS firewall follows the same flow.

## Key concepts

- INPUT, FORWARD, OUTPUT
- Connection tracking
- Stateful filtering

## Linux vs MikroTik

iptables/nftables vs RouterOS firewall.<br>
Different syntax, same logic.

## Common mistakes

- Filtering before understanding packet direction
- Blocking traffic in wrong chain

## Real-world example

Ping blocked unexpectedly.<br>
Rule placed in INPUT instead of FORWARD.
