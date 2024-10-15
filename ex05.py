lista = [1,2,3,4,5,6,7,8,1,2,3,4,5,3,4,5,1,1]
n = int(input('Numero(N): '))

def quantidade(lista,n):
    if not lista:
        return 0
    if lista[0] == n:
        return 1 + quantidade(lista[1:], n)
    else:
        return quantidade(lista[1:], n)

print(f'A quantidade do numero {n} na lista é: {quantidade(lista,n)}')