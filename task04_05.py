# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов


from numpy import append


def get_file(u_file):
    with open(u_file, 'r', encoding='utf-8') as f:
        return f.readline()


def get_str_list(u_str):
    return u_str.split(' + ')


def get_list_numbers(arr):
    arr_01 = list(s.replace('*x**', ', ') for s in arr)
    arr_02 = list(s.replace('x**', '1, ') for s in arr_01)
    arr_03 = list(s.replace('*x', ', 1') for s in arr_02)
    arr_04 = list(s.replace('x', ', 1') for s in arr_03)
    arr_05 = list(s.replace('\n', '') for s in arr_04)
    arr_new = list(s.split(', ') for s in arr_05)
    arr_new[-1].append('0')
    return arr_new


def get_checking_for_consistency(arr):
    arr_new = [arr[0]]
    for i in range(len(arr) - 1):
        count_arr = 0
        while not (int(arr[i][1]) == int(arr[i + 1][1]) + 1 + count_arr):
            arr_new.append(['0', '0'])
            count_arr += 1
        else:
            arr_new.append(arr[i + 1])
    return arr_new


def get_list_alignment(arr_01, arr_02):
    arr_new_01 = get_checking_for_consistency(arr_01)
    arr_new_02 = get_checking_for_consistency(arr_02)
    if int(arr_new_01[0][1]) > int(arr_new_02[0][1]):
        x = int(arr_new_01[0][1]) - int(arr_new_02[0][1])
        for i in range(x):
            arr_new_02.insert(0, ['0', '0'])
    elif int(arr_new_01[0][1]) < int(arr_new_02[0][1]):
        x = int(arr_new_02[0][1]) - int(arr_new_01[0][1])
        for i in range(x):
            arr_new_01.insert(0, ['0', '0'])
    if int(arr_new_01[-1][1]) == int(arr_new_02[-1][1]):
        return [arr_new_01, arr_new_02]
    elif int(arr_new_01[-1][1]) > int(arr_new_02[-1][1]):
        x = int(arr_new_01[-1][1]) - int(arr_new_02[-1][1])
        for i in range(x):
            arr_new_01.append(['0', '0'])
    elif int(arr_new_01[-1][1]) < int(arr_new_02[-1][1]):
        x = int(arr_new_02[-1][1]) - int(arr_new_01[-1][1])
        for i in range(x):
            arr_new_02.append(['0', '0'])
    return [arr_new_01, arr_new_02]


def get_sum_polynomials(arr):
    arr_01 = arr[0]
    arr_02 = arr[1]
    arr_new = []
    for i in range(len(arr_01)):
        if int(arr_01[i][1]) >= int(arr_02[i][1]):
            x = int(arr_01[i][1])
        else:
            x = int(arr_02[i][1])
        arr_new.append([(int(arr_01[i][0]) + int(arr_02[i][0])), x])
    return arr_new


def get_user_polynomial(arr_list):
    pol = []

    for i in range(len(arr_list)):
        if not (int(arr_list[i][0]) == 0 and int(arr_list[i][1]) == 0):
            if int(arr_list[i][0]) > 1 and int(arr_list[i][1]) > 1:
                pol.append(f'{int(arr_list[i][0])}*x**{int(arr_list[i][1])}')
            elif int(arr_list[i][0]) == 1 and int(arr_list[i][1]) > 1:
                pol.append(f'x**{int(arr_list[i][1])}')
            elif int(arr_list[i][0]) > 1 and int(arr_list[i][1]) == 1:
                pol.append(f'{int(arr_list[i][0])}*x')
            elif int(arr_list[i][0]) == 1 and int(arr_list[i][1]) == 1:
                pol.append('x')
            elif int(arr_list[i][0]) >= 1 and int(arr_list[i][1]) == 0:
                pol.append(f'{int(arr_list[i][0])}')

    str_pol = ' + '.join(pol)
    print(str_pol)
    return str_pol


def get_file_total(u_file, user_str):
    with open(u_file, 'w', encoding='utf-8') as f:
        f.write(user_str)


polynomial_01 = get_file('text1.txt')
polynomial_02 = get_file('text2.txt')
print(polynomial_01, polynomial_02, sep='\n')
polynomial_01 = get_str_list(polynomial_01)
polynomial_02 = get_str_list(polynomial_02)
polynomial_01 = get_list_numbers(polynomial_01)
polynomial_02 = get_list_numbers(polynomial_02)
total = get_list_alignment(polynomial_01, polynomial_02)
total_new = get_sum_polynomials(total)
polynomial_03 = get_user_polynomial(total_new)
get_file_total('text3.txt', polynomial_03)
