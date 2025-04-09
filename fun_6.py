def value(start, end):
    list_tuple= []
    list_final = []
    for i in range(start,end+1):
        list_tuple.append(i)
        list_tuple.append(i**2)
        list_tuple.append(i**3)
        tuple_final = tuple(list_tuple)
        list_tuple.clear()
        list_final.append(tuple_final)
        tuple_final = ()
    print(list_final)
start = int(input("enter starting value"))
end = int(input("enter ending value"))
value(start,end)
