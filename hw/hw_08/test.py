# Эрик и Элизбет Фридмен  "Шаблоны проектирования"

# class WorkerBuilder:
#     def __init__(self, my_dict):
#         for key, value in my_dict.items():
#             setattr(self, key, value)
#
# worker = WorkerBuilder({'name': 'Петр', 'surname': 'Алексеев', 'age': 25})
# print(worker.name)
# print(worker.surname)
# setattr(worker,'x', 10000)
# print(worker.x)

# class Wrapper:
#     def __init__(self, object):
#         self.wrapped = object
#     def __getattr__(self, attrname):
#         print('Working with ', attrname)
#         return getattr(self.wrapped, attrname)
#
# class Test:
#     def __init__(self):
#         self.name = 'qwerty'
#
# test = Test()
# wrapper = Wrapper(test)
#
# print(wrapper.name)

class IncorrectCaseName(Exception):
    def __str__(self):
        return 'name has incorrect name'

def check_name(name):
    if name == name.title():
        print('ok')
    else:
        raise IncorrectCaseName

name = input('Name: ')
try:
    check_name(name)
except IncorrectCaseName:
    print('Вы ввели некорректное имя!')