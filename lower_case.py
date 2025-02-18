string = input("enter a string")
lower_case = []
for char in string:
    if ("A" <= char <= "Z"):    
        str = ord(char) + 32
        lower_case.append(chr(str))
    else:
        lower_case.append(char)
for i in lower_case:
    print(i, end = "")
