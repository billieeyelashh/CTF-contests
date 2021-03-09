# Add up and int and and string with xor reveals flag 



int_0 = 13
string_0 = "label"

flag= ''

for c in string_0:
    flag += chr(ord(c) ^ int_0) #ord gets unicode character and goes through the string. Every Character is xored with the integer 13


print('crypto{{{}}}'.format(flag))







