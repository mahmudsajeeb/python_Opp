import random

class NumberGame:
    def __init__(self,playerName):
         self.playerName = playerName

    def guess(self):
         number = random.randint(1,6)
         print(f"{self.playerName} guessed...{number}")

player1 = NumberGame("sajib")
player2 = NumberGame("mumu")

player1.guess()
player2.guess()