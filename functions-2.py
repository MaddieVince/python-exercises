# Calculate the mean of a list of numbers

# User to input numbers
# Stop when a blank input is entered
# Use the sum of the integers and total numbers to calculate mean
# Print mean

def calculate_mean(total_sum, num_items):
    mean = total_sum / num_items
    print(f"{mean:.2f}")

num_list = []

num_input = 0
total_sum = 0
num_items = 0

num_input = input("Enter a number: ")
while len(num_input) > 0:
    total_sum += int(num_input)
    num_items += 1
    num_input = input("Enter a number: ")
      
# print(total_sum, num_items)

calculate_mean(total_sum, num_items)

