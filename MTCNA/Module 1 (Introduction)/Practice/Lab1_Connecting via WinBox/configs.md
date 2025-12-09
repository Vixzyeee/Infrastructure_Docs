# RouterBOARD-1 Configuration

## Connect to `<RouterBOARD-1>` via MAC Address
- Connect to: `<MAC Address of RouterBOARD-1>`  
    - Example: `00:0C:42:FA:60:FC`
- Login: `<Username of RouterBOARD-1>`  
    - Example: `admin`
- Password: `<Password of RouterBOARD-1>`  
    - Example: (leave blank if default)

---

## Configure the IP Address on `<RouterBOARD-1 to PC-1>`

```bash
/ip address add address=<RouterBOARD-1 IP to PC-1> interface=<RouterBOARD-1 Interface to PC-1>
/ip address add address=192.168.88.1/24 interface=ether5

PC-1 Configuration
Configure the static IP Address on <PC-1>

IP address: <PC-1 IP to RouterBOARD-1>

Example: 192.168.88.2

Subnet mask: <PC-1 Subnet mask to RouterBOARD-1>

Example: 255.255.255.0

Default gateway:

Example: (leave blank — only required when accessing networks outside the local subnet)

DNS:

Example: (leave blank — only required when accessing networks outside the local subnet)

RouterBOARD-1 and PC-1 Testing
Ping <PC-1> from <RouterBOARD-1> Terminal
ping <IP Address of PC-1>
ping 192.168.88.2

Ping <RouterBOARD-1> from <PC-1> Terminal
ping <IP Address of RouterBOARD-1>
ping 192.168.88.1

Connect to <RouterBOARD-1> via IP Address

Connect to: <IP Address of RouterBOARD-1>

Example: 192.168.88.1

Login: <Username of RouterBOARD-1>

Example: admin

Password: <Password of RouterBOARD-1>

Example: (leave blank if default)
