import csv

colours_list = []

with open("supporting-info/students/exercise_data/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list.append(line)

with open("supporting-info/students/exercise_data/colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_list.append(line)

# print(colours_list)

format_colours_list = []

for colour in colours_list:
    print(f"")
    
    format_colours_list.append([colour[1], colour[2], colour[4]])

print()

print(format_colours_list)

for format_colour in 
# with open("exam_results_output.csv", "w") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for result in exam_results:
#         score = round(float(result[1]) * 100)
#         csv_writer.writerow([result[0], f"{score}%"])