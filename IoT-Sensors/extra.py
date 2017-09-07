import time
import pycom

from machine import Pin, ADC
from onewire import DS18X20
from onewire import OneWire

pycom.heartbeat(False)
adc = ADC(0)
potentiometer = adc.channel(pin='P17')

print("Hello World")
while(True):
    value = int(potentiometer.value() / 1023 * (2 ** 24))
    pycom.rgbled(value)
