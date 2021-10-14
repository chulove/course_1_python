from random import randrange
from functools import reduce

orig_list = [randrange(100, 1000 + 1, 2) for i in range(20)]
print(orig_list)
print(reduce(lambda x, y: x * y, orig_list))
