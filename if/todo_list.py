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