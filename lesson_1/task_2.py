seconds = input('Введите время в секундах: ')
hh = int(seconds) // 3600
mm = (int(seconds) % 3600) // 60
ss = int(seconds) % 60

print(f'Время в формате чч:мм:сс: {hh:02}:{mm:02}:{ss:02}')
