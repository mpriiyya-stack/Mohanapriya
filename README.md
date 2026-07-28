# Mohanapriya
# Day -1
("AI/ML Training Log")
Name: Mohanapriya  
Mentor: Aditi Krishana

1. Hello World
- Learn how to print output in Python.
# Concept
print() is a built-in Python function used to display output on the console.
#  What I Learned
- How to write my first Python program.
- How print() displays output.
- Strings are written inside quotation marks.

2. Variables
- Variables are used to store values in memory.

# What I Learned
- Variables are used to store data.
- Python automatically determines the data type.
- Different data types are used for different kinds of values.
- print() is used to display variable values.
# Functions Used
print()
# Operators Used
= (Assignment Operator)
# Purpose
= → Assigns (stores) a value in a variable.
print() → Displays the value stored in the variable.
# Data Types Used
- str → Stores text ("Priya")
- int → Stores whole numbers (21)
- float → Stores decimal numbers (5.4)
- bool → Stores Boolean values (True or False)
 3. User Input
- Learn how to receive input from the user during program execution and store it in variables.
# Function Used
- input()
- print()
 # Example
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name)
print("Age:", age)
# Output
Enter your name: Priya
Enter your age: 21
Name: Priya
Age: 21
4. f-Strings
- `f` allows variables and expressions to be inserted directly inside a string using curly braces `{}`.
# What I Learned
- I learned how to use f-strings to format strings.
- I learned that variables can be inserted directly into a string using `{}`.
- I learned that f-strings make the code more readable and easier to write than string concatenation.
Function Used: print()
Feature Used: f-string (Formatted String Literal)
5. Operators
# What I Learned
- I learned how to perform arithmetic operations.
- I learned how to compare values using comparison operators.
- I learned that comparison operators return `True` or `False`.
6. if, elif, else
- `if` executes a block of code when the given condition is `True`.
- `elif` checks another condition if the previous condition is `False`.
- `else` executes when none of the above conditions are `True`.
- `print()` displays the output.
# What I Learned
- I learned how to make decisions using conditional statements.
- I learned that only one matching block is executed.
- I learned to use `if`, `elif`, and `else` to handle multiple conditions
7. for Loop
# What I Learned
- I learned how to repeat a block of code using a `for` loop.
- I learned how to use `range()` to control the number of iterations.
- I learned that the loop executes once for each value in the sequence.
8. while Loop
- `while` repeatedly executes a block of code as long as the condition is `True`.
# What I Learned
- I learned how to use a `while` loop for repeated execution.
- I learned that the loop continues until the condition becomes `False`.
- I learned the importance of updating the loop variable to avoid an infinite loop.
# Git Commands Practiced
- git init
- git add.
- git commit -m "Day 1: first commit"
- git branch -M main
- git push
# day 2
 day2-word-counter
1. String Indexing
 - String Indexing (`[]`)
- String indexing is used to access individual characters in a string.
- Indexing starts from `0`.
# What I Learned
- I learned how to access characters using their index.
- I learned that the first character always has index `0`.
2. String Slicing
- String Slicing (`[start:end]`)
- String slicing is used to extract a portion of a string.
- The start index is included, and the end index is excluded.
# What I Learned
- I learned how to extract part of a string.
- I learned that slicing does not modify the original string.
3. len()
- `len()` returns the total number of characters in a string or the number of items in a collection.
# What I Learned
- I learned how to find the length of a string.
- I learned that spaces are also counted as characters.
4. lower()
- Converts all characters in a string to lowercase.
# What I Learned
- I learned how to convert text to lowercase.
- I learned that `lower()` returns a new string.
5. upper()
- Converts all characters in a string to uppercase.
# What I Learned
- I learned how to convert text to uppercase.
- I learned that `upper()` returns a new string.
6. strip()
- Removes leading and trailing whitespace from a string.
# What I Learned
- I learned how to remove unwanted spaces.
- I learned that `strip()` does not remove spaces in the middle of a string.
7. replace()
- Replaces one substring with another substring.
# What I Learned
- I learned how to replace specific text in a string.
- I learned that it returns a new string.
8. split()
- Splits a string into a list using a separator.
# What I Learned
- I learned how to convert a sentence into a list of words.
- I learned that the default separator is a space.
9. join()
- Joins the elements of a list into a single string.
# What I Learned
- I learned how to combine list elements into one string.
- I learned that `join()` requires all elements to be strings.
10. Reverse String
- String Slicing (`[::-1]`)
- `[::-1]` reverses the characters in a string.
# What I Learned
- I learned how to reverse a string using slicing.
- I learned that the original string remains unchanged.
11. Lists
- `append()` adds a new item to the end of a list.
- `remove()` removes a specified item from the list.
# What I Learned
- I learned how to create and modify lists.
- I learned how to access list items using indexes.
12. enumerate()
 Returns both the index and the value while looping through a sequence.
# What I Learned
- I learned how to get both the index and value in a loop.
- I learned that `enumerate()` makes loops easier to read.
13. Tuples

- A tuple stores multiple values and cannot be modified after creation.
# What I Learned
- I learned that tuples are immutable.
- I learned that trying to modify a tuple raises a `TypeError`.
14. Dictionaries
- `items()` returns all key-value pairs in a dictionary.
# What I Learned
- I learned how to create dictionaries.
- I learned how to access values using keys.
# Day 3
1. Functions (Without Parameters)
- Functions are reusable blocks of code.
A function is created using the `def` keyword and executed by calling its name.
# What I Learned
- How to create a function.
- How to call a function.
- Functions help avoid writing the same code repeatedly.

