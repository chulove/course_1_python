while True:
    try:
        orig_list = [int(el) for el in input('Введите исходный список чисел через пробел: ').split()]
        break
    except:
        print('Некорректный ввод! Необходимо ввести числа')

if len(orig_list) > 1:
    res_list = [orig_list[i] for i in range(1, len(orig_list)) if orig_list[i] > orig_list[i - 1]]
else:
    res_list = []

print(res_list)
