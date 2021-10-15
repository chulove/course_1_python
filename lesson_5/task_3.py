from statistics import mean

f = open('task_3.txt', 'r', encoding='utf-8')
lines = f.readlines()
salary = {line.split('\t')[0]: float(line.split('\t')[1][:-1]) for line in lines}
print('Сотрудники с окладом менее 20 т.р.:\n' + '\n'.join([k for k, v in salary.items() if v < 20000]))
print(f'Средняя величина оклада: {mean(salary.values()):.2f}')
