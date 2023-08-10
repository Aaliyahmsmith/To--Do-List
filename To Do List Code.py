#Aaliyah Smith
#8/10/2023
#To-Do List
"""
This is a program focused on the basic functions of a to do list.
Users can effortlessly add tasks to the list, remove completed or
unnecessary items, and view the remaining tasks.
"""

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the to-do list include:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("The to-do list is empty.")

   
def main():
    todo_list = ToDoList()
    name = input("Input your First Name : ")
    print ("Hello" + ", " + name + "!")
    print("Welcome to your To-Do List! \nPlease select an option below to get started...")
    
    while True: 
        print ("To-Do List Menu: ")
        print("1~ Add Task")
        print("2~ Remove Task")
        print("3~ View Tasks")
        print("4~ Exit To-Do List")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the to-do list application.")
            print(f"GoodBye, {name}!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
