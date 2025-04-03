import random
random_dig ={random.randint(15,45) for _ in range (10)}
print("random set:",random_dig)

count_less30 = len([num for num in random_dig if num < 30])
print(f"number which are less than 30 are:{count_less30}")

remove_greater35 =[num for num in random_dig if num >= 35]
for num in remove_greater35:
    random_dig.remove(num)
print("your set less than 35 is:",random_dig)

