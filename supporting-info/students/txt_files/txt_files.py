names = []

with open("names.txt") as txt_file:
    # print(txt_file)

    for line in txt_file:
        line = line.strip()
        names.append(line)
    
print(names)

for name in names:
    print(name)

with open("names_output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(name + "\n")   