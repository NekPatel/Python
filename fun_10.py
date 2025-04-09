def frequency(string):
    remove_space = string.replace(" ","")
    convert_list = list(remove_space)
    convert_set = list(set(remove_space))
    sorting = sorted(convert_set)
    for i in sorting:
        count = convert_list.count(i)
        print(f"{i}:{count}")
        
string = input("input string")
frequency(string)
