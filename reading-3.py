import csv

colours_list_20 = []

with open("supporting-info/students/exercise_data/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list_20.append(line)

# print(colours_list)

red_counter = 0
green_counter = 0
blue_counter = 0

for colour in colours_list_20:
    if "green" in colour[4]:
        green_counter += 1
    elif "blue" in colour[4]:
        blue_counter += 1
    elif "red" in colour[4]:
        red_counter += 1
    else:
        pass

print("colours_20.csv")
print(f"Red: {red_counter}")
print(f"Green: {green_counter}")
print(f"Blue: {blue_counter}")

colours_list_213 = []

with open("supporting-info/students/exercise_data/colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list_213.append(line)

print()

red_counter = 0
green_counter = 0
blue_counter = 0

for colour in colours_list_213:
    if "green" in colour[4]:
        green_counter += 1
    elif "blue" in colour[4]:
        blue_counter += 1
    elif "red" in colour[4]:
        red_counter += 1
    else:
        pass

print("colours_213.csv")
print(f"Red: {red_counter}")
print(f"Green: {green_counter}")
print(f"Blue: {blue_counter}")
