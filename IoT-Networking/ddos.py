from network import LoRa
import socket
import time
#from network import WLAN

lora = LoRa(mode=LoRa.LORA, frequency=868000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

#wlan = WLAN(mode=WLAN.STA)

#nets = wlan.scan()
#for net in nets:
#    if net.ssid == 'BEST-IoT-Gateway':
#        print('Connecting to Wifi...')
#        wlan.connect(net.ssid, auth=(net.sec, "BEST-password"), timeout=5000)
#        print('Connected!')
#        break

#ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#ss.settimeout(1.0)
while True:
    s.send("                                      .,;;;;;;;,.")
    s.send("                                 ,;;;;;;;,/;;;;")
    s.send("                .,aa###########@a;;;;;/;;;,//;;;")
    s.send("       ..,,,.,aa##################@a;//;;;,//;;;")
    s.send("   ,;;;;;;;O#####OO##############OOO###a,/;;;;'")
    s.send(" .;;//,;;;O####OOO##########OOO####OOO#####a'")
    s.send(" .;;/,;;/;OO##OO#######################OOO####.")
    s.send(" ;;;/,;;//OO#######OOO###########OOO###########.")
    s.send(" `;;//,;,OOO#########OO#########OO##############.")
    s.send(" ;.  ``````OOO#####;;;;;;OO#####OO;;;;;;######O####.")
    s.send(" .;;,       OOO###O;; ~`;##OOOOO##; ~`;;O#####OO###")
    s.send(" ;;;;    ,  OOO##O;;;,.,;O#########O;,.,;;;O####OO###,")
    s.send(" `;;'   ,;; OOO##OO;;;;OOO(???????)OOO;;;;OO####OO###%,")
    s.send(" `\   ;;; `OOO#####OOOO##\?????/##OOOO#######O####%O@a")
    s.send(" \,`;'  `OOO####OOO######;######OOO###########%O###,")
    s.send(" .,\      `OO####OO"#####;#####"OO##########%oO###O#;")
    s.send(" ,;;;; \   .::::OO##OOOaaa###aaaOOO#######',;OO##OOO##;,")
    s.send(" .;;''    \:::.OOaa`###OO#######OO###'::aOO.:;;OO###OO;::.")
    s.send(" '       .::\.OO####O#::;;;;;;;;;;;;::O#O@OO.::::::::://::")
    s.send(" .:::.O\########O#O::;;;::O#OO#O###@OO.:;;;;;;;;//:,")
    s.send(" .:/;:.OO#\#########OO#OO#OO########@OO.:;;;;;;;;;//:")
    s.send(" .://;;.OO###\##########O#############@OO.:;;;;;;;;//:.")
    s.send(" ;//;;;;.O'//;;;;;;\##################@OO.:;;;;;;;;//:..")
    s.send(" ;//:;;;;:.//;;;;;;;;;#################@OO.:;;;;;;;;;//..")
    s.send(" ;;//:;;;:://;;;;;;;;;################@OO.:/;;;;;;;;;//..")
    s.send(" `;;;;;:::::::ooOOOoo#\############@OOO.;;//;;;;;;;;;//.o,")
    s.send(" .;,,,.OOOOO############\#######@OOO.;;;//;;;;;;;;;;//;.OO,")
    s.send(" //;;.oO##################@\OOO.;;;;;;;;;;;;;;;;;;;;//;.oO#O,")
    s.send(" //;;;;O##############@OOO=;;;;//;;;;;;;;;;;;;;;;;;;//;.oO##Oo")
    s.send(" //::;;O#########@OOOOO=;;;;;;;//;;;;;;;;;;;;;;;////;.oO####OO")
    s.send(" .n.n.n.n`;O########@OOOOO=;;;;;;;;;;///;;;;////////';oO########OO")


    time.sleep_ms(5000)

magic = '*'
aux = True
print('Starting')
while True:
    s.send(magic)
#    try:
        #if wlan.isconnected == 0:
        #    wlan.connect(net.ssid, auth=(net.sec, "BEST-password"), timeout=5000)
        #ss.sendto(magic, socket.getaddrinfo('192.169.4.1', 5555)[0][-1])
    #except Exception as ex:
    #    pass

    if aux:
        magic = magic + "*"
    else:
        magic = magic[:len(magic)-1]

    if len(magic) == 55:
        s.send("               We are where. We are Anonymous")
        aux = False
    elif len(magic) == 0:
        aux = True
