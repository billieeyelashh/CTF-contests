from pwn import xor

# Given encoded xor string with a single byte
bytes_array = ['A', 'B', 'C','D','0','1']

favourite_string = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
print("Decoded Hex: " + str(favourite_string))

# xoring with all 1 byte == means it's from
# for loop that

for byt in bytes_array:
    flag = xor(byt, favourite_string)
    print("[*] " + str(flag) + "\n")



