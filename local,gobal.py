message1 = "Hello" #global variable
def my_function():
    message = "Hello this is priya" #local variable
    print(message)
    print(message1)
my_function()
print(message1)

count = 10

def change_value():
    count = 20
    print("Inside function:", count)
change_value()
print("Outside function:", count)