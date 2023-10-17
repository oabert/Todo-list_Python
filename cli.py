import functions
import time


current_time = time.strftime("%b %d, %Y %H:%M:%S")
print('It is ', current_time)


from functions import read_todos, write_todos

while True:
    user_action = input('Please enter your action: ')
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = read_todos()

        # file = open('todos_list', 'r')
        # todos = file.readlines()
        # file.close()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        with open('todos_list', 'r') as file:
            todos = file.readlines()

        # file = open('todos_list', 'r')
        # todos = file.readlines()
        # file.close()

        # new_todos = [item.strip('\n') for item in todos]

        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # for index, item in enumerate(new_todos):
        #     list_text = f"{index + 1}. {item}"
        #     print(list_text)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            list_text = f"{index + 1}. {item}"
            print(list_text)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            # or index = int(input("Number of the todo to complete: ")) - 1

            todos = read_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = read_todos()

            todo_to_remove = todos.pop(number - 1).strip('\n')

            write_todos('todos_list', todos)

            message = f'Todo `{todo_to_remove}` was removed from the list'
            print(message)

        except IndexError:
            print('There is no todo with this number')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Wrong command')



