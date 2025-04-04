dict_price = {
    'wheat':450,
    'rice' : 300,
    'dal' : 250
    }
dict_quantity = {
    'wheat' : 10,
    'rice' : 8,
    'dal' : 10
    }
sum = 0
for v in dict_price:
    if v in dict_quantity:
        sum = (dict_quantity[v]*dict_price[v]) + sum
print("total sum is:", sum)
