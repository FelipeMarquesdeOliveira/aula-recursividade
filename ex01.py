n = int(input('Digite um numero inteiro: '))

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)

print(f"O somatório de 1 a {n} é: {soma(n)}")