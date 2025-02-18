string = input("enter a string")
upper_case = []
for char in string:
    if ("a" <= char <= "z"):    
        str = ord(char) - 32
        upper_case.append(chr(str))
    elif ("A" <= char <= "Z"):
        str2 = ord(char) + 32
        upper_case.append(chr(str2))
for i in upper_case:
    print(i, end = "")