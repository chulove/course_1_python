import re

f = open('task_2.txt', 'r', encoding='utf-8')
lines = f.readlines()
print('Количество строк в файле:', len(lines))
for i, line in enumerate(lines):
    print(f'Количество слов в {i + 1}й строке:', len(list(filter(lambda x: re.search('\w', x), line.split()))))
f.close()
