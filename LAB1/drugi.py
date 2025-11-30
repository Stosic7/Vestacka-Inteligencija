def numlista(lista):
    tipovi = {type(x) for x in lista}
    return {tip.__name__: [x for x in lista if type(x) == tip] for tip in tipovi}

print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))
