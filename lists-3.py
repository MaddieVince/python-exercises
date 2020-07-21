# Ask the user for three names, append them to a list, then print the list

names_list = []

name_1 = input("Enter Name 1: ")
name_2 = input("Enter Name 2: ")
name_3 = input("Enter Name 3: ")

names_list.extend([name_1, name_2, name_3])

print(names_list)