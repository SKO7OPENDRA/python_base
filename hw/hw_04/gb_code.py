# x = [1, 2, 3]

# def test(some_list):
#     some_list.append(100)
# test(x)
# print(x)

# def test(some_list):
#     some_list = [3]
#     return some_list
# a = test(x)
# print(a)

# x = [1, 2, 3, 4]
#
# for number in x.copy():
#     print(number)
#     x.remove(number)
# print(x)


# a = [1, 2, 3, 4]
# b = a.copy()
# b.append(100)
# print(a)

# import copy
# a = [1, 2, 3, [100]]
# b = copy.deepcopy(a)
# b[3].append(200)
# print(a)

# qwe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for line in qwe:
#     for number in line:
#         print(number)
# print(qwe[1][2])

# name = input('Name')
# print(name or 'Гость')

# age = input('Age')
# print('Welcome' if int(age) >= 18 else 'No Access')

# def admin():
#     print('I am admin')
# login = input('login ')
# admin() if login == 'admin' else print('Hello user')

# от -5  до 256
# a = 257
# b = 257
# print(id(a), id(b), a is b)

# result = []
# for i in range(10):
#     result.append(i)
# print(result)

# result1 = [i for i in range(-10, 10) if i % 2 == 0]
# print(result1)

# keys = 'qwerty'
# values = (1,2,3,4,5,6)
# my_dict = {key: value*2 for key, value in zip(keys, values)}
# print(my_dict)



# a = [1, 2]
# try:
#     a[5]
# except IndexError:
#     print('проверь индекс')
# print(1)

# try:
#     age = int(input('Age: '))
# except ValueError:
#     print('Вы должны ввести цифры')

# def get_user_data():
#     try:
#         age = int(input('Age: '))
#     except ValueError:
#         print('деление на ноль!')
#
# get_user_data()
# print(1)

import re
text = 'dfs df sdf   alex@mail.comhgfjfg kjhkljh alex@mail.com ;lk ;lk alex@mail.com'
pattern = '([a-zA-Z_0-9]+@[a-z]+\.[a-z]{2,3})'

# print(re.match(pattern, text))
print(re.findall(pattern, text))