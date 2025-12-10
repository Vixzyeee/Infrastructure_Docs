```bash
# PC-1 Configuration

## Configure the static IP Address on <PC-1>

- IP address: <PC-1 IP to RouterBOARD-1>
    - Example: 192.168.88.2
- Subnet mask: <PC-1 Subnet mask to RouterBOARD-1>
    - Example: 255.255.255.0
- Default gateway:
    - Example: (leave blank — only required when accessing networks outside the local subnet)
- DNS:
    - Example: (leave blank — only required when accessing networks outside the local subnet)

## Configure the Key Authentication on <PC-1>

ssh-keygen -t <SSH Key Types> -C <Comment of Key Authentication>
ssh-keygen -t ed25519 -C "vixzye-ops@DevOps"

or

ssh-keygen -t <SSH Key Types> -b <RSA Key Size> -C <Comment of Key Authentication>
ssh-keygen -t rsa -b 4096 -C "vixzye-ops@DevOps"

## Send the .pub Key Authentication on <PC-1> to <RouterBOARD-1>

scp <Source .pub Key Authentication File> <Username of RouterBOARD-1>@<IP Address of RouterBOARD-1>:<Location of RouterBOARD-1>
scp /home/vixzye-ops/.ssh/id_rsa.pub admin@192.168.88.1:/

## Connect to <RouterBOARD-1> via MAC Address

- Connect to: <MAC Address of RouterBOARD-1>
    - Example: 00:0C:42:FA:60:FC
- Login: <Username of RouterBOARD-1>
    - Example: admin
- Password: <Password of RouterBOARD-1>
    - Example: (leave blank if default)


# RouterBOARD-1 Configuration

## Configure the IP Address on <RouterBOARD-1 to PC-1>

/ip address add address=<RouterBOARD-1 IP to PC-1> interface=<RouterBOARD-1 Interface to PC-1>
/ip address add address=192.168.88.1/24 interface=ether5

## Import the .pub Key Authentication File on <RouterBOARD-1>

/user ssh-keys import user=<Username of RouterBOARD-1> public-key-file=<Public Key File on RouterBOARD-1>
/user ssh-keys import user=admin public-key-file=id_rsa.pub 

# RouterBOARD-1 and PC-1 Testing

## Ping <PC-1> from <RouterBOARD-1> Terminal

ping <IP Address of PC-1>
ping 192.168.88.2

## Ping <RouterBOARD-1> from <PC-1> Terminal

ping <IP Address of RouterBOARD-1>
ping 192.168.88.1


# Lab Testing

## Connect to <RouterBOARD-1> via SSH

ssh <Username of RouterBOARD-1>@<IP Address of RouterBOARD-1>
ssh admin@192.168.88.1

or

ssh -p <Default Port of SSH> <Username of RouterBOARD-1>@<IP Address of RouterBOARD-1>
ssh -p 22 admin@192.168.88.1
