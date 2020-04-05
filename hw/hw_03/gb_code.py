# print(max(1, 2, 3, 4, 5))
# print(max('zz', 'aaa', key=len))
# print(round(1.444444444, 2))
# for index, char in enumerate(['q', 'w', 'z'], start=1):
#     print(index, char)

# def say_hello():
#     print('Hello')
#
# say_hello()
#
#
# def say_hello_to(name):
#     print('Hello', name)
#
# say_hello_to('Oleg')


# def average(numbers):
#     count = len(numbers)
#     my_summ = 0
#     for num in numbers:
#         my_summ += num
#     return my_summ / count
#
#
# result = average([1, 2, 3, 4, 5])
# print(result)

x = 100


# def test():
#     global x # ПЛОХО!!!!
#     x = 99

# def test(x):
#     x += 1
#     return x
#
# x = test(x)
# print(x)


# def render_person(name, surname=''):
#     print(name, surname)
#
#
# render_person('иван')
# render_person('иван', 'петров')

# def render_person(name, *args):
#     print(name)
#     print(args)
#     for arg in args:
#         print(arg)
#
#
# data = [10, 100.100]
# render_person('Ivan', *data)

# def render_person(name, **kwargs):
#     print(name, kwargs)
#
# data = {'surname': 'Petrov', 'age': 20}
# render_person('Ivan', **data, date='today')

# x = 10
# names = ['Alex', 'Igor', 'Alice', x]
# numbers = [100, 200, 300, 400]
#
# print(list(zip(names, numbers)))
# print(dict(zip(names, numbers)))

# def my_pow(x):
#     return x ** 2
#
#
# def my_filter(x):
#     return x > 0
#
#
# data = [-2, -10, 5, 19]
#
# result = []
# for num in data:
#     result.append(my_pow(num))
# print(result)
#
# result = list(map(lambda x: x ** 2, data))
# result = list(filter(lambda x: x > 0, data))
# print(result)


# file = open('1.txt')
#
# for line in file:
#     print(line, end='')
#
# file.close()

# file = open('999.txt', 'a+', encoding='utf-8')
# file.write('1\n')
# # file.seek(0)
# print(file.readline())
# file.close()

# with open('999.txt') as file:
#     for line in file:
#         print(line)

# ДЗ ОТ МЕНЯ!!!!
