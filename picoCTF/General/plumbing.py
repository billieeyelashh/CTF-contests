from pwn import *

host, port = "jupiter.challenges.picoctf.org" 14291

s = remote(host,port, level='debug')


f = open("output.txt", "rb")


# Dont needed 
# just grep
# $ nc jupiter.challenges.picoctf.org 14291 | grep picoCTF