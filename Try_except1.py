print("===Inverse Calculator===")

while True:
    try:
        user_input = input("Please enter 'q' or 'Q' to quiz.\nEnter your number : ")
        number = float(user_input)
        inverse_num = number**-1
        print("The inverse of {} is {}".format(number, inverse_num))
    except ValueError:
        if user_input == 'q' or user_input == 'Q':
            print("Good bye!")
            break
        else:
            print("Could not covert string to float '{}'".format(user_input))

