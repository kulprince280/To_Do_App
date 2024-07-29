# A simple command-line To-Do app in Python

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added task: '{task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['completed'] = True
            print(f"Task '{self.tasks[task_number]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            task = self.tasks.pop(task_number)
            print(f"Deleted task: '{task['task']}'")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nTo-Do App")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                self.complete_task(task_number)
            elif choice == '4':
                task_number = int(input("Enter task number to delete: ")) - 1
                self.delete_task(task_number)
            elif choice == '5':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = ToDoApp()
    app.run()