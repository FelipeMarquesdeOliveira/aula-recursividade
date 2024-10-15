n = int(input('Qual fatorial você deseja saber: '))
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(n))