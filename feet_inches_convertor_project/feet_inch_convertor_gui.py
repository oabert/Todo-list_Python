import PySimpleGUI as Sg
import feet_to_meter_fnc

label_feet = Sg.Text('Enter feet:')
feet_input = Sg.Input(key='feet')

label_inches = Sg.Text('Enter inches:')
inches_input = Sg.Input(key='inches')

convert_btn = Sg.Button('Convert', key='convert_btn')
result = Sg.Text(key='result')

# exit_btn = Sg.Button('Exit', key='exit')

app_window = Sg.Window('Convertor',
                       [[label_feet, feet_input],
                        [label_inches, inches_input],
                        [convert_btn, result]])

while True:
    event, values = app_window.read()
    print(event, values)
    feet = float(values['feet'])
    inches = float(values['inches'])
    convert_result = feet_to_meter_fnc.convert(feet, inches)
    app_window['result'].update(value=f"{convert_result} m")


# while True:
#     event, values = app_window.read()
#     print(event, values)
#
#     match event:
#         case "Convert":
#             feet = float(values['feet'])
#             inches = float(values['inches'])
#             convert_result = feet_to_meter_fnc.convert(feet, inches)
#             app_window['result'].update(value=f"{convert_result} m")
#         case "Exit":
#             break
#         case Sg.WIN_CLOSED:
#             break

app_window.close()
