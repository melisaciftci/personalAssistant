
def add_task(task):
    tasks = []
    with open('tasks.txt', 'r') as file:
        tasks =file.readlines()

    tasks.append(task + '\n')

    with open('tasks.txt', 'w') as file:
        tasks = file.writelines(tasks)

    return f"Task added: {task}"

while True:
    user_input = input("What can I do for you?").strip()

    if 'add task' in user_input or 'new task' in user_input:
        print("What task would you like to add?")
        task = input("Please specify the task: ").strip()
        if task:
            print(add_task(task))
        else:
            print("You didn't specify a task.")