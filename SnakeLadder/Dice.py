import random
class Dice:

    def __init__(self, count) -> None:
        self.count = count
        self.min = 1
        self.max = 6

    def rollDice(self):
        diceVal = 0
        for _ in range(self.count):
            diceVal += random.randint(self.min, self.max)
        return diceVal