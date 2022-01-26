class Species:
    def __init__(self, age, name, kind, gender=None):
        self.age = age
        self.name = name
        self.kind = kind
        self.gender = gender
    def info(self):
        print(f'{self.name} is a {self.kind} and he/she is {self.age} years old')

    def express(self,emotion):
        self.emotion=emotion
        print(f'lob lob lob {emotion}')
        
class Human(Species):
    def __init__(self, age, name, family_name, gender=None):
        super().__init__(age, name, 'Human', gender)
        self.family_name = family_name
    def job_condition(self, emplyment_situation):
        self.emplyment_situation = emplyment_situation
        if self.emplyment_situation == 'student':
            print(f'{self.name} you should study hard')
    def change_name(self,name):
        print(f"your name {self.name} changed to {name}")
        self.name=name
        print(f"your name changed to{self.name} {name}")
        
    def express(self,emotion):
        self.emotion=emotion
        print(f'is talking about {emotion}')
        
class Animal(Species):
    pass

human_1 = Human(25, 'mina', 'habibi', 'Female')
animal_1 = Animal(5, 'Daya', 'Dog', 'Male')
human_1.info()
animal_1.info()
human_1.job_condition('student')
print(human_1.name, human_1.emplyment_situation)
human_1.change_name('gha')
print(human_1.name)
human_1.express('anger')
animal_1.express('anger')
