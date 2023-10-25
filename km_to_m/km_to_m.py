import PySimpleGUI as sg

sg.theme('Black')


def km_to_miles(km):
    return km / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

exit_btn = sg.Button('Exit')

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box],
                           [miles_button, exit_btn, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
