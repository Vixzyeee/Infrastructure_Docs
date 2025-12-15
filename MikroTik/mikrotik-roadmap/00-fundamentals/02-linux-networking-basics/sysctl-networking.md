## What this covers

sysctl controls kernel networking behavior.<br>
RouterOS exposes similar tunables internally.

## Key concepts

- IP forwarding
- Reverse path filtering
- TCP behavior tuning

## Why it matters in MikroTik

Some RouterOS defaults mirror Linux defaults.<br>
Understanding intent helps tuning.

## Common mistakes

- Copy-pasting sysctl tweaks blindly
- Assuming tuning fixes design flaws

## Real-world example

Forwarding enabled, traffic still fails.<br>
rp_filter drops asymmetric routes.
