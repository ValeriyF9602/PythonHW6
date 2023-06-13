'''
Задача 30

Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
a(n) = a(1) + (n-1) * d. Каждое число вводится с новой строки.

    Ввод: 7 2 5
    Вывод: 7 9 11 13 15
'''


def read_int(text):

    value = int(input(text))
    return value


def fill_arithmetic_progression(length, initial_term, difference):

    arith_list = list()

    for i in range(length):
        arith_list.append(initial_term + i * difference)
    
    return arith_list


a_1 = read_int('Укажите первый элемент арифметической прогрессии: ')
d = read_int('Укажите разность арифметической прогрессии: ')
size = read_int('Укажите количество элементов в арифметической прогрессии: ')

print(fill_arithmetic_progression(size, a_1, d))