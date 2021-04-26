from pwn import *
from Crypto import *

with open('flag.enc')  as handle:

    cipher = handle.read()
    print(cipher)

