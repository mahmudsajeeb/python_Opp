class superHero:
    def __init__(self,name,power):
        self.name = name
        self.power= power

    def introduce(self):
        print(f"I am {self.name}, and my power is{self.power}")

superHero1 = superHero("Batman", "Intelligenece")
superHero2 = superHero("superman", "Flying")

superHero2.introduce()
superHero1.introduce()