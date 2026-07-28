class Student:

    college = "RIT"      

    def __init__(self, name, age):
        self.name = name
        self.age = age    

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f"I study at {Student.college}")


student1 = Student("Priya", 22)
student2 = Student("Ramya", 21)
student3 = Student("Moni", 23)

student1.introduce()
print()

student2.introduce()
print()

student3.introduce()