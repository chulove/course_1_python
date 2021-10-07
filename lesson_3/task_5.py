res = 0
while True:
    line = input('Введите строку чисел, разделенных пробелом (либо q для завершения): ').split()
    try:
        res += sum([float(i) for i in line])
        print(f'Сумма введенных чисел равна {res}')
    except:
        if len(line) == 1 and line[0] == 'q':
            break
        elif len(line) > 1 and line[-1] == 'q':
            try:
                res += sum([float(i) for i in line[:-1]])
                print(f'Сумма введенных чисел равна {res}')
                break
            except:
                print('Некорректный ввод')
        else:
            print('Некорректный ввод')
