# Imports

from file_access import *

# Define Functions

def add(user_action):
    """Adds new tasks to the external file"""
    if len(user_action) > 4:
        todo = user_action[4:].title().strip() + "\n"
    else:
        todo = input("Enter the new todo item name: ").title().strip() + "\n"

    todos = get_todos()

    todos.append(todo)

    give_todos(todos)

def show():
    """Shows the list of todos"""
    todos = get_todos()

    for index, item in enumerate(todos):
        item = item.strip("\n")
        print(f"{index + 1}. {item}")

def edit(user_action):
    """Lets the user edit a todo list item"""
    todos = get_todos()

    if len(user_action) > 5:
        number = int(user_action[5:]) - 1
    else:
        number = int(input("Enter number of the todo item you would like to edit: "))
        number = number - 1
    new_todo = input("Enter the new todo item name: ").title().strip() + "\n"
    todos[number] = new_todo

    give_todos(todos)

def complete(user_action):
    """Lets the user remove an item from the todo list once it's been completed"""
    todos = get_todos()

    if len(user_action) > 9:
        number = int(user_action[9:]) - 1
    else:
        number = int(input("Enter number of the todo item that has been completed: "))
        number = number - 1
    todos.pop(number)

    give_todos(todos)