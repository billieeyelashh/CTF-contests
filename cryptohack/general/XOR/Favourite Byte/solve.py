from pwn import xor
import binascii
# Given encoded xor string with a single byte
bytes_array = ['A', 'B', 'C','D','0','1']

favourite_string = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print("Decoded Hex: " + str(favourite_string))

# xoring with all 1 byte == means it's from
# for loop that

for byt in bytes_array:
    flag = xor(byt, favourite_string)
    print("[*] " + (flag.decode("utf-8")) + "\n")



# More cleaner way by boge
byte= 0x00

for i in range(256):
    flag=xor(favourite_string, byte).decode("utf-8")
    if("crypto" in flag):
        print(flag)
        break;
    byte=byte + 0x01