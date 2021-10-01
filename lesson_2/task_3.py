month_list = ['Зима'] * 2 + ['Весна'] * 3 + ['Лето'] * 3 + ['Осень'] * 3 + ['Зима']
while True:
    month = input('Введите порядковый номер месяца: ')
    try:
        month = int(month)
        if month in range(1, 12 + 1):
            print(f'Это {month_list[int(month) - 1]}')
            break
        else:
            print('Необходимо ввести натуральное число от 1 до 12')
    except:
        print('Необходимо ввести натуральное число от 1 до 12')

month_dict = {}
for i, el in enumerate(month_list):
    month_dict[i + 1] = el
while True:
    month = input('Введите порядковый номер месяца: ')
    try:
        print(f'Это {month_dict[int(month)]}')
        break
    except:
        print('Необходимо ввести натуральное число от 1 до 12')
