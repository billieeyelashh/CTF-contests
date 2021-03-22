p = 29
ints = [14,6,11]
print(x for x in range(p) if pow(x,2,p) in ints)



qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")