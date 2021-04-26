from Crypto import *

f = open('flag.enc', 'rb')
s = f.read()


print(len(s))

for i in range(256):
    flag = bytes([i])
    for x in range(42):
        flag += bytes([flag[-1] ^ s[x]])
    
    print(flag)
