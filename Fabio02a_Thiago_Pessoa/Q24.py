def main():
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))

    raiz(a, b, c)


def raiz(a, b, c):
    delta = (b**2) - (4 * a * c)
    if a == 0:
        print('A não poder ser zero')
    elif delta > 0:
        raiz_1 = (-b) + (delta**(1/2)) // (2*a)
        raiz_2 = (-b) - (delta**(1/2)) // (2*a)
        print(f'A primeira raiz é {raiz_1}')
        print(f'A segunda raiz é {raiz_2}')
    elif delta == 0:
        raiz_1 = (-b) + (delta**(1/2)) // (2*a)
        print(f'A raiz é {raiz_1}')
    else:
        print('Não forma números reais')


main()

