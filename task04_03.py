# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


import random


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            if num >= 0:
                return num
            else:
                print('Введенное число меньше 0. Повторите ввод')
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_user_random_list(arr_len):
    arr_list = []
    for i in range(arr_len):
        arr_list.append(random.randint(0, 20))
    return arr_list


def convert_list_set(u_list):
    return set(u_list)


def convert_set_list(u_set):
    return list(u_set)


user_len = get_user_number('Задайте длину списка (массива): ')
user_list = get_user_random_list(user_len)
user_set = convert_list_set(user_list)
total_list = convert_set_list(user_set)
print(user_list, total_list, user_set, sep='\n')
