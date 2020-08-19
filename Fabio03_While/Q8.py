n = int(input('Digite um número: '))
limite_inferior = int(input('Digite o limite inferior: '))
limite_superior = int(input('Digite o limite superior: '))
c = limite_inferior

while c <= limite_superior:
    if c % n == 0:
        print(c)

        c = c + 1



        