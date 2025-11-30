def kreiraj(n):
    return [(i, sum(range(i + 1)) ** 2) for i in range(n + 1)]

print(kreiraj(4))