2. Functions (With Parameters)

- Parameters allow data to be passed into a function.
Functions can accept one or more parameters to perform operations on different inputs.
# What I Learned
- How to pass arguments to a function.
- How parameters make functions reusable.
- Used f-strings with function parameters.
3. Return Values
- Functions can return values using the `return` keyword.
The `return` statement sends the result back to the caller instead of printing it inside the function.
# What I Learned
- Difference between `print()` and `return`.
- Stored returned values in variables.
- Printed returned values.
4. Default Parameters
- Functions can have default parameter values.
A default value is used when no argument is passed to the function.
# What I Learned
- Created functions with default parameters.
- Called functions with and without arguments.
- Learned how default values improve flexibility.
5. Docstrings
- Docstrings describe the purpose of a function.
A docstring is written inside triple quotes (`""" """`) immediately below the function definition.
# What I Learned
- Added documentation to functions.
- Learned that docstrings improve code readability.
- Understood that docstrings explain what a function does.
6. Variable Scope
- Variables can have local or global scope.
Variables created inside a function are local, while variables created outside are global.
# What I Learned
- Local variables are accessible only inside the function.
- Accessing a local variable outside the function causes a `NameError`.
- Global variables can be accessed throughout the program.
- Using the `global` keyword modifies the global variable inside a function.
7. Git & GitHub
- Practiced Git branching and merging.
Git branches allow developers to work on new features without affecting the main branch.
# What I Learned
- Merged the `day2-word-counter` branch into `main`.
- Resolved merge conflicts in `README.md`.
- Pushed the updated `main` branch to GitHub.
- Deleted the merged branch.
- Created a new branch called `day3-refactor`.
- Pushed the new branch to GitHub.

# Day 4
# 1. File Handling

- Learned how to create, write, read, append, and process text files using Python.
- Python provides the `open()` function to work with files. Different file modes such as `"r"`, `"w"`, and `"a"` are used for reading, writing, and appending data.
# What I Learned
- Created a new text file using write mode.
- Wrote multiple lines into a file.
- Read the complete contents of a file.
- Read a file line by line.
- Appended new content without deleting existing data.
- Understood different file modes (`r`, `w`, `a`).
# 2. Error Handling
- Learned how to handle program errors without crashing.
- Python uses `try`, `except`, `else`, and `finally` blocks to handle exceptions gracefully and improve program reliability.
# What I Learned
- Handled `FileNotFoundError`.
- Handled `ZeroDivisionError`.
- Handled `ValueError`.
- Used `try`, `except`, `else`, and `finally`.
- Displayed user-friendly error messages.
# 3. File-Based Word Counter

- Modified the previous word counter to read input from a text file.
- Files can be processed to count word frequencies and save the results into another file.
# What I Learned
- Read text from `input.txt`.
- Counted the frequency of each word.
- Stored results using a dictionary.
- Saved the output into `word_counts.txt`.
- Checked whether the input file exists before reading it.
- Used `os.path.exists()` for file checking.
# 4. Modules and Code Organization
- Learned how to organize Python code into multiple modules.
- Modules help split programs into reusable files, making projects easier to maintain and understand.
# What I Learned
- Created custom modules.
- Imported functions using `import` and `from ... import`.
- Built a calculator module.
- Built a FizzBuzz module.
- Created a Number Guessing Game using the `random` module.
- Used the `os` module to check whether files exist.
- Understood the importance of modular programming and reusable code.

# Day 5
# What I Learned
- Created and worked with multiple Git branches.
- Practiced resolving merge conflicts in VS Code.
- Learned the purpose of git restore, git reset, git revert and git stash.
# Personal Notes
Merge conflicts were confusing at first because I had to understand which changes to keep. After practicing with Git, I understood how conflicts are resolved and how different undo commands work.

# Day 6
# 1. Object-Oriented Programming (OOP)
- Learned the basics of Object-Oriented Programming in Python.
- A class is a blueprint used to create objects.
- An object is an instance of a class.
# What I Learned
- Created a `Student` class.
- Created multiple objects from the same class.
- Accessed object attributes using dot (`.`) notation.
# 2. Constructors (__init__)
- The `__init__()` method is called automatically when an object is created.
# What I Learned
- Initialized object data using constructors.
- Passed values through parameters.
- Stored values using `self`.
# 3. Methods
- Methods are functions defined inside a class.
# What I Learned
- Created an `introduce()` method.
- Called methods using objects.
- Used f-strings to display object information.
# 4. Class Attribute vs Instance Attribute
- Class attributes are shared by all objects.
- Instance attributes belong to individual objects.
# What I Learned
- Created a class attribute (`college`).
- Created instance attributes (`name`, `age`).
- Understood the difference between shared and individual data.
# 5. self Keyword
- `self` refers to the current object.
# What I Learned
- Learned why every instance method needs `self`.
- Observed the error when `self` was removed.
- Fixed the error by adding `self` back.
# 6. TodoList Class
- Built a simple Todo List using OOP.
# What I Learned
- Added tasks using `add_task()`.
- Removed tasks using `remove_task()`.
- Displayed tasks using `list_tasks()`.
- Handled removing a task that does not exist.
# 7. Extra Practice
# What I Learned
- Created a `Car` class.
- Practiced creating objects and calling methods.
- Improved confidence in writing simple OOP programs.
