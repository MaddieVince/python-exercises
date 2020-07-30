import csv

def read_csv_file(filepath):
    item_list = []
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            item_list.append(line)
    # print(item_list)
    return item_list

################################################

csv_file = input("Location of csv file: ")

title_list = []
colour_list = read_csv_file(csv_file)
for i in range(1):
    title_list = colour_list[0]
# print(title_list)

full_list = []

itercolours = iter(colour_list)
next(itercolours)
for colours in itercolours:
    for colour in colours:
        dict_colour = dict(zip(title_list, colours))
        full_list.append(dict_colour)
print(f"colours = {full_list[2]}")