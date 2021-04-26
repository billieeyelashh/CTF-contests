from Crypto import *


hex_string = "0x70"[2:]
Bdytes = bytes.fromhex(hex_string)

flag= Bdytes.decode('Ascii')

print(flag)