class Animal:
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print("This is animal Sound")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} is barking")
        return super().sound()

dog1 = Dog("Tommy")
dog1.sound()