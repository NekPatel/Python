string = input("enter a string")
upper_case = []
for char in string:
    if ("a" <= char <= "z"):    
        str = ord(char) - 32
        upper_case.append(chr(str))
    else:
        upper_case.append(char)
for i in upper_case:
    print(i, end = "")
