# Solving and Notes of Arithmetic 2
import math

p = 17

print(3^17 % p) # =3
print(5^17 % p) # = 5

print(7^16 % p) # = 23 -> 7 + 16

##
x = 65537


# Since p is a prime p = 65537

print(273246787654^65536 % 65537)

# Bei Primzaheln a^(p-1) = 1 % p

# pow takes pow(x,y,z) x =base y = exponent z = modulus
'''
Looking at Fermat's little theorem...
if p is prime, for every integer a:
        pow(a, p) = a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p
So lets check
        pow(273246787654, 65536) mod 65537
Notice that 65536 is exactly 65537-1,
If 273246787654 and 65537 are coprime,
        then the result is one
'''
from math import gcd

a = 273246787654
p = 65537

if gcd(a,p)==1: #a and p are coprime
        print(1)