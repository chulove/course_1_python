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


def division(dividend, divisor):
    """
    Возвращает частное от деления параметров
    :param dividend: делимое
    :param divisor: делитель
    :return: частное (либо None, если делитель = 0)
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return None


a = input_num('Введите делимое: ')
b = input_num('Введите делитель: ')
if division(a, b) == None:
    print('Ошибка! Деление на 0 невозможно')
else:
    print('Частное равно', division(a, b))
