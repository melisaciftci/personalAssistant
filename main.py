from datetime import datetime
import random

def add_task(task):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks=[]

    tasks.append(task + '\n')

    with open('tasks.txt', 'w') as file:
        tasks = file.writelines(tasks)

    return f"Task added: {task}"

def show_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []

    if not tasks:
        print("There is nothing here.")
    else:
        print("Tasks:\n")
        for index, tasks in enumerate(tasks, start=1):
            print(f"{index}.{tasks.strip()}")

def date_time():
    current_time=datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H: %M: %S")
    return formatted_time

def random_quote(mood):
    if mood=='happy':
        quotes = ['Today is a good day!', 'You are glowing!']
    elif mood=='sad':
        quotes = ['You can do it!', 'Believe in yourself!']
    return random.choice(quotes)


while True:
    user_input = input("What can I do for you?").strip()

    if 'add task' in user_input or 'new task' in user_input:
        print("What task would you like to add?")
        task = input("Please specify the task: ").strip()
        if task:
            print(add_task(task))
        else:
            print("You didn't specify a task.")

    elif 'show tasks' in user_input:
        print(show_tasks())

    elif 'show date' in user_input:
        print("Current Date and Time: ", date_time())

    elif 'motivate' in user_input or f"today's quote" in user_input:
        print("How do you feel today?")
        mood = input("Mood: ")
        if mood:
            print(random_quote(mood))
        else:
            print("You didn't specify your mood.")

    elif 'bye' in user_input:
        print('Goodbye!')
        break