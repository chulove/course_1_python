my_list = [7, 5, 3, 3, 2]
print('Исходный набор: ', my_list)

while True:
    new_num = input('Введите любое натуральное число (либо q для выхода): ')
    try:
        if new_num == 'q':
            break
        if int(new_num) > 0:
            for i in range(len(my_list)):
                if my_list[i] < int(new_num):
                    my_list.insert(i, int(new_num))
                    break
            else:
                my_list.append(int(new_num))
            print('Результат: ', my_list)
        else:
            print('Необходимо ввести натуральное число или q')
    except:
        print('Необходимо ввести натуральное число или q')
