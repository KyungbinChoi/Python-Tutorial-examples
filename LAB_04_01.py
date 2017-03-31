#LAB_04_1
full_name = input("Enter your name: ")
full_name = full_name.split()
first_name = full_name[0]
family_name = full_name[1]

print("First name is {}".format(first_name))
print("Family name is {}".format(family_name))


"""
#index() function

full_name = input("Enter your name : ")
space = full_name.index(" ")
first_name = full_name[:space]
family_name = full_name[space+1:]

"""