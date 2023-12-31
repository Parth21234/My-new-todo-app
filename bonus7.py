import PySimpleGUI as sg


label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")  # FileBrowse is already programmed to select the files.

label2 = sg.Text("Select destination folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")


compress_button = sg.Button("Compress")
window = sg.Window("File Compressor",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                            [compress_button]])
window.read()
window.close()
