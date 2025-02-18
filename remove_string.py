string = input("enter a string")
remove_string = input("enter the string to be removed")
index = string.find(remove_string)
#slicing from start to index of removed string
print(string[0:index], end = "")
#slicing from the end of remove string
print(string[index + len(remove_string): len(string)])
