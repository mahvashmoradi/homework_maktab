class Animal:
    def __init__(self, name):
        self.name = name
        print(name, 'is an animal.')

        
class Mammal(Animal):
    def __init__(self, name):
        print(name, 'is a warm-blooded animal.')
        super().__init__(name)
        
class NonWingedMammal(Mammal):
    def __init__(self, name):
        print(name, "can't fly.")
        super().__init__(name)
        
class NonMarineMammal(Mammal):
    def __init__(self, name):
        print(name, "can't swim.")
        super().__init__(name)

        
class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self,name):
        self.name = name
        print(f'{self.name} is a Dog with 4 legs.')
        super().__init__(name)
d = Dog('Jack')
bat = NonMarineMammal('Jack')
