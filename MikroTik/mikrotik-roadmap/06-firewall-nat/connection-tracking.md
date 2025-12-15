## What this covers

Connection tracking makes firewall stateful.<br>
Router remembers flows.

## Key concepts

- New, established, related
- Connection table
- Timeout behavior

## Why it matters in MikroTik

Most firewall logic depends on conntrack.<br>
Disabling it breaks many features.

## Common mistakes

- Disabling conntrack blindly
- Forgetting fasttrack interaction

## Real-world example

Return traffic blocked.<br>
Conntrack disabled.
