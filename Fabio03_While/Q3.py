a = int(input('Digite o valor inicial: '))
limite = int(input('Digite o limite: '))
r = int(input('Digite a razão: '))
c = 1

while a < limite:
    a = a + r
    print(a)
    if a > limite:
        break



