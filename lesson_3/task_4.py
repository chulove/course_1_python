def input_num(text):
    """
    Обеспечивает ввод числа (не строки)
    :param text: Текст приглашения к вводу числа
    :return: Введенное число (float)
    """
    while True:
        a = input(text)
        try:
            return float(a)
        except:
            print('Ошибка! Необходимо ввести число')


def exponentiate_1(base, power):
    """
    Возводит в степень (сделал не только отрицательную)
    :param base: Основание
    :param power: Степень
    """
    if power > 0:
        return base ** power
    elif power == 0:
        return 1.0
    else:
        return 1 / (base ** abs(power))


def exponentiate_2(base, power):
    """
    Возводит в степень (сделал не только отрицательную)
    :param base: Основание
    :param power: Степень
    """
    if power > 0:
        res = base
        for i in range(1, power):
            res = res * base
        return res
    elif power == 0:
        return 1.0
    else:
        res = 1 / base
        for i in range(-1, power, -1):
            res = res / base
        return res


while True:
    a = input_num('Введите действительное положительное число: ')
    if a > 0:
        break
    else:
        print('Ошибка! Необходимо ввести положительное число')
while True:
    b = input_num('Введите целое число: ')
    if int(b) != b:
        print('Ошибка! Необходимо ввести целое число')
    else:
        b = int(b)
        break

print(f'Число {a} в степени {b} равно {exponentiate_1(a, b)} (Метод 1)')
print(f'Число {a} в степени {b} равно {exponentiate_2(a, b)} (Метод 2)')
