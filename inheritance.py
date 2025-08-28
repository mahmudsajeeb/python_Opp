#Base class,parent class, common attribute
# derived class , child class, uncommon attribute 

class Gadget:
    def __init__(self,brand,price,color,origin) ->None:
        self.brand =brand
        self.price = price
        self.color = color
        self.origin=origin
    def run(self):
        return f"Running Laptop:{self.brand}"    
    

class Laptop:
    def __init__(self, memory) ->None:
       
        self.memory = memory
 
    def coding(self) ->None:
        return f'Learning python oop'
    
class Phone(Gadget):
    def __init__(self,brand,price,color,origin, dual_sim) ->None:
         
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)
    def run(self):
        return f"Dont usee to much Phone"
    def phone_call(self,number,text) ->None:
        return f'Sending message to Number: {number}, with text{text}'

    def __repr__(self) ->str:
        return f'phone:{self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel) ->None:
        
        self.pixel = pixel
def run(self):
    pass

def change_lens(self):
    pass

#inheritance
my_phone = Phone('iphone', 120000, 'silver','china', True)
# my_phone.phone_call()
print(my_phone)
print(my_phone.brand)
