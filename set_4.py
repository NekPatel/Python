name = {'aryan','abhishek','bhavesh','brijesh'}
name_a = set()
name_b =  set()

for i in name:
    if(i.startswith('a')):
        name_a.add(i)
    else:
        name_b.add(i)
print("name starts with a are:", name_a)
print(f"name starts with b are: {name_b}")
