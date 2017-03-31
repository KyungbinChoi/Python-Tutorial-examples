#LAB_04_05
f1 = open("C:\\Users\\Choikyungbin\\Desktop\\2017\\Management_Data_Analysis\\ExamsQuiz.txt" , "r")
f2 = open("C:\\Users\\Choikyungbin\\Desktop\\2017\\Management_Data_Analysis\\ExamsQuiz_r.txt" , "w")

lines = f1.readlines()
for line in lines:
    splited = line.split()
    total = float(splited[1]) + float(splited[2]) +float(splited[3])
    writeline = splited[0] + " " + splited[1] + " " +splited[2] + " " + splited[3] + str(total) + "\n"
    f2.write(writeline)

f1.close()
f2.close()

