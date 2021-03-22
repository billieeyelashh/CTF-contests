import pwn
from Crypto import *
from base64 import b64decode
from base64 import b64encode
import socket
import multiprocessing

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import sys
data = "Y+RdPb1Wtw1T99neojgAHi6jciFzJwjPW5L8MG2KWYi8tzsTE0ODplQAiXnOHrxQzO9r1pFlSih4Bnxq8mvX5XPfoq+G7tJWoQAYp5h1kGNGwxz2GhR6zixYI9XTTCX+I2xjOBgeakGJkBVzLdlJck7370nIJs0aZdgr4w2dYa2hjKKuoJSgJLI7Omo8MMdHVehbxaSr6KP7RHN3VfL1xVKOWNwuvapF8OP5+7tb1q7sbVP/rXdSElztr/tmM6WG"

def decrypt(self, data):
    raw = b64decode(data)
    self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    flag = decrypt()