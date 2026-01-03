import file_access
import FreeSimpleGUI as sg

label = sg.Text('Label')
input_box = sg.InputText(tooltip="Input Text", key='todo')
list_box = sg.Listbox(
    values=file_access.get_todos(),
    key='todos',
    enable_events=True,
    size=(45, 10)
)
add_btn = sg.Button('Add')
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')

title = "My To-Do App"
layout = [
    [label],
    [input_box, add_btn],
    [list_box],
    [edit_btn, complete_btn]
]
font = ("Helvetica", 20)

window = sg.Window(title, layout, font=font)

# Code Execution

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
            window['todos'].update(todos)
        case 'Edit':
            old_todo = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = file_access.get_todos()
            index = todos.index(old_todo)
            todos[index] = new_todo
            file_access.give_todos(todos)
            window["todos"].update(todos)
        case 'Complete':
            old_todo = values["todos"][0]
            todos = file_access.get_todos()
            index = todos.index(old_todo)
            todos.pop(index)
            file_access.give_todos(todos)
            window['todos'].update(todos)
        case sg.WIN_CLOSED:
            break
print("Program properly closed.")
window.close()
