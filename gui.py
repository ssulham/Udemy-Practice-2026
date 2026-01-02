import file_access
import FreeSimpleGUI as sg

label = sg.Text('Label')
input_box = sg.InputText(tooltip="Input Text")
add_btn = sg.Button('Add')

window = sg.Window("My To-Do List", layout=[[label], [input_box, add_btn]])
window.read()
window.close()
