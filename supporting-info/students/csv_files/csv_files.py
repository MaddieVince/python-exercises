import csv

exam_results = []

with open("exam_results.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        exam_results.append(line)

# for result in exam_results:
#     print(f"{result[0]}: {result[1]}")

for result in exam_results:
    score = round(float(result[1]) * 100)
    print(f"{result[0]:<20} {score}%")

with open("exam_results_output.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    for result in exam_results:
        score = round(float(result[1]) * 100)
        csv_writer.writerow([result[0], f"{score}%"])