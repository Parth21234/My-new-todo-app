from convert import convert

# Decoupling the output! >> Don't complex the output.


""" return f" {feet} feet and {inches} inches is equal to {meters} meters." It should not be this complex, instead."""

result = convert()

if result < 1:  # Problem is that the result is <str> data type.
    print('The kid is so small')

else:
    print('Kid can use the slide')
