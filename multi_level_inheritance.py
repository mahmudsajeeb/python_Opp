class Vehicle:

    def __init__(self,name,price) ->None:
        self.name = name
        self.price =price
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)        