string1 = input("enter string 1")
string2 = input("enter string 2")
if (string1.count(string2) == True):
    print("string2 is there in string1")
elif(string2.count(string1) == True):
    print("string1 is there in string2")
else:
    print("any string doesn't exist in other")
    
