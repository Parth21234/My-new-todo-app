FILEPATH = '/home/parth/program/files/subfiles/todos.txt'

# This is the backend and interface for the app.


def get_todos(filepath=FILEPATH):  # filepath is a parameter.
    """ Read the text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # outer scope is the variable declared outside the function.
        return todos_local

# Default parameters should come after the non-default parameters.


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""

    # This function is more like a procedure, it does not return anything.

    with open(filepath, 'w') as file:  # We don't need the function to return any value.
        file.writelines(todos_arg)     # This function returns None.


if __name__ == "__main__":
    print(get_todos())

# The value of __name__ is __main__ if we print __name__ here in functions.py
# But if we access the valur of __name__ in the cli.py through importing functions
# Then the value of __name__ turn out to be functions.
