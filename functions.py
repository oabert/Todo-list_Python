def read_todos(filepath='todos_list'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_input, filepath='todos_list'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_input)
