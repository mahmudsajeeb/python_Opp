class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def meow(self):
        print(f"{self.name} says Meow")

cat1 =Cat("Tom","Gray")
cat2 =Cat("Kitty","White")

cat1.meow()
cat2.meow()