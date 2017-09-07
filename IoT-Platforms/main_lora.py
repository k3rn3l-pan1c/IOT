from network import LoRa
import binascii
import pycom
import socket
import time
import config

# create OTA authentication params
dev_eui = binascii.unhexlify(config.DEV_EUI)
app_eui = binascii.unhexlify(config.APP_EUI)
app_key = binascii.unhexlify(config.APP_KEY)

# disable heartbeat so we can use the LED for feedback
pycom.heartbeat(False)

# turn LED on with red color while not joined
pycom.rgbled(0xff0000)

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
	time.sleep(2.5)
print('Successfuly joined!')

# change LED to green
pycom.rgbled(0x00ff00)

# create a LoRa socket
sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
sock.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
sock.setblocking(False)

time.sleep(1.0)

# change LED to blue
pycom.rgbled(0x0000ff)

for i in range (200):
	# send bytes
	sock.send(b'PKT #' + bytes([i]))

	# Wait some time before trying to receive data
	time.sleep(4)

	# Print data if it is available
	rx = sock.recv(256)
	if rx:
		print(rx)
	time.sleep(6)