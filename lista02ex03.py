lista = [2,3,5,6,1,10,123,2315,513]

def somalista(lista):
    if len(lista) == 0:
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + somalista(lista[1:])
    else:
        return somalista(lista[1:])

print(somalista(lista))