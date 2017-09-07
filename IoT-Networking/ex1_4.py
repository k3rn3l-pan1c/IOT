from network import WLAN
import socket
import machine
import time

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()

for net in nets:
    if net.ssid == 'BEST-IoT-Gateway':
        print('Connecting to Wifi...')

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.settimeout(1.0)

        while True:
            message = input("Enter your message: ")
            s.sendto(message, socket.getaddrinfo('192.169.4.1', 5555)[0][-1])
            try:
                msg = s.recv(1500)
                print(msg)
            except Exception as ex:
                print(ex)
