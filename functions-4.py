# Write a funciton to calculate the total cost for each item.

def calculate_cost(unit_price, number_purchase):
    total_cost = float(unit_price) * float(number_purchase)
    # print(total_cost)
    return total_cost


groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

receipt_list = []

for grocery in groceries:
    unit_price = grocery[1]
    number_purchase = input(f"How many units of {grocery[0]} were bought? ")
    total_cost = calculate_cost(unit_price, number_purchase)
    receipt_list.append([grocery[0], total_cost])

print(f"====Izzy's Food Emporium===")    

total = 0

for receipt in receipt_list:
    print(f"{receipt[0]:<20} ${receipt[1]:.2f}")
    total = receipt[1] + total
print("===========================")
print(f"{'$':>20} {total:.2f}")