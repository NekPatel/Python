def count_lower_upper(string):
    lower = 0 
    upper = 0
    for i in string:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    output = { "lower" : lower, "upper" : upper }
    print(output)
    
string = input('enter a string')
count_lower_upper(string)
