```bash
# Lab 3: Connecting to MikroTik via SSH

## Objective
Learn how to connect to a MikroTik RouterBOARD using:
1. SSH

## Requirements
- WinBox installed
  - Example: WinBox 4.0beta42
- RouterBOARD device powered on
  - Example: RouterBOARD 951-2n
- RouterOS version used in this lab
  - Example: 6.49.13 (long-term)
- RouterBOARD architecture
  - Example: MIPSBE (AR9344)
- Ethernet connection between PC-1 and RouterBOARD-1
  - Example: eth0 (PC-1) → ether5 (RouterBOARD-1)

## What You Will Do
- Configure IP on RouterBOARD and PC
- Test connectivity using ping
- Connect to RouterBOARD using SSH

## Files in This Lab
- **configs.md** — Complete step-by-step configuration guide

## Notes
- SSH requires the RouterBOARD and PC to have valid IP addresses in the same subnet.
- SSH cannot be used until the router has an assigned IP on the interface being accessed.
- SSH operates on TCP port 22 by default and can be managed or reconfigured through `/ip service`.


Copyright © Christopher Aldrinovito 2025. All rights reserved.     |     Personal use only
Date: Dec 9 2025
