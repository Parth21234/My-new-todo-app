import csv

with open("new.csv", 'r') as file:
    data = list(csv.reader(file))
    #  reader() would give us an 'iterator' which is not readable, so we convert it into list
print(data)  # Output is list of list. Each list represent a row.
city = input("Enter the name of the city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])
