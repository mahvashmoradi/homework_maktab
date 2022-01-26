class Species:

    def __init__(self,age,name,kind,gender=None):
        self.age=age
        self.name=name
        self.kind=kind
        self.gender=gender

    def info(self):
        print(f"{self.name} is a {self.kind} and he/she is {self.kind}")


class Human(Species):
    def __init__(self,family,age,name,kind,gender=None):
        Species.__init__(self,age,name,'Human',gender)
        self.family=family
        
    def job_condition(self,employment_sitution):
        self.employment_sitution=employment_sitution
        if self.employment_sitution=='student':
            print(f"{self.name} you should study hard")
        

class Animal(Species):
    pass

#human_1= Species(27,'mahvash','human')
human_1= Human(27,'mahvash','human')

animal=Species(5,'Daya','Dog','Male')

human_1.info()
animal.info()
human_1.job_condition('student')
print(human_1.name, human_1.employment_sitution)
