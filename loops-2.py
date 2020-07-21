# Use a for loop to format and print mailing_list



mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for details in mailing_list:
    print(f"{details[0]:<30}: {details[1]}")

