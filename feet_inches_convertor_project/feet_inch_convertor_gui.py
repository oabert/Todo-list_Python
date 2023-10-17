import PySimpleGUI as Sg


label_feet = Sg.Text('Enter feet:')
feet_input = Sg.Input()
label_inches = Sg.Text('Enter inches:')
inches_input = Sg.Input()
convert_btn = Sg.Button('Convert')

app_window = Sg.Window('Convertor',
                       [[label_feet, feet_input],
                        [label_inches, inches_input],
                        [convert_btn]])

app_window.read()
app_window.close()
