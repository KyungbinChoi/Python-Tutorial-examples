print("===Inverse Calculator from a File===")

while True:
    try:
        file_name = input("Please enter 'q' or 'Q' to quiz.\nEnter your File path : ")
        if file_name == 'q' or file_name == 'Q': # q or Q면 종료
            print("Good bye!")
            break
        f = open(file_name, 'r')
        value = f.readline()
        number = float(value)
        f.close()
        inverse_num = number**-1
        print("The inverse of {} is {}".format(number, inverse_num))
    except ValueError as Error1: #실수가 아닌 문자열을 받을 경우
        print("Could not covert string to float '{}'".format(value))
    except ZeroDivisionError as Error2  : # 0은 역수로 취하지 못함
        print("float division by zero")
    except FileNotFoundError as Error3:
        print("{} No such file or directory: {}".format(Error3,file_name))