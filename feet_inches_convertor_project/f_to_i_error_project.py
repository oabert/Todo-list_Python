import PySimpleGUI as sg


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")
error_btn = sg.Text('OK', key='error')

col1 = sg.Column([[feet_label], [inches_label]])
col2 = sg.Column([[feet_input], [inches_input]])
# col3 = sg.Column([])
window = sg.Window("Convertor",
                   layout=[[col1, col2],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = convert(feet, inches)
                window["output"].update(value=f"{result} m", text_color="white")
            except ValueError:
                sg.popup('Please provide two numbers', font=('Helvetica', 15))

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
