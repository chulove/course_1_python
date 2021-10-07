def my_func(num_1, num_2, num_3):
    """
    Возвращает сумму наибольших двух аргументов
    """
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)


while True:
    abc = input('Введите три числа через пробел: ')
    try:
        a, b, c = abc.split()
        print(f'Сумма наибольших двух чисел равна {my_func(num_1=float(a), num_2=float(b), num_3=float(c))}')
        break
    except:
        print('Некорректный ввод')
