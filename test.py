def greet():  # It is just a recipe for the code. If you do not call the function then it would not return anything.
    message = 'hello'
    # local scope variable 'new_message' which cannot be used outside the function greet().
    new_message = message.capitalize()
    return new_message


greeting = greet()
print(greeting)

# new_message and message variables are the local variables.
# print(new_message) >> it would create an error.