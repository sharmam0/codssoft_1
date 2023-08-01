class ToDoItem:
    def _init_(self, task):
        self.task = task
        self.completed = False

class ToDoList:
    def _init_(self):
        self.items = []

    def add_item(self, task):
        item = ToDoItem(task)
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def mark_complete(self, index):
        if 0 <= index < len(self.items):
            self.items[index].completed = True

    def display_list(self):
        for i, item in enumerate(self.items):
            print(f"{i}. [{item.completed and 'X' or ' '}] {item.task}")


def menu():
    print("\nWelcome to the To-Do List App!")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as complete")
    print("4. Display tasks")
    print("5. Exit")


todo_list = ToDoList()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_item(task)
        print("Task added successfully!")
    elif choice == "2":
        index = int(input("Enter the index of the task to remove: "))
        todo_list.remove_item(index)
        print("Task removed successfully!")
    elif choice == "3":
        index = int(input("Enter the index of the task to mark as complete: "))
        todo_list.mark_complete(index)
        print("Task marked as complete!")
    elif choice == "4":
        todo_list.display_list()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")