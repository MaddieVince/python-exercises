names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie",
    "Maddie", "Tash", "Nic", "Rachael", "Bec", "Bec", "Tabitha",
    "Teagen", "Viv", "Anna", "Catherine", "Catherine", "Debby", "Gab",
    "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# for name in names:
#     counter = 0
#     print(name)
#     if 

result = {}
temp=set(names)
for i in temp:
        result[i] = names.count(i)
        
for name, num in result.items():
    print(f"{name:<10} {num}")
