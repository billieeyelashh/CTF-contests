import base64



string1 = open("boxres/b64.txt","r+").read()

#string =''



for i in range(0,50):
    string1=base64.b64decode(string1)



print(string1)


#string1.close()

