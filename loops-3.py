# Use a while loop to ask the user for three names and append them to a list, then use a for loop to print the
# list.

names_list = []

name_add = ""

name_add = input("Enter a name: ")
while len(name_add) > 0:
    names_list.append(name_add)
    name_add = input("Enter a name: ")

print(names_list)