def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    yield f


for n in range(1, 10000):
    print(*fact(n))
