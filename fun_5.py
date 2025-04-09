def ispangram(string):
    set_str = set(string)
    abc = set('abcdefghijklmnopqrstuvwxyz')
    if (set_str >= abc):
        print('it is pangram')
    else:
        print('it is not pangram')
string = input("enter a string")
ispangram(string)
