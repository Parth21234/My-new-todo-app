import json

with open("questions.json", 'r') as file:
    content = file.read()  # Content as a string.

data = json.loads(content)  # Converts content to list.
# It assigns the type of the data which is in the .json file.


for question in data:
    print(question["questions_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}.{alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["Correct_answer"]:
        score = score + 1
        result = "Correct answer."
    else:
        result = "Wrong answer."

    message = f"{index + 1}.{result} Your answer: {question['user_choice']},"\
              f"Correct answer is {question['Correct_answer']}"
    print(message)
print(score, "/", len(data))
