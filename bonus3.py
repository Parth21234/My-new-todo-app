# Program to get numbers from a text file and print average of these numbers.

def get_average():
    with open('//files/temperatures.txt', 'r') as file_local:
        temperatures = file_local.readlines()
    values = temperatures[1:]
    values = [float(i) for i in values]
    """sum = 0
    for item in values:
        Sum = sum + item"""

    # Also the sum() funtion which is a builtin function takes the argument as a list.

    average_local = sum(values)/len(values)
    return average_local


average = get_average()
print(average)
