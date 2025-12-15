# UFW (Uncomplicated Firewall)

## Purpose
Manage firewall rules simply on Ubuntu-based systems.

## Core Concept
UFW is a frontend for iptables.
It simplifies common firewall tasks.

Typical usage:
- allow SSH
- deny all other inbound traffic

## Engineer Notes
Always allow SSH before enabling UFW.
Locking yourself out is a rite of passage,
but not a good one.

## Summary
- Simple firewall interface
- Common on Ubuntu
- Easy to misconfigure if careless
