

feet_inches = input("Enter feet and inches: ")
def extract():
        parts = feet_inches.split(' ')
        feet_local = float(parts[0])
        inches_local = float(parts[1])
        return feet_local, inches_local  # returns the tuple data object
