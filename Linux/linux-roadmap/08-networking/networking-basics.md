# Networking Basics

## Purpose
Introduce fundamental networking concepts in Linux.

## Core Concept
Linux networking is based on standard TCP/IP concepts.
A system communicates using network interfaces,
IP addresses, routing tables, and ports.

Most network issues fall into one of these categories:
- interface is down
- IP configuration is wrong
- routing is incorrect
- DNS is broken

## Engineer Notes
Always start debugging from the lowest layer:
interface → IP → route → DNS → application.

Skipping layers wastes time.

## Summary
- Linux uses standard TCP/IP networking
- Interfaces, IPs, and routes matter
- Debug from low level to high level
