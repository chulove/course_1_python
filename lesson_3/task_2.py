import re


def input_format(text, regex):
    """
    Обеспечивает ввод строки определенного формата, задаваемого регулярным выражением
    :param text: Текст приглашения к вводу строки
    :param regex: Регулярное выражение
    :return: Введенная строка
    """
    while True:
        a = input(text)
        if (re.search(regex, a)):
            return a
        else:
            print('Ошибка! Неверный формат ввода')


def format_user_info(name, sname, birth, city, email, tel):
    """
    Реализует вывод данных о пользователе одной строкой определенного формата
    :param name, sname, birth, city, email, tel: входные данные о пользователе
    :return: строка нужного формата
    """
    tel = ''.join(list(filter(lambda s: s.isdigit(), [s for s in tel])))
    return f'{name.title():<15}{sname.title():<20}{birth:<6}{city.title():<20}{email:<25}' + \
           f'+7 ({tel[-10:-7]}) {tel[-7:-4]}-{tel[-4:-2]}-{tel[-2:0]}'


users = []
while True:
    action = input('''Выберите действие:
    (1) Ввести данные нового пользователя
    (2) Вывести данные пользователей
    (q) Выход
    ''')
    if action == '1':
        print('Введите информацию о пользователе: ')
        p1 = input_format('Имя: ', '^[А-Яа-яЁё]{2,15}$')
        p2 = input_format('Фамилия: ', '^[А-Яа-яЁё]{2,20}$')
        p3 = input_format('Год рождения: ', '^(19\d\d|200\d|201\d|2020|2021)$')
        p4 = input_format('Город проживания: ', '^[А-Яа-яЁё0-9\- ]{2,30}$')
        p5 = input_format('email: ', '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$')
        p6 = input_format('Телефон: ', '^((8|\+7)[\- ]?)?\(?\d{3}\)?[\- ]?[\d\- ]{7}$')
        users.append(format_user_info(name=p1, sname=p2, birth=p3, city=p4, email=p5, tel=p6))
    elif action == '2':
        if users:
            for k in users:
                print(k)
        else:
            print('Нет введенных товаров')
    elif action == 'q':
        break
    else:
        print('Выберите один из пунктов меню')
