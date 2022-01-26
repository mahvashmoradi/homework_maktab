def get_data(number):
    list_student = []
    for i in range(number):
        student = input('enter name, age, height, weight of student:').split(',')
        student = [float(x.strip()) if x.isdigit() else x for x in student]
        print(student)
        #student = [float(x) if x.isdigit() else x for x in student]
        """ name=input('name: ')
        weight=float(input('weight: '))
        age=int(input('age: '))
        height=float(input('height: '))"""
        member = Student(*student)
        #member = Student(name, weight, age, height)
        list_student.append(member)
    return list_student


class Student:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} is {self.age} years old"


def calculate_mean(lst):
    '''_sum=0
    add=[x.age for x in lst]
    _sum(add)
    print(_sum)
    '''
    average_age = sum(i.age for i in lst) / len(lst)
    average_weight = sum(i.weight for i in lst) / len(lst)
    average_height = sum(i.height for i in lst) / len(lst)
    return average_age, average_weight, average_height


number_student_a = int(input("please enter number of students for class A: "))
number_student_b = int(input("please enter number of students for class B: "))

lst_a = get_data(number_student_a)
lst_b = get_data(number_student_b)
[print(i) for i in lst_a]
print(calculate_mean(lst_a))
