import functions
import time
import PySimpleGUI as Sg

Sg.theme('DarkTeal6')

time_label = Sg.Text('', key='time_label')
label = Sg.Text('Type in a do-to')
input_box = Sg.InputText(tooltip='Enter todo', key='input_todo')
add_button = Sg.Button('Add')
list_box = Sg.Listbox(values=functions.get_read_todos(),
                      key='todos_list',
                      enable_events=True,
                      size=[45, 10])

edit_button = Sg.Button('Edit')

complete_btn = Sg.Button('Complete')
exit_btn = Sg.Button('Exit')

app_window = Sg.Window('My to-do list',
                       layout=[[time_label],
                               [label],
                               [input_box, add_button],
                               [list_box, edit_button, complete_btn],
                               [exit_btn]],
                       font=('Helvetica', 20))

while True:
    event, values = app_window.read(timeout=200)
    app_window['time_label'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['todos_list'])

    match event:
        case "Add":
            added_todos = functions.get_read_todos()
            new_todo = values['input_todo'] + "\n"
            added_todos.append(new_todo)
            functions.write_todos(added_todos)

            """Display updated todolist"""
            app_window['todos_list'].update(values=added_todos)

        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['input_todo']

                current_todos = functions.get_read_todos()
                todo_to_edit_index = current_todos.index(todo_to_edit)

                """Updated todo list"""
                current_todos[todo_to_edit_index] = new_todo + '\n'
                functions.write_todos(current_todos)

                app_window['todos_list'].update(values=current_todos)

            except IndexError:
                Sg.popup_error('Please select a todo', font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos_list'][0]

                complete_todos = functions.get_read_todos()

                complete_todos.remove(todo_to_complete)
                functions.write_todos(complete_todos)

                app_window['todos_list'].update(values=complete_todos)
                app_window['input_todo'].update(value='')
            except IndexError:
                Sg.popup_error('Please select a todo', font=('Helvetica', 20))

        case 'Exit':
            break

        case 'todos_list':
            app_window['input_todo'].update(value=values['todos_list'][0])
        case Sg.WIN_CLOSED:
            break

app_window.close()
