def count_alpha_digits(string):
    alpha = 0
    digit = 0
    for i in string:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1

    dict = {
        'alphabets' : alpha, 'digits' : digit}
    print(dict)
string = input("enter a string: ")
count_alpha_digits(string)
