# dpkg

## Purpose
Manage individual Debian package files.

## Core Concept
`dpkg` works at a lower level than APT.
It installs `.deb` files directly
without resolving dependencies automatically.

APT uses dpkg internally.

## Engineer Notes
If dpkg reports dependency errors,
APT is usually the tool to fix them.

Using dpkg directly is situational, not daily workflow.

## Summary
- Low-level package tool
- Installs `.deb` files
- Does not resolve dependencies automatically
