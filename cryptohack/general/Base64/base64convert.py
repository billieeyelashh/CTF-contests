import pybase64
encodedHexString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"


# Decode into bytes
hexstringByteDecoded = bytes.fromhex(encodedHexString)

# Encode it into Base64
print(pybase64.b64encode(hexstringByteDecoded))

