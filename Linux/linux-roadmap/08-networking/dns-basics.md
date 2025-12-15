# DNS Basics

## Purpose
Explain how name resolution works in Linux.

## Core Concept
DNS translates hostnames into IP addresses.
Linux resolves names using configured resolvers,
usually defined in `/etc/resolv.conf`.

If DNS fails, many services appear "down"
even when the network is fine.

## Engineer Notes
Most "internet is broken" issues
are actually DNS problems.

Always test with IP addresses
to separate DNS from connectivity.

## Summary
- DNS resolves names to IPs
- Misconfiguration causes widespread failures
- Test DNS separately from networking
