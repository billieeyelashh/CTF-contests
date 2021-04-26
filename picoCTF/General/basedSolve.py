binary_string ="01101100 01100001 01101101 01110000"
binary_values = binary_string.split()

ascii_string =""

for binary_value in binary_values:
    an_integer = int(binary_value,2)
    ascii_character = chr(an_integer)
    ascii_string += ascii_character

print(ascii_string)


def octal_to_str(octal_str):

    str_converted = ""
    for octal_char in octal_str.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted



print(octal_to_str("160 145 141 162"))


hex_string= "6c69676874"
flag= bytearray.fromhex(hex_string).decode()

print(flag)