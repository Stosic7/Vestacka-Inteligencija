from collections import Counter

def brojanje(recnik):
    tipovi = [type(v).__name__ for v in recnik.values()]
    return list(Counter(tipovi).items())

print(brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}))
