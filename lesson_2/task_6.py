products = {}
product = 0
while True:
    action = input('Выберите действие: \n (1) Ввести новый товар \n (2) Вывести итоговую статистику \n (q) Выход \n')
    if action == '1':
        print('Введите информацию о товаре: ')
        product += 1
        products[product] = {}
        products[product]['Название'] = input('Название: ')
        products[product]['Цена'] = input('Цена: ')
        products[product]['Количество'] = input('Количество: ')
        products[product]['Единица измерения'] = input('Единица измерения: ')
    elif action == '2':
        if product == 0:
            print('Нет введенных товаров')
        else:
            for k in products[1].keys():
                print(k, set([v[k] for v in products.values()]))
    elif action == 'q':
        break
    else:
        print('Выберите один из пунктов меню')
