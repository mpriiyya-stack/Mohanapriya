#with open("myfile.txt", "r") as f:
try:
    with open("myfile.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Sorry! The file was not found.")