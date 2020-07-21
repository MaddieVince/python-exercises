# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined in the list above.

groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

number_bought = 0
receipt_list = []

for grocery in groceries:
    number_bought = input(f"How many units of {grocery[0]} were bought? ")
    receipt_list.append([grocery[0], grocery[1] * float(number_bought)])

print(f"====Izzy's Food Emporium===")    

total = 0

for receipt in receipt_list:
    print(f"{receipt[0]:<20} ${receipt[1]:.2f}")
    total = receipt[1] + total
print("===========================")
print(f"{'$':>20} {total:.2f}")

