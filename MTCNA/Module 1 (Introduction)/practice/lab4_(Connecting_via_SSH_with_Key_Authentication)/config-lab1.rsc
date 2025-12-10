# jan/02/1970 02:24:11 by RouterOS 6.49.13
# software id = <redacted>
#
# model = 951-2n
# serial number = <redacted>
/interface wireless
set [ find default-name=wlan1 ] ssid=MikroTik
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip address
add address=192.168.88.1/24 interface=ether5 network=192.168.88.0
