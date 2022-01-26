a1 = [1,2,3,4,5,6,7,8,9,10]
print(a1)
a2 =[]
for i in a1:
    if i %2 != 0:
        a2.append(i**2)
print(a2)

a3 = [i**2 for i in a1 if i %2 != 0]
print(a3)

student = {'ala':10,'maryam':8,'zahra':11}
student_names = [x.upper() for x in student.keys()]
print(student_names)

a4 = [v**2 for v in student.values()]
print(a4)

for k,v in student.items():
    print(k,v)

a5 = [(k.capitalize(),v*2) for k,v in student.items()]
print(a5)


a6 = {k.capitalize():v*2 for k,v in student.items()}
print(a6)
print(type(a6))