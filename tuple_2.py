student = [(188,'nek', 19), (175,'vraj',17), (173,'ved',18)]
rollno = []
name = []
age = []
for i in range(0,3):
    rollno.append(student[i][0])
    name.append(student[i][1])
    age.append(student[i][2])

print('roll number:', rollno)
print('name:', name)
print('age:', age)
