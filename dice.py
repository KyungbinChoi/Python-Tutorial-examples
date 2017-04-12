class Dice:
    def __init__(self, number = 1):
        self.number = number
    def roll(self):
        import random
        self.number = random.choice(range(1,7))
    def getDice(self):
        return  self.number
    def __str__(self):
        return str(self.number)
    def __eq__(self, other):
        if self.number > other.number:
            return "wins"
        elif self.number < other.number:
            return  "losees"
        else:
            return "ties"
