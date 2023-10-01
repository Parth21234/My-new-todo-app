feet_inches = input("Enter feet and inches: ")

# Decoupling the output! >> Don't complex the output.
def extract():
        parts = feet_inches.split(' ')
        feet_local = float(parts[0])
        inches_local = float(parts[1])
        return feet_local, inches_local  # returns the tuple data object


def convert(feet_conv):

    # The value that this function should return must not be complex.
    # So we are decoupling the function and creating a new function.
    """parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])"""

    feet, inches = extract()

    meters = feet * 0.3048 + inches * 0.0254
    return meters


""" return f" {feet} feet and {inches} inches is equal to {meters} meters." It should not be this complex, instead."""

result = (convert(feet_inches))

if result < 1:  # Problem is that the result is <str> data type.
    print('The kid is so small')

else:
    print('Kid can use the slide')
