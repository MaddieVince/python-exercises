#User input - convert string provided into list items

sentence_list = []

user_input = input("Enter your text: ")
print(user_input)

#split into words, separated by space
sentence_list.extend(user_input.split(" "))

print(f"{len(sentence_list)}, {sentence_list}")

#split by character
word_list = list(user_input)
print(f"{len(word_list)}, {word_list}")




