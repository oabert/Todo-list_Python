import functions

import PySimpleGUI as Sg
label = Sg.Text('Type in a do-to')
input_box = Sg.InputText(tooltip='Enter todo', key='input_todo')
add_button = Sg.Button('Add')

app_window = Sg.Window('My to-do list',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = app_window.read()
    print(1, event)
    print(2, values)

    match event:
        case "Add":
            added_todos = functions.get_read_todos()
            new_todo = values['input_todo']+"\n"
            added_todos.append(new_todo)
            functions.write_todos(added_todos)
        case Sg.WIN_CLOSED:
            break

app_window.close()
