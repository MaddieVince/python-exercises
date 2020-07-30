import csv

colours_list_20 = []

with open("supporting-info/students/exercise_data/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list_20.append(line)

# print(colours_list)

for colour in colours_list_20:
    print(f"{colour[1]}     {colour[2]}     {colour[4]}")

colours_list_213 = []

with open("supporting-info/students/exercise_data/colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list_213.append(line)

print()

for colour in colours_list_213:
    print(f"{colour[1]}     {colour[2]}     {colour[4]}")