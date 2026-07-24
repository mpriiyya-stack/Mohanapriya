try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Sorry! File not found.")
else:
    print("File read successfully!")
    print(content)
finally:
    print("Program execution completed.")