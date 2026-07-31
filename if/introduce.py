class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
student1 = Student("Priya", 22)
student2 = Student("Ramya", 21)
student3 = Student("Moni", 23)

student1.introduce()
student2.introduce()
student3.introduce()