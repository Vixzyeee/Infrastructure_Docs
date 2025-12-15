# CIDR and VLSM

## What is this
CIDR removes class-based IP limitations.<br>
VLSM allows variable subnet sizes based on need.

## Why it matters in MikroTik
Routing decisions depend on prefix length.

Longest prefix match decides traffic flow.

Bad CIDR design breaks routing logic.

## Key concepts
- Prefix aggregation
- Longest prefix match
- Route summarization
- Efficient IP allocation

## Common mistakes
- Forgetting route priority over distance
- Poor summarization causing large routing tables
- Overlapping CIDR blocks

## Real-world example
Traffic goes to wrong gateway because /24 route overrides /16 default.

## Related topics
- routing-tables.md
- routing-filters.md
