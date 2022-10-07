# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


import math


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            if num > 1:
                return num
            else:
                print('Введенное число меньше или равно 1. Повторите ввод')
        except ValueError:
            print("Вы ввели не натуральное число. Повторите ввод")


def get_checking_natural_number(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_list_prime_factors_number(number):
    list_prime_factors_number = []
    multiplier = 1
    while not multiplier == number:
        print(multiplier, number)
        multiplier += 1
        if get_checking_natural_number(multiplier):
            if number % multiplier == 0:
                list_prime_factors_number.append(multiplier)
                number /= multiplier
                multiplier = 1
    return list_prime_factors_number


user_number = get_user_number('Введите натуральное число: ')
user_list = get_list_prime_factors_number(user_number)
print(f"{user_list} => {math.prod(user_list)} (Проверка)")
