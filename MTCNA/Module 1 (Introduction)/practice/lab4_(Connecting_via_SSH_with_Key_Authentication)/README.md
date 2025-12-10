```bash
# Lab 4: Connecting to MikroTik via SSH with Key Authentication

## Objective
Learn how to connect to a MikroTik RouterBOARD using:
1. SSH keys instead of passwords

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
- Connect to RouterBOARD using MAC Address
- Configure IP on RouterBOARD and PC
- Test connectivity using ping
- Generate SSH key pairs on the client
- Install the public key on MikroTik
- Disable password authentication (optional hardening)
- Log into the router using the private key
- Verify SSH key functionality

## Files in This Lab
- **configs.md** — Commands for key generation, key installation, and RouterOS configuration 

## Notes
- This lab assumes you already understand basic SSH concepts from the previous lab.
- IP addressing requirements are identical: SSH still needs L3 connectivity. 
- Only the authentication method changes, not the connection process.  
- SSH with keys is strongly recommended for production use.


Copyright © Christopher Aldrinovito 2025. All rights reserved.     |     Personal use only
Date: Dec 9 2025
