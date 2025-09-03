class Dog:
    def  __init__(self,name,breed):
        self.name = name
        self.breed=breed

    def bark(self):
        print(f"{self.name} ({self.breed}) is barking")
    
dog1 =Dog("tom","German Shepher")

dog1.bark()

 
    

