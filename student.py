class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def introduce(self):
        print(f"Hi, I am {self.name} my roll {self.roll}")
    
name1 = Student("Sajib",20)
name1.introduce()