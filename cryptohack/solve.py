from pwn    import *

# connect to remote machine 
r = remote('socket.cryptohack.org', 13381)


r.recvline()
# fake signature
r.sendline('A'*0x20)

