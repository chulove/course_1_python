from itertools import count, cycle
from math import log

cubes = [1]
for el in count(3, 3):
    if el / 3 in cubes:
        cubes.append(el)
    if el >= 9999:
        break
print(cubes)

nums = []
for i in cycle(cubes):
    nums.append(round(log(i, 3)))
    if len(nums) == 20:
        break
print(nums)
