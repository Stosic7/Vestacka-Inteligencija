from itertools import zip_longest
from itertools import pairwise
from itertools import groupby
from functools import reduce

def poredak(lista1, lista2):
    return [(x, y, 'Jeste' if y == 2 * x else 'Nije') for x, y in zip_longest(lista1, lista2, fillvalue=0)]

def spojidict(lista1, lista2):
    return [{'prvi': x, 'drugi': y} for x, y in zip_longest(lista1, lista2, fillvalue='-')]

def spoji(lista1, lista2):
     return [(min(x, y), max(x, y), x + y) for x, y in zip_longest(lista1, lista2, fillvalue=0)]

def suma(lista):
     return reduce(lambda x, y: x + y, [i for podlista in lista for i in podlista])

def proizvod(A, B):
    return list(map(lambda podlista, b: reduce(lambda x, y: x + y, [elem * b for elem in podlista]), A, B))

def objedini1(lista1, lista2):
    return list(((min(x,y), max(x,y)) for x,y in zip_longest(lista1, lista2, fillvalue = 0)))

def objedini2(lista):
    return {i[0]: list(i[1:]) if len(i) > 1 else None for i in lista}

def izracunaj1(lista):
    return [reduce(lambda x, y: x * y, elem) if isinstance(elem, list) else elem for elem in lista]

def zamena(lista, x):
    return [reduce(lambda a, b: a + b, lista[i+1:]) if elem < x else elem for i, elem in enumerate(lista)]

def stepen(lista):
    return list(x**y for x,y in pairwise(lista))

def proizvod(lista):
     return reduce(lambda x, y: x * y, [i for podlista in lista for i in podlista])

def izracunaj2(lista):
   return [reduce(lambda a, b: a + b, [x**2 for x in elem]) if isinstance(elem, list) else elem**2 for elem in lista]

def skupi(lista):
    return [[x + y for x, y in zip_longest(p1, p2, fillvalue=0)] for p1, p2 in pairwise(lista)]

def suma2(lista):
    return reduce(lambda x, y: x + y, [reduce(lambda a, b: a * b, podlista) for podlista in lista])

def promeni(lista, x):
    return list(elem - x if elem >= x else elem + x for elem in lista)

def broj(hex_boja):
    return int(hex_boja[1:], 16)

def tekst(string):
    return ''.join([f'\\u{hex(ord(c))[2:].zfill(4)}' if not ((65 <= ord(c) <= 90) or (97 <= ord(c) <= 122) or (48 <= ord(c) <= 57)) else c for c in string])

def brojanje(string):
    return len([k for k, g in groupby(string) if len(list(g)) > 1])

def izracunaj(lista, func):
    return [func(x, y, z) for x, y, z in zip(lista, lista[1:], lista[2:])]
