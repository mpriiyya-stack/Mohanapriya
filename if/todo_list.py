class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"'{task}' added successfully.")
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"'{task}' removed successfully.")
        else:
            print(f"'{task}' not found.")
    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTodo List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
                      
class PriorityTodo(TodoList):

    def __init__(self):
        super().__init__()
        self.priority = {}

    def add_task(self, task, priority):
        super().add_task(task)
        self.priority[task] = priority

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            print("\nPriority Todo List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task} - Priority: {self.priority.get(task, 'Normal')}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task},{self.priority[task]}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "w") as file:
                self.tasks = []
                self.priority = {}
            for line in file:
                task, priority = line.strip().split(",")
                self.tasks.append(task)
                self.priority[task] = priority
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved file found.")

    priority = PriorityTodo()

priority.add_task("Study Python", "High")
priority.add_task("Buy Groceries", "Medium")

priority.save_to_file("tasks.txt")

priority.load_from_file("tasks.txt")

priority.list_tasks()
                
                
todo = TodoList()
todo.add_task("Study Python")
todo.add_task("Complete Project")
todo.add_task("Buy Groceries")
todo.list_tasks()
print()
todo.remove_task("Complete Project")
print()
todo.list_tasks()
print()
todo.remove_task("Sleep")