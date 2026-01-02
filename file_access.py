# For accessing external file

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    To make sure that the list can persist over multiple uses, an external file is being used.
    This function opens the file for use in other functions.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def give_todos(todos, filepath=FILEPATH):
    """Saves changes made to the list to the external file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)