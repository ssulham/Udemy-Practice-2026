# Imports

from user_actions import *

# Define Functions

def execute():
    while True:

        user_action = input("Type Add, Show, Edit, Complete, or Exit: ")
        user_action = user_action.strip().lower()

        if user_action.startswith("add"):
            add(user_action)

        elif user_action.startswith("show"):
            show()

        elif user_action.startswith("edit"):
            try:
                edit(user_action)
            except ValueError:
                print("Invalid input")
            except IndexError:
                print("Invalid input")

        elif user_action.startswith("complete"):
            try:
                complete(user_action)
            except ValueError:
                print("Invalid input")
            except IndexError:
                print("Invalid input")

        elif user_action.startswith("exit") | user_action.startswith("done"):
            break

        else:
            print("Invalid input")
            print("Try again")

    print("All done.")