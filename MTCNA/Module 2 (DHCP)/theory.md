# Module 2: DHCP (Dynamic Host Configuration Protocol)

## What is DHCP?

DHCP is a Layer 3 protocol used to automatically assign IP configuration to devices on a network.
It eliminates the need for manual IP settings and ensures consistent, conflict-free addressing.

A DHCP-enabled network assigns:
- IP address
- Subnet mask
- Default gateway
- DNS servers
- Lease duration


## Why DHCP Exists

Manual IP configuration does not scale.  
DHCP provides:

- Automated IP address assignment  
- Prevention of duplicate IP addresses  
- Faster onboarding for clients  
- Centralized management of addressing  
- Support for both small and large networks  


## How DHCP Works (DORA)

DHCP uses a four-step process known as **DORA**:

1. **Discover**  
   The client broadcasts a request asking for available DHCP servers.

2. **Offer**  
   A DHCP server responds with an available IP address and configuration options.

3. **Request**  
   The client requests to use the offered IP.

4. **Acknowledge**  
   The server confirms and assigns the IP to the client.

This process creates a temporary contract called a **lease**.


## DHCP Components

### DHCP Server
- Provides and manages IP addresses from an IP pool
- Supplies gateway, DNS, and lease time
- Runs on routers, servers, or virtualization systems

### DHCP Client
- Requests and receives configuration automatically
- Used by PCs, phones, printers, routers, access points

### DHCP Relay (IP Helper)
- Forwards DHCP requests across Layer 3 boundaries
- Allows a central DHCP server to serve multiple subnets


## Key Concepts

### IP Pool
A range of IP addresses used by the DHCP server to assign to clients.

### Lease Time
The duration for which an IP address is valid.  
Clients must renew the lease before expiration.

### Reservation (Static Lease)
A fixed IP assignment based on MAC address.  
Useful for servers, printers, or devices needing consistent addressing.

### Options (DHCP Options)
Additional configuration provided by the server:  
- Option 3: Default Gateway  
- Option 6: DNS server  
- Option 15: Domain name  
- Option 42: NTP server  
- Option 66/67: PXE boot (for provisioning environments)


## DHCP in MikroTik RouterOS

- DHCP Server is configured under `/ip dhcp-server`
- IP pools are created under `/ip pool`
- DHCP leases are visible under `/ip dhcp-server lease`
- Relay is configured under `/ip dhcp-relay`
- RouterOS supports dynamic and static leases
- Default configuration on MikroTik includes an enabled DHCP server on `bridge` or `ether2`

Core commands:
- `/ip pool add`
- `/ip dhcp-server add`
- `/ip dhcp-server network add`
- `/ip dhcp-server lease add`
- `/ip dhcp-relay add`


## Security Considerations

- DHCP is not encrypted and is vulnerable to spoofing  
- Rogue DHCP servers can mislead clients  
- Use switch port isolation or DHCP Snooping (if supported by the switch)  
- Static reservations reduce unpredictable addressing  
- Avoid bridging large networks without proper segmentation


## Practical Use Cases

- Home networks: automatic assignment for all client devices  
- Small businesses: centralized addressing via router  
- Large networks: dedicated DHCP servers with relays across subnets  
- IoT environments: static leases for non-interactive devices  
- ISP networks: provisioning CPE devices via DHCP options  


## Course Context

In this module, you will:
- Understand DHCP theory and process  
- Configure DHCP server and pool on RouterOS  
- Observe dynamic and static leases  
- Test automatic address assignment  
- Work with DHCP relay in routed networks  

This knowledge prepares you for building scalable Layer 3 networks using MikroTik.
