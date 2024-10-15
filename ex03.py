a = int(input('Numero(A): '))
b = int(input('Numero(B): '))

def raiz(a,b):
    if b == 1:
        return 1
    else:
        return a * raiz(a, b - 1)

print(f"O resultado de {a}^{b} é: {(raiz(a,b))}")