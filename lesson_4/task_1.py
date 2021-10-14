from sys import argv

print(argv)
if len(argv) == 4:
    try:
        hours = float(argv[1])
        rate = float(argv[2])
        bonus = float(argv[3])
        salary = hours * rate + bonus
        print(f'Заработная плата сотрудника составит {salary:.2f} рублей')
    except:
        print('Необходимо ввести 3 числовых параметра (выработка в часах / ставка в час / премия)')
else:
    print('Необходимо ввести 3 числовых параметра (выработка в часах / ставка в час / премия)')
