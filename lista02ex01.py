a = int(input('Numero Inteiro(A): ')) 
b = int(input('Numero Inteiro(b): '))

def multiplicacao(a,b):
    if b == 0:
        return 0
    else:
        return a + multiplicacao(a, b - 1)
        
print(multiplicacao(a,b))