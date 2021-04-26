from pwn import *
from Crypto import *

host, port = "mercury.picoctf.net" ,35652

r=remote(host,port, level= 'debug')


lines = r.recvlines() + "\n"



flag = "".join(chr(line) for line in lines)


print(flag)