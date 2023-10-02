import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input_box1 = sg.Input()
convert_button = sg.Button("Covert")

label2 = sg.Text("Enter feet: ")
input_box2 = sg.Input()

window = sg.Window("Convertor", layout=[[label1, input_box1],
                                        [label2, input_box2], [convert_button]])
window.read()
window.close()