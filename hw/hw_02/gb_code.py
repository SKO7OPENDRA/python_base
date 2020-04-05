# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

# name = 'Анастасия'
# print(name[0])
# print(name[-5])
# print(name[0:5])
# print(name[:5])
# print(name[5:])
# print(name[0:9:2])
# print(name[::2])
# print(name[::-1])


# email = 'welcome@my_site.com'
# index = email.find('@')
# print(email[:index])

# name = 'пЕтРоВ ГеНаДиЙ ИвАновИч'
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.count('о'))
# print(len(name))
#
# email = 'test@test.com'
# print(email.split('@'))
# rjust, ljust

# name = 'Ivan'
# age = 20
# money = 300.23
# # print('Hello', name, 'вам', age, 'лет', str(money) + 'р.')
# result = 'Привет %s вам %i лет, у вас на счету %f р.' % (name, age, money)
# result = 'Привет {} вам {} лет, у вас на счету {} р.'.format(name, age, money)
# result = f'Привет {name} вам {age} лет, у вас на счету {money} р.'
# print(result)


# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html

# name = 'Sergey'
# humans = ['Ivan', 'Alex', 'Olga', name]
# humans[0] = 'Anastasia'
# humans.append(100)
# humans.insert(1, 200)
# humans.remove('Olga')
# humans.pop()
# print(humans.index(name))
# print(humans)
# print(humans[0])
# print(humans[1:])
# print(humans[::2])
# print(humans[::-1])

# humans = ['Ivan', 'Alex', 'Olga']
#
# print('Sergey' in humans)
# x = [1, 2, 3, 4, 5, ['qwe', 'qwewq']]

# admin = ['Ivan', 'Alex', 'Olga']
# admin = ('Ivan', 'Alex', 'Olga')

# humans = ['Ivan', 'Alex', 'Olga', 123123]

# x = 0
# while x < len(humans):
#     print(humans[x])
#     x += 1


# for name in humans:
#     print(name)

# for i in (1, 2, 3, 4, 5):
#     print('Привет')

# for i in range(1, 11):
#     print(f'{i} Привет')

# for _ in range(10):
#     print('Привет')


# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html

# human = {'name': 'Ivan', 'age': 20, 'money': 200.30}
# print(human['name'])
# print(human['age'])
# print(human['money'])
# human['data'] = [1, 2, 3, 4, 5, 6]
# human['age'] = 40
# print(human)
# print(human['data'][-1])

# if human.get('name'):
#     print(human['name'])

# print(human.pop('age'))
# print(human.popitem())


# human = {'name': 'Ivan', 'age': 20, 'money': 200.30}
#
# for key in human.keys():
#     print(key)
#
# print()
#
# for value in human.values():
#     print(value)
#
# print()
#
# for key, value in human.items():
#     print(key, value)

# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

# my_set = {1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5}
# my_set = {'Ivan', 'Olga', 'Ivan', 'Olga'}

# my_set = {1, 2, 3}
# my_set2 = {3, 4, 5}
#
#
# print(my_set | my_set2)
# print(my_set == my_set2)
# print(my_set <= my_set2)
# print(my_set & my_set2)
# print(my_set - my_set2)
# print(my_set ^ my_set2)

# Сдаете все, кроме 3-го задания hard!

'''
asdasd
asda
asda
'''

# 1. Сохраняйте текст задачи
# 2. Не усложняйте
# 3. Сделали ДЗ -> Сделали коммит в отдельной ветке от мастер-> Push -> Pull Request