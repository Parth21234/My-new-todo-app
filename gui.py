import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")  # Text has to have a string as the argument.
input_box = sg.InputText(tooltip="Enter To-do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos_existing',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My-To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 12))


# The argument is the title of the window.
# The layout has to have a tuple or a list as an argument. This list has to has other lists inside it.
# label and input_box are in the same box because we want them in one row.
# If we put label and input_box in the different boxes then the input_box would come in the next row.

while True:
    event, values = window.read()  # It displays the window actually on the screen.
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_existing'].update(values=todos)

        case "Edit":
            todo_user_selected = values['todos_existing'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_user_selected)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos_existing'].update(values=todos)
        case "todos_existing":
            window['todo'].update(value=values['todos_existing'][0])
        case sg.WIN_CLOSED:
            break
window.close()
