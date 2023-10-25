import zipfile
import pathlib


def make_zipfile(filepaths, destination_directory):
    destination_path = pathlib.Path(destination_directory, 'compressed.zip')
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            print(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_zipfile(filepaths=['to_be_zipped.txt', 'to_be_zipped_2.txt'], destination_directory='test_zip')
