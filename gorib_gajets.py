class Laptop:
    def __init__(self,brand,price,color,memory) ->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    def run(self):
        return f'running laptop {self.brand}'
    def coding(self) ->None:
        return f'Learning python oop'
    
class Phone:
    def __init__(self,brand,price,color,dual_sim) ->None:
        self.brand =brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    
    def run(self):
        return f"Dont usee to much Phone"
    def phone_call(self,number,text) ->None:
        return f'Sending message to Number: {number}, with text{text}'

class Camera:
    def __init__(self,brand,price,color,pixel) ->None:
        self.brand = brand
        self.price =price
        self.color =color
        self.pixel = pixel
def run(self):
    pass

def change_lens(self):
    pass
