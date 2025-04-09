def palindrome(str):
    str_1 = str.replace(" ","") #it will remove all space from string
    count = 0
    i = 0
    while(i<= len(str_1)-1):
        if (str_1[i] == str_1[len(str_1)-i-1]):
            count += 1
        i += 1
    if(count == len(str_1)):
        print("it is palindrome")
    else:
        print("it is not a palindrome")
str = input("enter a string")
palindrome(str)
