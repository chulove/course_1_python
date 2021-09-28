access_list = {"Гость":"0000"}

print('Добро пожаловать!')
menu_text = '''
Вы хотите:
(1) Войти
(2) Зарегистрироваться
(q) Закрыть окно
'''

main_loop = True
while main_loop:
    key = input(menu_text)
    if (key == '1'):
        attemp = 1
        while True:
            name = input("Введите имя пользователя: ")
            if name in access_list.keys():
                access = False
                i = 0
                while access == False and i<3:
                    if i>0:
                        print('Неверный пароль!')
                    password = input('Введите пароль: ')
                    if access_list[name] == password:
                        access = True
                        main_loop = False
                        print('Доступ предоставлен')
                    else:
                        i += 1
                if access == False:
                    print('Превышено количество попыток. В доступе отказано!')
                break
            elif attemp < 3:
                print('Ползователь не найден. Проверьте правильность написания')
                attemp += 1
            else:
                print('Превышено количество попыток. В доступе отказано!')
                break
    elif (key == '2'):
        name = input("Введите имя пользователя: ")
        while True:
            password1 = input('Введите пароль: ')
            password2 = input('Повторите пароль: ')
            if password1 == password2:
                access_list[name] = password1
                print('Вы успешно зарегистрировались!')
                break
            else:
                print('Пароли не совпадают!')
    elif (key == 'q'):
        main_loop = False
        print('До свидания!')
    else:
        print('Введите корректный ответ')
