department = {
    1 : [(188, 50000), (186,30000),(187,20000)],
    2 : [(173, 60000), (175, 45000), (178,35000)],
    3 : [(184, 45000), (191,50000), (192,20000)]
    }

for i in department:
    employee_data = department[i] #it will give you  values
    salary = []
    for j in employee_data:
        salary += [j[1]]#it will give you only salaries
    max_salary = max(salary)
    min_salary = min(salary)
    print(f"department {i}: max salary is {max_salary}, min salary is {min_salary}")
