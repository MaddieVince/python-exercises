# For each name in ​names.txt​, output the name and line number.

names = []

with open("supporting-info/students/txt_files/names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)


print(names)

counter = 1

for name in names:
    print(f"{counter}. {name}")
    counter += 1

# reset counter   
counter = 1
     
with open("z-output/reading-1-output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(f"{counter}. {name}" + "\n")
        counter +=1