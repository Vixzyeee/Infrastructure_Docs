```bash
## SSH with Key Authentication

SSH key authentication uses a **public/private key pair** instead of a password.  
The goal is simple: stronger security, faster logins, and compatibility with automation.

The private key stays on the client.  
The public key is placed on the device.  
If they match, access is granted without typing a password.

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
