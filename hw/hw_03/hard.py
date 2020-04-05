# -*- coding: utf-8 -*-
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5

# вычислите и выведите y
split_result = equation.split()
number_with_x = float(split_result[2].replace('x', '')) * x

# Так как условием четко прописано сложение, то другие варианты здесь не учитываем,
# но это не сложно (добавляется несколько условий).
y = number_with_x + float(split_result[4])
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

########

days_count_by_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = input('Введите дату:')
day, month, year = date.split('.')

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if 0 < int(month) <= 12 \
            and 0 < int(year) <= 9999 \
            and 0 < int(day) <= days_count_by_month[int(month)]:
        print('Дата корректна')
    else:
        print('Дата некорректна')
else:
    print('Длина одной из частей даты некорректна')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room_for_search = int(input('Номер искомой комнаты: '))

block = 1
first_room = 1
stage = 1

while room_for_search >= first_room + block ** 2:
    first_room = first_room + block ** 2
    stage += block
    block += 1

stage += ((room_for_search - first_room) // block)
room_sequence = int((room_for_search - first_room) % block + 1)

print(stage, room_sequence)
