from network import LoRa
import socket
import time
lora = LoRa(mode=LoRa.LORA, frequency=868000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setblocking(True)

s.send('Party in room')

message = ('    | $$  | $$', '    | $$  | $$', '    | $$  | $$', '    | $$$$$$$$', '    |_____  $$','           | $$','          | $$', '          |__/')
for idx in range(len(message)):
    s.send(message[idx])
    time.sleep_ms(900)

magic = '*'
aux = True

while True:
    s.send(magic)
    if aux:
        magic = magic + "*"
    else:
        magic = magic[:len(magic)-1]

    if len(magic) == 40:
        aux = False
    elif len(magic) == 0:
        aux = True
