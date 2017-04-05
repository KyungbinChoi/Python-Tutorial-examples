import dice

def casino_game():
    #한 쌍의 주사위를 24번 던져 적어도 한 번 이상 두 주사위가 모두 6이 나오면 승리
    dice1 = dice.Dice()
    dice2 = dice.Dice()
    count = 0
    while count <= 24:
        dice1.roll()
        dice2.roll()
        if dice1.get_dice() == 6 and dice2.get_dice() == 6:
            return "win"
        elif count == 24:
            return "lose"
        else:
            count += 1

# 10000 번 반복 실행
counting_wins = 0

for i in range(10001):
    if casino_game() == "win":
        counting_wins += 1

print(counting_wins)