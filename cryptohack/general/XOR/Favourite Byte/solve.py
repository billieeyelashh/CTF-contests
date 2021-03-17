from pwn import xor
import binascii
# Given encoded xor string with a single byte
bytes_array = ['A', 'B', 'C','D','0','1']

favourite_string = binascii.unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print("Decoded Hex: " + str(favourite_string))

# xoring with all 1 byte == means it's from
# for loop that

for byt in bytes_array:
    flag = xor(byt, favourite_string)
    print("[*] " + (flag.decode("utf-8")) + "\n")



# More cleaner way by boge
byte= 0x00

for i in range(256):
    flag1=xor(favourite_string, byte).decode("utf-8")
    if("crypto" in flag1):
        print(flag1)
        break;
    byte=byte + 0x01