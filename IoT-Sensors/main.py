import pycom
import time

pycom.heartbeat(False)

print("Disco")
value = 0x000001

while True:
    pycom.rgbled(value)
    value = value << 1
    time.sleep_ms(5)
    print(value)
    if(value == 0x800000):
        value = 0x000001
