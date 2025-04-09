def convert(string):
    spliting = string.split()
    remove_duplicate = list(set(spliting))
    sorting = sorted(remove_duplicate)
    joining = " ".join(sorting)
    print(joining)
string = input("enter a string")
convert(string)
