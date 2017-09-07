from machine import Pin
from onewire import DS18X20
from onewire import OneWire
import time

ow = OneWire(Pin('P9'))
temp = DS18X20(ow)
print("Hello World")
while(True):
    temp.start_convertion()
    time.sleep_ms(750)

    print(temp.read_temp_async())
