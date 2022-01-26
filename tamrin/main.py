# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Human:
    planet='Earth'
    def __init__(self, name, age, family_name):
        self.name = name
        self.age = age
        self.family_name = family_name

    def __str__(self):
        return self.name

    def greeting(self):
        print(f'my name is {self.name} and {self.family_name} well come world')

    def test(self):
        print(f' well come world {Human.planet}')

mahvash = Human('mash', 20, 'mor')
yasaman = Human('yasi', 25, 'kam')
print(mahvash)
print(yasaman.family_name)
mahvash.greeting()
yasaman.greeting()
mahvash.test()