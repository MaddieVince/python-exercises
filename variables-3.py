# Input distance in kilometers and show meters and centimeters

#Input 1 = 10
firstNumber = int(input("Enter your number in kilometers: "))

meters = firstNumber * 1000
centimeters = firstNumber * 1000000

print(f"{firstNumber}km = {meters}m")
print(f"{firstNumber}km = {centimeters}cm")

#Input 2 = 5.4
firstNumber = float(input("Enter your number in kilometers: "))

meters = int(firstNumber * 1000)
centimeters = int(firstNumber * 1000000)

print(f"{firstNumber}km = {meters}m")
print(f"{firstNumber}km = {centimeters}cm")