import pycom
import time

pycom.heartbeat(False)

print("Hello World")

while True:
    pycom.rgbled(0xFF0000)
    time.sleep_ms(500)

    pycom.rgbled(0x00FF00)
    time.sleep_ms(500)

    pycom.rgbled(0x0000FF)
    time.sleep_ms(500)
