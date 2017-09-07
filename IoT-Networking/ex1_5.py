from network import WLAN
import socket
import machine
import time

wlan = WLAN(mode=WLAN.AP, ssid='Party_Room_4', auth=(WLAN.WPA2, 'password'), channel=3)

print('Wifi setup completed')
