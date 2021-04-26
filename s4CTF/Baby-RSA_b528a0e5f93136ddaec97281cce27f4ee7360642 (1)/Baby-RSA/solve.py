from Crypto import *
n = 48564396752059338791464352725210493148212425902751190745668164451763507023284970474595680869078726765719920168392505794415687815488076204724659643390252172928332322944711949999326843460702414647825442748821062427474599006915155109396213406624079900714394311217571510958430682853948004734434233860146109894977
c = 28767981118696173499362412795754123415661648348744243377735885542432968964926551295510845917978847771440173910696607195964650864733310997503291576565605508828208679238871651079005335403223194484223700571589836641593207297310906538525042640141507638449129445170765859354237239005410738965923592173867475751585
e = 31337
#p =
#q =
# nbit =256
# P = Q = 
# Factor 
# 1. Need to find p and q
# Then tot = (p-1) * (q-1)
# d modinv(31337, tot) 


# Find private key d  Need to retrieve phi
# then pow(c, d,n ) = flag 


tot = (p-1) * (q-1)

d = modinv(e,tot)


flag = pow(c,d n)

# Maybe and long to bytes is needed
#long_to_bytes(flag)

print(flag)