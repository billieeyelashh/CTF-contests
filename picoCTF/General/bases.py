import base64
mysterious_string = "bDNhcm5fdGgzX3IwcDM1"


flag = base64.b64decode(mysterious_string)
print(flag)