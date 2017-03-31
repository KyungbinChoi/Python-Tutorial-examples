#LAB_04_03
f = open("C:\\Users\\Choikyungbin\\Desktop\\2017\\Management_Data_Analysis\\names.txt", 'r')
lines = f.readlines()
f.close()

f2 = open("C:\\Users\\Choikyungbin\\Desktop\\2017\\Management_Data_Analysis\\seperatednames.txt", 'w')

for line in lines:
    listed_name = line.split()
    first_name = listed_name[0]
    family_name = listed_name[1]
    data = "First name : %s , Family name : %s \n" %(first_name, family_name)
    f2.write(data)

f2.close()

