# Continuously ask the user to enter a number until they provide a blank input. 
# Output the sum of all the numbers.

#Loop 1 - 8
print("Start of Loop 1")
user_input = input("Enter any number: ")
user_total = 0
while len(user_input) > 0:
    user_total = user_total + int(user_input)
    user_input = input("Enter any number: ")
print(user_total)


#Loop 2 - 5
print("Start of Loop 2")
user_input = input("Enter any number: ")
user_total = 0
while len(user_input) > 0:
    user_total = user_total + int(user_input)
    user_input = input("Enter any number: ")
print(user_total)


#Loop 3 - 0
print("Start of Loop 3")
user_input = input("Enter any number: ")
user_total = 0
while len(user_input) > 0:
    user_total = user_total + int(user_input)
    user_input = input("Enter any number: ")
print(user_total)