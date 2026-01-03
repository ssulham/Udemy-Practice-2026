import file_access
import FreeSimpleGUI as sg

from file_access import give_todos

label = sg.Text('Label')
input_box = sg.InputText(tooltip="Input Text", key='todo')
add_btn = sg.Button('Add')
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')

title = "My To-Do App"
layout = [
    [label],
    [input_box],
    [add_btn, edit_btn, complete_btn]
]
font = ("Helvetica", 20)

window = sg.Window(title, layout, font=font)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = file_access.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            file_access.give_todos(todos)
        case 'Edit':
            break
        case 'Complete':
            break
        case sg.WIN_CLOSED:
            break
print("Program properly closed.")
window.close()
