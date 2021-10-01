res_list = [None, True, 10, 10.0, 10 + 1j, 'abc', (1, 'a'), [[1, 2], 2, (1,)], {'a', 23.4, False},
            {'abc': "ssss", 21: 7j, -1: ('re',)}]

for i in res_list:
    print(type(i))
