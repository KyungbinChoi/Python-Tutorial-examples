#LAB_04_02
def nameSeperate(full_name):
    listed_full_name = full_name.split()
    first_name = listed_full_name[0]
    family_name = listed_full_name[1]
    return full_name, first_name, family_name

fullname = input("Enter your name : ")

print("First name is {}".format(nameSeperate(fullname)[1]))
print("Family name is {}".format(nameSeperate(fullname)[2]))

