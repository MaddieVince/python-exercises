import json
with open("data/quiz.json") as json_file:
    json_data = json.load(json_file)

for quiz, json_set in json_data.items():
    # print(quiz, json_set)
    # print()
    # print()
    for q_set, details in json_set.items():
        # print(q_set, details)
        # print()
        # print()
        for detail, values in details.items():
            if detail == "question":
                print(f"Question {q_set}: {values}")
            if detail == "options":
                for option in values:
                    print(f"      {option}")
                print()
            else:
                pass
            # print(detail, value)

