def compute(n):
    total = 0
    for i in range (1,5):
        num = int(str(n)*i)
        total += num
    print(total)
    
n = int(input('input a number'))
compute(n)
