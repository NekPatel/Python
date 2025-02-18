chem = int(input("enter a chemistry marks"))
phy = int(input("enter a phy marks"))
bio = int(input("enter a biology marks"))

marks = (chem + phy + bio) / 3

if(chem > 100 or phy > 100 or bio > 100):
    print("incorrect input of marks")
elif(marks >= 80):
    print("Distinction")
elif(marks > 60):
    print("First Division")
elif(marks > 45):
    print("second division")
elif(marks > 40):
    print("pass")
elif(marks < 40 < 0):
    print("Fail")
else:
    print("enter correct marks")
print("Your average marks is:", marks)
