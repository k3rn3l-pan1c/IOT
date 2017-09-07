from network import WLAN
import socket
import machine
import time

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    print(net.ssid)
