import uos

__author__ = __maintainer__ = "Helder Moreira"
__email__ = "helderm14@ua.pt"
__version__ = "1.0.0"

def random(minv=0, maxv=1):
    return (uos.urandom(1)[0]/255)*(maxv-minv) + minv

def randint(minv=0, maxv=1):
    return int(random(minv,maxv))

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return result

def rgb2hex(*values):
    h = "#"
    if len(values) != 3:
        return None
    for v in values:
        tmp = hex(v)[2:]
        h+=  tmp if len(tmp) == 2 else "0"+tmp
    return h
