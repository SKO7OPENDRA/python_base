# Модули

# import my_game_lib as lib
# # from my_game_lib import pow
# # from my_game_lib import *
#
#
# print(lib.pow(5, 5))
# print(pow(5, 5))

# import sys
# for path in sys.path:
#     print(path)

import os
# print(os.getcwd())
# os.remove()
# os.system()
# os.mkdir('test')
# print(os.listdir())

import sys
print(sys.argv)
if 'help' in sys.argv:
    print('Большое описание программы')
if 'qwe'in sys.argv:
    print('Реакция на qwe')

