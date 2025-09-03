class Book:
    def __init__(self,title,auhtor,price):
        self.title = title
        self.author = auhtor
        self.price = price

    def details(self):
        print(f"Book: {self.title} by  {self.author} costs {self.price}")

bool1 = Book("Python Basics", "John Smith", 500)

bool1.details()