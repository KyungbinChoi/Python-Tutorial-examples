import dice

a = dice.Dice()
a.roll()
a_round_1 = a.get_dice()
a.roll()
a_round_2 = a.get_dice()
a_total = a_round_1 + a_round_2
print("Player 1 :", str(a_total))

b = dice.Dice()
b.roll()
b_round_1 = b.get_dice()
b.roll()
b_round_2 = b.get_dice()
b_total = b_round_1 + b_round_2
print("Player 2 :", str(b_total))

if a_total > b_total:
    print("Player 1 wins")
elif a_total < b_total:
    print("Player 2 wins")
else:
    print("Tie")