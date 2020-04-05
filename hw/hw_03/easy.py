# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
# Без key=len будет переводить в ASCII
right_offset = len(max(fruits, key=len))

# https://lancelote.gitbooks.io/intermediate-python/content/book/enumerate.html
for index, item in enumerate(fruits, start=1):
    # print('{}. {:>{}}'.format(index, item, right_offset)) # второй способ
    print('{}. {}'.format(index, item.rjust(right_offset)))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_a = [1, 2, 3, 4, 4, 5, 6]
list_b = [3, 4, 5, 6, 7, 8]

for b in list_b:
    while b in list_a:
        list_a.remove(b)

print(list_a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1, 5, 7, 9, 5, 3, 4, 6, 8, 54, 3453, 7, 345, 7, 4, 3]
print(a)

new_a = []

for val in a:
    if val % 2 == 0:
        new_a.append(val / 4)
    else:
        new_a.append(val * 2)

print(new_a)
