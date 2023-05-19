def permutations(s):
    import itertools
    p=itertools.permutations(s)
    w=[*set(p)]
    listita=[]
    h=""
    for j in w:
        listita.append("".join(j))
    return listita
