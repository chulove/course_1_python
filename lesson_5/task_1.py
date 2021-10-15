print('Для записи текса в файл введите его ниже. Для завершения ввода нажмите дважды Enter')
f = open('task_1.txt', 'w', encoding='utf-8')
while True:
    line = input()
    f.write(line + '\n')
    if line == '':
        break
f.close()
