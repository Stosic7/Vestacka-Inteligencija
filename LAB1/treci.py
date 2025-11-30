def uredi(lista, n, m):
    return [lista[i] + m if i < n else lista[i] - m for i in range(len(lista))]

print(uredi([1, 2, 3, 4, 5], 3, 1))
