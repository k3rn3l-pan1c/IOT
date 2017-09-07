from network import WLAN
import socket
import machine
import time

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()

for net in nets:
    if net.ssid == 'BEST-IoT-Gateway':
        print('Connecting to Wifi...')

        while True:
            wlan.connect(net.ssid, auth=(net.sec, "BEST-password"), timeout=5000)
            connected = wlan.isconnected()
            if connected:
                print('Connected!')
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                s.settimeout(1.0)
                s.sendto('Party in room', socket.getaddrinfo('192.168.4.1', 5555)[0][-1])

                message = ('    | $$  | $$', '    | $$  | $$', '    | $$  | $$', '    | $$$$$$$$', '    |_____  $$','           | $$','          | $$', '          |__/')
                for idx in range(len(message)):
                    print(idx)
                    x = message[idx]
                    s.sendto(x, socket.getaddrinfo('192.168.4.1', 5555)[0][-1])
                break
            if connected:
                break
