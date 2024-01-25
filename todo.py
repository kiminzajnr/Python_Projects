import json
TASK_FILE = "tasks.json"

def show_tasks():
    print("Tasks currently added are:")
    if tasks_lst:
        for task in tasks_lst:
            print(task)
    else:
        print("No tasks added.")

# def complete_task(index):
#     tasks_complete_lst.append(tasks_lst[index])
#     completed_item = tasks_lst.pop(index)
#     print("Task {} completed successfully".format(completed_item))

def add_task(task):
    if task:
        tasks_lst.append(task)
        save_task_to_file()
        print("Task added successfully")

def save_task_to_file():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks_lst, file)

def load_tasks_from_file():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    global tasks_lst
    tasks_lst = load_tasks_from_file()

    print("1: to add a tasks ")
    print("2: to show tasks ")
    print("Your Answer: ", end="")
    user_choice = input()

    if user_choice == "1":
        print("Enter task to add: ", end="")
        task_to_add = input()
        add_task(task_to_add)

    elif user_choice == "2":
        show_tasks()

    # elif user_choice == "3":
    #     print("Please enter task ID to complete: ", end="")
    #     task_id = input()
    #     complete_task(int(task_id))

    
    else:
        print("Please select the available options")

main()