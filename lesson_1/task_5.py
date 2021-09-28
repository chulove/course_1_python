income = float(input("Укажите совокупный доход компании (руб.): "))
costs = float(input("Укажите общие издержки компании (руб.): "))

if income >= costs:
    print(f'Прибыль компании составила: {income - costs:.2f} руб.')
    print(f'Рентабельность: {(income - costs)/income*100:.2f} %')
    employees = int(input('Укажите численность сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника: {(income - costs) / employees:.2f} руб.')
else:
    print(f'Убытки компании составили: {costs - income:.2f} руб.')
