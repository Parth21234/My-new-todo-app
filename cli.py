from functions import get_todos, write_todos
import time


# This is the frontend of the app.


now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)


# <functions> is executed with the above code.
# Above syntax works only when this file and the program file is in the same directory.
# >> from functions import get_todos, write_todos
# If not in the same directory >> from modules.functions import get_todos, write_todos is used.

# if we use >> <import functions> then we have to use the syntax >> function.get_todos().
# The above case if for the same directory. If the directory is not the same but placed somewhere else >>
# <from modules import functions> is used as a syntax to do the same work.
# That is the same syntax we use to call methods. Just that the functions is a module.

while True:
    user_action = input("Type add, show, edit, exit or complete: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()  # todos is a global variable.

        todos.append(todo + '\n')

        """If you specify the name of the parameters then you don't care about the sequence of variable
        write_todos(filepath='/home/parth/program/files/subfiles/todos.txt', todos_arg=todos)"""

        # You don't have to mention the filepath as it is a default argument.

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")

            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue
            # user_action = input("Type add, show, edit, exit or complete: ")
            # user_action = user_action.strip()

    elif user_action.startswith("complete"):
        try:
            done_todo = user_action[9:]

            todos = get_todos()
            # The statement below is a docstring, it is used in the beginning of the function.
            """or get_todos(filepath='/home/parth/program/files/subfiles/todos.txt')"""
            # Here, filepath is an argument and the value of the argument is specified.

            todos.remove(done_todo + '\n')
            write_todos(todos)

        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print('Command is not valid.')

print('Bye!')
