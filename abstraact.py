from abc import ABC, abstractmethod
class Animal:
    @abstractmethod # enforce all
    def eat(self):
        print('I need food')
    def move(self):
        pass

class Monkey (Animal):
    def __init__(self)->None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()