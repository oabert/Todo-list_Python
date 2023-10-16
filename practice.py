# ips = ['100.122.133.105', '100.122.133.111']
#
# num=int(input('Enter the index of the IP you want'))
# output=f'You chose {ips[num]}'
# print(output)

# seconds = [1.23, 1.45, 1.02, 1.11]
#
# seconds.remove(1.45)

# todo = input('Enter todo: ') + '\n'
#
#             file = open('todos_list', 'r')
#             todos = file.readlines()
#             file.close()
#
#             todos.append(todo)
#
#             file = open('todos_list', 'w')
#             file.writelines(todos)
#             file.close()

# array_name = input('Add a new member: ') + '\n'
#
# name = open('members.txt', 'r')
# array_names = name.readlines()
# name.close()
#
# array_names.append(array_name)
#
# name = open('members.txt', 'w')
# name.writelines(array_names)
# name.close()

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for text in zip(filenames):
#     file = open(f'{text}', 'w')
#     file.write('Hello')
#     file.close()

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for text in filenames:
#     # with open(filenames,'r') as file:
#     #     content = file.read()
#     #     print(content)
#     file = open(text, 'r')
#     read_text = file.read()
#     print(read_text)
#     file.close()

# for text in filenames:
#
#     file = open(text, 'r')
#     content = file.read()
#     print(content)
#     file.close()

# array_docs = ['a.doc', 'b.project, c.list']
#
# array_docs = [array_doc.replace('.', '-') + '.txt' for array_doc in array_docs]
#
# print(array_docs)

# names = ["john smith", "jay santi", "eva kuki"]
#
# names = [name.title() for name in names]
#
# print(names)


# user_entries = ['10', '19.1', '20']
#
# num = [float(i) for i in user_entries]
#
# total = sum(num)
#
# print(total)


# temperatures = [10, 12, 14]
# temperatures = [str(i) + '\n' for i in temperatures]
# file = open("file.txt", 'w')
#
# file.writelines(temperatures)


# numbers = [10.1, 12.3, 14.7]
# numbers = [int(item) for item in numbers]
# print(numbers)




# password = input('Enter your password: ')
#
# result = {}
#
# if len(password) > 7:
#     result['lenght'] = True
# else:
#     result['lenght'] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result['digit'] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase=True
# result['uppercase'] = uppercase
#
# if all(result.values()):
#     print('Strong password')
# else:
#     print("Weak password")


# password = input('Enter your password: ')
#
# if len(password) >7:
#     print("Great password there")
# elif len(password) == 7:
#     print('Password is OK, but not too strong')
# elif len(password) <7:
#     print('Your password is weak"')


# day_temperatures: dict[str, float] = {}

# day_temperatures = {'morning': 11.5, 'noon': 12.7, 'evening': 45.7}
# print(day_temperatures)

# day_temperatures = {'morning': (11.5,12.3,12.4), 'noon': (11.5,12.3,12.4), 'evening': (11.5,12.3,12.4)}


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[1:4]) => return ['b', 'c', 'd']

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[4:]) => return ['e', 'f', 'g']

# ids = ["XF345_89", "XER76849", "XA454_55"]
# x = 0
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)



# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
#
# perimeter = (length + width) * 2
# area = length * width
#
# print("Perimeter is", perimeter)
# print("Area is", area)
#
# if perimeter < 14 and area > 10:
#     print("OK")
# else:
#     print("NOT OK")



# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = value/total_value * 100
#
#     print(f"That is {percentage}%")
#
# except:
#     print('You need to enter a number. Run the program again')


# try:
#     waiting_list = ["john", "marry"]
#     name = input("Enter name: ")
#
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
#
# except:
#     print('zen is not in the list')


# def get_max():
#     grades = [9.6, 9.2, 9.7]
#
#     value = max(grades)
#     return value
#
#
# print(get_max())



# def get_maximum():
#     celsius_l = [14, 15.1, 12.3]
#     maximum = max(celsius_l)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)


# def strength(password):
#     result = {}
#
#     if len(password) > 8:
#         result['length'] = True
#     else:
#         result['length'] = False
#
#     uppercase = False
#     for i in password:
#         if i.isupper():
#             uppercase = True
#     result['uppercase'] = uppercase
#
#     digit = False
#     for i in password:
#         if i.isdigit():
#             digit = True
#     result['digit'] = digit
#
#     if all(result.values()):
#         return 'Strong Password'
#     else:
#         return 'Weak Password'

# def average(num):
#     av=sum(num)/len(num)
#     return av


# def speed(distance, time):
#     return distance / time
#
# print(speed(200, 4))


# def get_age(year_of_birth, current_year=2023):
#
#     age = current_year - year_of_birth
#     return age

# """
#     The function takes one parameter: user_input.
#
#     Split the user_input string by comma (',') using the split() method.
#
#     Store the resulting items in the items list.
#
#     Return the length of the items list using the len() function and the return statement.
# """
# def get_nr_items(user_input):
#     items = user_input.split(',')
#     return len(items)
#


# def mult(argument):
#     return argument*argument


# def weather(temp):
#     if temp > 7:
#         return 'Warm'
#     else:
#         return 'Cold'

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)


# def water_state(temperature):
#     if temperature <=0:
#         return 'Solid'
#     elif 0 < temperature <= 100:
#         return 'Liquid'
#     else:
#         return 'Gas'


# FREEZING_POINT = 0
# BOILING_POINT = 100
#
#
# def water_state(temperature):
#     if temperature <= FREEZING_POINT:
#         return "Solid"
#     elif FREEZING_POINT < temperature < BOILING_POINT:
#         return "Liquid"
#     else:
#         return "Gas"


# main.py:
#
# import functions
#
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
# functions.py:
#
#
# def count(phrase):
#     return phrase.count('.')