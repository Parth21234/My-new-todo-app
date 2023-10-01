waiting_list = ['eashan','aryan', 'rudraksh']
waiting_list.sort()
user_prompt= input("Enter the name: ")
for index, item in enumerate(waiting_list):
    print(f"{index+1}.{item.capitalize()}")
    user_prompt == item
    print(index+1, item)
