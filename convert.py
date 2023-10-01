from extract import extract


def convert():

    # The value that this function should return must not be complex.
    # So we are decoupling the function and creating a new function.
    """parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])"""

    feet, inches = extract()

    meters = feet * 0.3048 + inches * 0.0254
    return meters
