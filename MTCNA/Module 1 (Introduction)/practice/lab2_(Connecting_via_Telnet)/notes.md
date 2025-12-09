```bash
## What is Telnet?

Telnet is a legacy remote-access protocol that provides command-line access to network devices over a TCP connection.  
It operates entirely in plaintext and offers no encryption, authentication hardening, or data integrity protection.  
Because of these limitations, Telnet is considered insecure and is used today only for lab environments, testing, or accessing older devices that do not support SSH.
Telnet operates strictly at Layer 3 and requires the device to have an assigned IP address before a connection can be established.

## Understanding Connection Methods

**Telnet Login**  
Telnet provides remote CLI access over TCP but transmits everything in plaintext, including usernames and passwords.  
It does not offer encryption, session integrity, or modern authentication mechanisms, which makes it unsuitable for any real network environment.  
Telnet is used mainly for training, troubleshooting older hardware, or demonstrating the security gap between unsecured access (Telnet) and secured access (SSH).
