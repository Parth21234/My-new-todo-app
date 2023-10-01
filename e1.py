import glob

myfiles = glob.glob("/home/parth/program/files/subfiles/*.txt")  # This function returns a list

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
