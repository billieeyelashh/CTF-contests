# Solve Extended Euclidian Algorithm
# The extended Euclidean algorithm is an efficient way to find integers u,v such that

# a * u + b * v = gcd(a,b)

# Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.


# Using the two primes p = 26513, q = 32321, find the integers u,v such that

# p * u + q * v = gcd(p,q)

# Knowing that p,q are prime, what would you expect gcd(p,q) to be?
# Must  be 1 since these two are primes

import math

def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

print("\n[*] FLAG: crypto{{{},{}}}".format(u,v))
