limite_inferior = int(input('Digite o limite inferior: '))
limite_superior = int(input('Digite o limite superior: '))
c = limite_inferior

while c <= limite_superior:
    if c % 2 == 0 and c % 3 == 0 and c % 5 == 0 and c % 7 == 0 and c % 11 == 0:
        print(c)
    c = c + 1