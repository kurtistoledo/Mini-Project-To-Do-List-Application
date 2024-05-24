# Mini-Project: To-Do List Application

def display_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks, title="Incomplete"):
    tasks.append({"title": title, "status": "Incomplete"})

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} ({task['status']})")

def mark_complete(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["status"] = "Complete"
    else:
        print("Invalid task index.")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index.")

def main():
    my_tasks = []  # Initialize an empty list for tasks
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            title = input("Enter the task title: ")
            add_task(my_tasks, title)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_complete(my_tasks, task_index - 1)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(my_tasks, task_index - 1)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
