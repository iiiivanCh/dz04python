# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

then = int(input("Введите число для заданной точности числа Пи: "))
print(f'число Пи с заданной точностью {then} равно {round(pi, then)}')


# Используем формулу Лейбница
def correct_pi(correct):
    total, denominator = 0, 1
    for i in range(10**then):
        if i % 2 == 0:
            total += 4 / denominator
        else:
            total -= 4 / denominator
        denominator += 2
    return total


user_pi = correct_pi(then)
print(f'{user_pi} отклонение: {pi - user_pi}')
