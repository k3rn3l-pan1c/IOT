from network import WLAN
import socket
import machine
import time

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'BEST-IoT-Gateway':
        print('Connecting to Wifi...')
        wlan.connect(net.ssid, auth=(net.sec, "BEST-password"), timeout=5000)
        print('Connected!')
        break
