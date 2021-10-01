while True:
    list_len = input('Введите размер массива: ')
    try:
        orig_arr = []
        for i in range(int(list_len) - 1):  # для того, чтобы ввод 0 тоже приводил к ошибке
            orig_arr.append(input(f'Введите {i + 1}-й элемент массива: '))
        orig_arr.append(input(f'Введите {i + 2}-й элемент массива: '))
        break
    except:
        print('Необходимо ввести натуральное число')

for i in range(1, len(orig_arr), 2):
    orig_arr[i - 1], orig_arr[i] = orig_arr[i], orig_arr[i - 1]

print('Результат:', orig_arr)
