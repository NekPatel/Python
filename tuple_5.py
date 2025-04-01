tuple_list = [(), ('apple',50), (),('banana',30)]
filtered_list = []
for i in tuple_list:
    if i != ():
        filtered_list.append(i)
print('list if tuple after removing empty tuple is:',filtered_list)
