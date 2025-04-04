string = input("enter a string")
dictionary = {}
for i in string:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)
