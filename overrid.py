class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Vat khai na just mangso khai ami ')

    def exercise(self):
         print("Gyn a kichu tk dybo r excercise krbo")
    
class Cricketer(Person):
        def __init__(self,name,age,height,weight,team) ->None:
            self.team = team
            super().__init__(name,age,height,weight)
        def eat (self):
            print("Vegetables")
sakib = Cricketer('Sakib', 38,68,91,'BD')
sakib.eat()
sakib.exercise()