from random import random
from statistics import mean
import json

data=[{},{}]
with open('task_7.txt','r',encoding='utf-8') as f:
    for line in f:
        data[0][line.split('\t')[0]] = int(line.split('\t')[2]) - int(line.split('\t')[3])
f.close()
data[1]['average_profit']=list(filter(lambda x: x>=0,data[0].values()))

with open("result_7.json", "w") as f:
    json.dump(data, f)
