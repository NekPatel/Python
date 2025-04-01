food_item = [('pani-puri', 30), ('cheese butter masala', 150), ('momos', 100), ('dabeli', 25), ('vadapav', 25)]
sorted_food = sorted(food_item, key = lambda x: x[1], reverse= True)
for item, price in sorted_food:
    print(f"{item}: Rs.{price}")
