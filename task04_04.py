# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            if 10 > num > 0:
                return num
            else:
                print('Введенное число меньше или равно 0 или больше 9. Повторите ввод')
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_user_list(degree, start=0, end=100):
    arr_list = []

    for i in range(degree + 1):
        arr_list.append(random.randint(start, end))

    print(arr_list)
    return arr_list


def get_user_polynomial(degree, arr_list):
    pol = []

    for i in range(degree, -1, -1):
        if not arr_list[i] == 0:
            if i == 0 and len(pol) == 0:
                pol = pol
            elif arr_list[i] > 1 and i > 1:
                pol.append(f'{arr_list[i]}*x**{i}')
            elif arr_list[i] == 1 and i > 1:
                pol.append(f'x**{i}')
            elif arr_list[i] > 1 and i == 1:
                pol.append(f'{arr_list[i]}*x')
            elif arr_list[i] == 1 and i == 1:
                pol.append('x')
            elif i == 0:
                pol.append(f'{arr_list[i]}')

    str_pol = ' + '.join(pol)
    print(str_pol)
    return str_pol


def get_file(u_file, user_str):
    with open(u_file, 'w', encoding='utf-8') as f:
        f.write(user_str)


user_degree = get_user_number('Введите натуральное число до 9 включительно: ')
user_list = get_user_list(user_degree)
user_polynomial = get_user_polynomial(user_degree, user_list)
get_file('text1.txt', user_polynomial)
user_degree = get_user_number('Введите натуральное число: ')
user_list = get_user_list(user_degree)
user_polynomial = get_user_polynomial(user_degree, user_list)
get_file('text2.txt', user_polynomial)
