import os
if os.path.exists("input.txt"):
    print("File found!")
    with open("input.txt", "r") as f:
        content = f.read()
    print(content)
else:
    print("File does not exist.")