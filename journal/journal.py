date = input("Enter today's date: ")
mood = input('How do you rate your day? 1 to 10: ')
thoughts = input("Tell me your thoughts:\n")

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(mood + 2*'\n')
    file.write(thoughts)