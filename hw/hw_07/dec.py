# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self._age = age
#         self.sex = sex
#
#     @property
#     def age(self):
#         # проверки возраста
#         return self._age
#
# # очень много кода, который использует все аттрибуты класса
#
# human = Human('Vagan', 35, 'м')
# print(human.name)
# print(human.age)
# print(human.sex)


# class DataBaseConnection:
#
#     @staticmethod
#     def connect():
#         print('connecting')
#
#     @staticmethod
#     def select():
#         print('selecting')
#
#     @staticmethod
#     def insert():
#         print('inserting')
#
# DataBaseConnection.connect()
# DataBaseConnection.select()

# db = DataBaseConnection()
# db.select()
# db.connect()

class MyDict(dict):
    def __setitem__(self, key, value):
        print('Пытаюсь добавить по ключу',key,'значение', value)
        super().__setitem__(key, value)

    def __getitem__(self, item):
        print('Работаю, вывожу на экран по ключу', item)
        return super().__getitem__(item)


my_dict = MyDict()
my_dict['name'] = 'qwerty'
a = my_dict['name']
print(a)