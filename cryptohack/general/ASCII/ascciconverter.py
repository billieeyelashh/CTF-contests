# Convert following ascii ints to string 
asciiStringList = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]


# Convert it 
# Chr converts ascci into string values
ans = ''.join(chr(i) for i in asciiStringList)
    
print(ans)



