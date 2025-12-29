filename = "tasks.txt"

def load_tasks():
    tasks = []

    try:
        with open(filename,"r") as file:

            for line in file:
                task, status = line.strip().split("|")

                tasks.append({"task": task, "status": status})

    except FileNotFoundError:
        pass            

    return tasks

def save_tasks(tasks):
    with open(filename, "w") as file:

        for task in tasks:
            file.write(f"{task['task']}|{task['status']}\n")

def add_task(tasks):
    task_name = input("Enter task: ")

    tasks.append({"task": task_name, "status": "Pending"})

    save_tasks(tasks)
    print("Task added successfully!")

def view_task(tasks):

    if not tasks:
        print("No tasks available.")
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {task['status']}")

def complete_task(tasks):
    view_task(tasks)
    try:
       choice = int(input("Enter task number to mark as completed: "))
        
       tasks[choice - 1]["status"] = "Completed"
       save_tasks(tasks)
       print("Task marked as completed!")
    except (IndexError, ValueError):
       print("Invalid Choice.")

def delete_task(tasks):
    view_task(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Task '{removed['task']} deleted.")
    except (IndexError, ValueError):
        print("Invalid choice.")
          
def main():
    tasks = load_tasks()

    while True:

        print("\n--- TO-Do LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
           add_task(tasks)
        elif choice == "2":
           view_task(tasks)
        elif choice == "3":
           complete_task(tasks)
        elif choice == "4":
           delete_task(tasks)
        elif choice == "5":
           print("Exiting application. Goodbye!")
           break
        else:
           print("Invalid choice. Try again.")

main()





