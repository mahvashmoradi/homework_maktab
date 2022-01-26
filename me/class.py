class Pet:
    
    def __init__(self,age,animal_type,name,breed=None,color=None,gender=None):

        self.age=age
        self.breed=breed
        self.animal_type=animal_type
        self.name=name
        self.color=color
        self.gender=gender

    def __str__(self):

        return f'This pet is an {self.animal_type},{self.breed}'

        
    def _print ():

        pass
    
'''
cat=Pet(2,"persian","cat","cat","white","male")
#dog=Pet(5,"chidso","dog",""
animal1 = Pet(9,"TirierYourkshaier","Dog", "Fido",
              "White", "Girls")

animal_1=Pet('Dala',2,'Persian','Dog','Black','male')
animal_2=Pet('Malos',3,'German','Cat','White','female')
animal_3=Pet('Nana',5,'Frensh','Dog','Brown','female')
chick = Pet(1, 'unknown','female','YoYo','white')
'''
animal_1 = Pet(2, 'persian', 'cat', 'caty', 'white', 'female')
animal_2 = Pet(2, 'Dala','Persian','Dog','Black','male')
animal_3 = Pet(3, 'Malos','German','Cat','White','female')
animal_4 = Pet(5, 'Nana','Frensh','Dog','Brown','female')
animal_5 = Pet(9, "TirierYourkshaier", "Dog", "Fido", "White", "Girls")
print(animal_1)
Pet(name = 'majid', animal_type = 'cat', age = 5)











