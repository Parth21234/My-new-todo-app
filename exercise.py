import random

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
random = random.randint(a,b)  # Or we can use randrange(lower_limit, upper_limit + 1) instead of randint.
print(random)
