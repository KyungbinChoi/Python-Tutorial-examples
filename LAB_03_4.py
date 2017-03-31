#종합 1


while True:
    i = input("***Welcome to Times Table Program***""\n"
              "If you enter 0, Then Exit""\n"
              "Enter your Number 0 ~ 9""\n")
    if i.isdigit():
        i = int(i)
        if i == 0: break
        elif i >= 1 and i <= 9:
            print("{} times table".format(i),"="*8)
            for j in range(1,10):
                print("{} * {} = {}".format(i, j, i*j))
            print("="*8, "End", "="*8)
        else:
            print("Notice! Please enter an integer number between 0 and 9.""\n"
                  "If you enter 0, then EXIT.""\n"
                  "Enter Your Number(0~9).""\n")
    else:
        print("Notice! Please enter an integer number between 0 and 9.""\n"
              "If you enter 0, then EXIT.""\n"
              "Enter Your Number(0~9).""\n")