from Crypto.PublicKey import RSA

privacyMail = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')

private_key = RSA.importKey(privacyMail.read())

print(private_key.d) # d ist the flag for the public exponent

# Take a look at these website for more information. they were very helpful during the solving process

# 1. https://tls.mbed.org/kb/cryptography/asn1-key-structures-in-der-and-pem
# 2. https://coolaj86.com/articles/asn1-for-dummies/d
