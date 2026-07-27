from calculator import add, subtract
from fizzbuzz import fizzbuzz
print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
print("\nFizzBuzz Results:")
for i in range(1, 16):
    print(i, "->", fizzbuzz(i))