text = input('Введите строку: ')
words = text.split()
for i, el in enumerate(words):
    print(f'{i}: {el[:min(len(el), 10)]}')
