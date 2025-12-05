def izdvoji(*args):
    return [podlista[i] if i < len(podlista) else 0 for i, podlista in enumerate(args)]

print(izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]))
