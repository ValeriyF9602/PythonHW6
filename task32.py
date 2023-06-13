'''
Задача 32

Определить индексы элементов массива (списка), значения которых принадлежат заданному 
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

    Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    Вывод: [1, 9, 13, 14, 19]
'''


from random import randint



def generate_list(length, left_range = -10, right_range = 10):

    list_1 = list()

    for i in range(length):
        list_1.append(randint(left_range, right_range))
    
    return list_1


def indexes_in_range(list_1, left_range, right_range):
    
    indexes = list()
    
    for i in range(len(list_1)):
        if list_1[i] >= left_range and list_1[i] <= right_range:
            indexes.append(i)
    
    return indexes


def read_int(text):

    value = int(input(text))
    return value



size = read_int('Укажите размер массива: ')
min_of_range = read_int('Укажите левую границу диапазона: ')
max_of_range = read_int('Укажите правую границу диапазона: ')

orig_list = generate_list(size)

print(orig_list)

print(indexes_in_range(orig_list, min_of_range, max_of_range))