lista = [1,2,3,4,5,6,7,8,10]
def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])

print(soma(lista))