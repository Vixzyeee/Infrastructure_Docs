```bash
## SSH with Key Authentication

SSH key authentication uses a **public/private key pair** instead of a password.  
The goal is simple: stronger security, faster logins, and compatibility with automation.

The private key stays on the client.  
The public key is placed on the device.  
If they match, access is granted without typing a password.

## Public Key vs Private Key

A **public key** is the part you are allowed to share.  
It is stored on the device you want to access. Anyone can see it; it does not compromise security.

A **private key** is the part you never share.  
It stays on the client machine and is used to prove your identity.  
If someone gets your private key, they can impersonate you.

In short:  
- Public key = “Lock” placed on the device  
- Private key = “Key” you keep locally  
- SSH authenticates you by verifying that your private key matches the public key stored on the server

## Key File Formats

When generating SSH keys, two files are created:

**Public Key (`.pub`)**  
- Always ends with `.pub`.  
- This is the key you upload to the device.  
- Safe to share.  
- Examples: `id_ed25519.pub`, `id_rsa.pub`

**Private Key (no extension)**  
- Has no `.pub` extension.  
- Stays on the client and must never be shared.  
- Used by the SSH client to prove your identity.  
- Examples: `id_ed25519`, `id_rsa`

The router must have the **public key**, and the client must keep the **private key**.  
Authentication only succeeds when both match.

## Why Use SSH Keys?

- Passwords can be guessed; 2048/4096-bit keys realistically cannot.  
- Bruteforce attempts become far less effective.  
- Perfect for automation (scripts, Ansible, CI/CD).  
- No need to remember or manually type passwords.

## Requirements

- The device must already have an IP address and SSH enabled (same as regular SSH).  
- The client must have an RSA or ED25519 keypair.  
- The public key must be installed on the device.

## How It Works (Short Version)

1. The client identifies itself using its public key.  
2. The server checks whether the key is authorized.  
3. The server sends an encrypted challenge.  
4. The client decrypts it using the **private key**.  
5. If the response matches, the server grants access.
