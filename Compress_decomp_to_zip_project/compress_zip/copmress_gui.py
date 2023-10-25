import PySimpleGUI as Sg
import zip_creator_functon

label1 = Sg.Text('Select files to compress:')
input1 = Sg.Input()
select_btn = Sg.FilesBrowse('Choose', key='files')

label2 = Sg.Text('Select destination folder:')
input2 = Sg.Input()
destination_btn = Sg.FolderBrowse('Choose', key='folder')

compress_btn = Sg.Button('Compress')
output_label = Sg.Text(key='output_msg')

app_window = Sg.Window('File Compressor',
                       layout=[[label1, input1, select_btn],
                               [label2, input2, destination_btn],
                               [compress_btn, output_label]])

while True:
    event, values = app_window.read()
    filepaths = values['files'].split(";")
    folder = values['folder']
    zip_creator_functon.make_zipfile(filepaths, folder)
    app_window['output_msg'].update(value='Compression complete!')

app_window.close()
