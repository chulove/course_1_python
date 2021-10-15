from random import randint

f = open('result_5.txt', 'w', encoding='utf-8')
f.write(' '.join([str(randint(0, 100)) for i in range(20)]))
f.close()

# правильнее сделать без повторного открытия файла, но в условии "подсчитывать сумму чисел в файле"
f = open('result_5.txt', 'r', encoding='utf-8')
print(sum([int(el) for el in f.read().split()]))
f.close()
