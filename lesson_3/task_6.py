def int_func(word):
    """
    Принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой, либо None
    """
    for i in word:
        if ord(i) not in range(97, 122 + 1):
            return None
    else:
        return chr(ord(word[0]) - 32) + word[1:]


words_orig = input('Введите строку из слов из латинских букв в нижнем регистре, разделенных пробелом: ').split()
words_res = [int_func(i) for i in words_orig]
if None in words_res:
    print('Некорректный ввод')
else:
    print(' '.join(words_res))
