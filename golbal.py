count = 10
def change_value():
    global count
    count = 20
    print("Inside function:", count)
change_value()
print("Outside function:", count)