try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
try:
    number = int("hello")
except ValueError:
    print("Error: Invalid number.")