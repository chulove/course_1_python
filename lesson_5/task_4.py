# Необходимо установить модуль googletrans (pip install googletrans==4.0.0-rc1)
from googletrans import Translator

translator = Translator()

lines = []
f = open('task_4.txt', 'r', encoding='utf-8')
for line in f:
    lines.append(translator.translate(line[:line.find(' ')], dest='ru').text + line[line.find(' '):])
f.close()

f = open('result_4.txt', 'w', encoding='utf-8')
f.writelines(lines)
f.close()
