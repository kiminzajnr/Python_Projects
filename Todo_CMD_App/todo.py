import json
TASK_FILE = "tasks.json"


def show_tasks():
    """Prints all tasks"""
    print("Tasks currently added are:")
    if tasks_lst:
        for index, task in enumerate(tasks_lst):
            print(f"{index}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")
    else:
        print("No tasks added.")


def complete_task(index):
    """Functionality for complete task"""
    if 0 <= index < len(tasks_lst):
        tasks_lst[index]['completed'] = True
        save_task_to_file()
        print("Task marked as completed")
    else:
        print("Invalid task index")


def add_task(task):
    """add task"""
    if task:
        tasks_lst.append({"task": task, "completed": False})
        save_task_to_file()
        print("Task added successfully")
    

def delete_task(index):
    """delete task given a task id"""
    if 0 <= index < len(tasks_lst):
        tasks_lst.remove(tasks_lst[index])
        save_task_to_file()
        print("Task deleted successully")
    else:
        print("OOphs! There is no such task")


def save_task_to_file():
    """persisting to a file"""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks_lst, file)


def load_tasks_from_file():
    """read from the json file"""
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def main():
    """main"""
    global tasks_lst
    tasks_lst = load_tasks_from_file()

    while 1:
        print("\nOptions")
        print("1: to add a tasks ")
        print("2: to show tasks ")
        print("3: to complete a task ")
        print("4: to delete a task ")
        print("5: to quit ")
        print("\nYour Answer: ", end="")
        user_choice = input()

        if user_choice == "1":
            print("Enter task to add: ", end="")
            task_to_add = input()
            add_task(task_to_add)

        elif user_choice == "2":
            show_tasks()

        elif user_choice == "3":
            print("Please enter task ID to complete: ", end="")
            task_id = input()
            complete_task(int(task_id))

        elif user_choice == "4":
            print("Please enter task ID to delete: ", end="")
            task_id = input()
            delete_task(int(task_id))

        elif user_choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please select the available options")


if __name__ == "__main__":
    main()