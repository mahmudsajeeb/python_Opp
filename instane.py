class Student:
    school_name = "ABC School"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def introduce(self):
        print(f"Hi, I am {self.name}, roll {self.roll} from   {Student.school_name}")

student1 = Student("Sajib", 20)

student1.introduce()