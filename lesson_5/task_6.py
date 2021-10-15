import re

with open('task_6.txt', 'r', encoding='utf-8') as f:
    subs = {l[:l.find(':')]: sum([int(el) for el in re.compile('\d+').findall(l[l.find(':'):])]) for l in f}

print(subs)
