try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length: # if conditions do not check errors but they check values.
        exit('That looks like a square.') # print the message - 'That looks like a square.' and exit the code.

    area = length * width
    print(area)
except ValueError:
    print('Please enter a number.')