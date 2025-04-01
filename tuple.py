name = [('nek',), ('yashvardhan',), 'radha', ('parva',), 'sita']
boy_count = 0
girl_count = 0
for i in name:
    if isinstance(i,tuple):
        boy_count += 1
    else:
        girl_count += 1
print(f"number of boys: {boy_count}")
print(f"number of girls: {girl_count}")
