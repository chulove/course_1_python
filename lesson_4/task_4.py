from random import randint

orig_list = [randint(1, 30) for i in range(20)]
print(orig_list)

repeated_nums = orig_list[:]
for i in set(repeated_nums):  # set оставляет только уникальные значения
    repeated_nums.remove(i)  # удалив уникальные значения, получим повторяющиеся

print([el for el in orig_list if el not in repeated_nums])
