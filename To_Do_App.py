def display_menu():
    # Display menu options
    print("\nWelcome to the To-Do List Application!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task(tasks)
        if choice == '2':
            view_tasks(tasks)      
        if choice == '3':
            delete_task(tasks)   
        if choice == '4':
            print("Goodbye!")
            break      
            

def add_task(tasks):
    try:
        title = input("Enter a task: ")
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        tasks.append({"title": title})
        print("Task added!")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} ")       

def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)    
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted!")
        else:
            raise IndexError("Invalid task number. Please enter valid number.")
    except ValueError:
        print("Invalid input. Please enter a number")
    except IndexError as e:
        print(f"Error: {e}")
    finally:
        print("Task deleted!")


if __name__ == "__main__":
    main()