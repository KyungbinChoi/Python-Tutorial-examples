import dice

a = dice.Dice(5)
a.roll()
print("Player 1 :", a)
b = dice.Dice(2)
b.roll()
print("Player 2 :", b)
print("Player 1", (a==b))
