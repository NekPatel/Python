def creat_list(list_1,list_2):
    list_3 =[]
    for i in list_1:
        for j in list_2:
            if j == i:
              list_3.append(j)
    print(list_3)

string_1 = input("enter list 1")
string_2 = input("enter list 2")
list_1 = string_1.split() #to avoid space & to seprate words properly
list_2 = string_2.split()
creat_list(list_1,list_2)
