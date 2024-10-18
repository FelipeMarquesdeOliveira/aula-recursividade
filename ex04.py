lista = [1,2,3,4,5,6,7,8,1,2,3,4,5,3,4,5,1,1]
item = 10

def busca(lista, item):
    if len(lista) == 0:
        return False
    else:
        if lista[0] == item:
            return True
        else:
            return busca(lista[1:], item)

print(busca(lista,item))