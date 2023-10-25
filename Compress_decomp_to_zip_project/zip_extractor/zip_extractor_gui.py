import PySimpleGUI as sg
from zip_extractor_function import extract_zip

sg.theme('Black')

label1 = sg.Text('Select zip file')
input1 = sg.Input()
choose_btn1 = sg.FileBrowse('Choose', key='zip_file')

label2 = sg.Text('Select destination directory')
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse('Choose', key='folder')

extract_btn = sg.Button('Extract')
output_msg = sg.Text(key='output', text_color='green')

col1 = sg.Column([[label1],[label2]])
col2 = sg.Column([[input1],[input2]])
col3 = sg.Column([[choose_btn1],[choose_btn2]])

app_window = sg.Window('Archive extractor',
                       layout=[
                           [col1, col2, col3],
                           [extract_btn, output_msg]
                       ])

while True:
    event, values = app_window.read()
    print(event, values)
    zip_path = values['zip_file']
    dest_dir = values['folder']
    extract_zip(zip_path, dest_dir)
    app_window['output'].update(value='Zip file extracted successfully!')

app_window.close()
