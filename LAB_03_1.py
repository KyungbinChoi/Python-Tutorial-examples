#1번 문제
"""
GPA >= 3.9 : summa cum laude
GPA >= 3.6 : magna cum laude
GPA >= 3.3 : cum laude
"""
prize = ["summa cum laude", "magna cum laude", "cum laude" , ""]
my_gpa = float(input("Enter your GPA: "))
print("Your GPA is {}".format(my_gpa))

if my_gpa >= 3.9:my_prize = prize[0]
elif my_gpa >= 3.6:my_prize = prize[1]
elif my_gpa >= 3.3:my_prize = prize[2]
else:my_prize = prize[3]

print("You graduate {}".format(my_prize))