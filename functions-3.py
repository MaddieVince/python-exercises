# Read_csv_file will take a filepath and return the content of that file as a list
import csv

def read_csv_file(filepath):
    item_list = []
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            item_list.append(line)
    # print(item_list)
    return item_list

def format_colour_line(colour_data):
    for colour in colour_data:
        print(f"{colour[1]:<15}     {colour[2]:<15}     {colour[4]:>}")
    return colour

csv_file = input("Location of csv file: ")

colour_list = read_csv_file(csv_file)
# print(colour_list)

format_colour = format_colour_line(colour_list)
# print(format_colour)

csv_file = input("Location of csv file: ")

colour_list = read_csv_file(csv_file)
# print(colour_list)

format_colour = format_colour_line(colour_list)
# print(format_colour)
    