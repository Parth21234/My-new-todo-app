import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")  # Text has to have a string as the argument.
input_box = sg.InputText(tooltip="Enter To-do")
add_button = sg.Button("Add")
window = sg.Window('My-To-Do App', layout=[[label], [input_box, add_button]])


# The argument is the title of the window.
# The layout has to have a tuple or a list as an argument.
# label and input_box are in the same box because we want them in a straight line.
# If we put label and input_box in the different boxes then the input_box would come in the next line.

window.read()  # It displays the window actually on the screen.
window.close()
