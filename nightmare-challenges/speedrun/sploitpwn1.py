from pwn import *

target = process('./pwn1')

target.sendline("Sir Lancelot of Camelot")
target.sendline('To seek the Holy Grail')


