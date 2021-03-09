from pwn import * # pip install pwntools
import json
from Crypto import *
import pybase64

r = remote('socket.cryptohack.org', 13377, level = 'debug')

#Decode diffrent types
# base64 is clear 
def decodebase64():
    encodedString = pybase64.b64decode(receivedString)
    return encodedString

def decodehex():

def decodehex():
    encodedString = 


#JSON Operations
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#Check enconding Type and decode it 



received = json_recv()

receivedString = received["encoded"]
#decode received 
print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])


#1. Get type of encoding 


#2. Decode it with the type asked 


#3. send ready json to server 



to_send = {
    "decoded": "changeme"
}





# send encrypted 
#json_send(to_send)

json_recv()
