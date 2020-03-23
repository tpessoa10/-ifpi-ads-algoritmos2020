def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    num(n1, n2)

def num(n1, n2):
    if n1 > n2:
        print(f'{n1} maior que {n2}')
    elif n2 > n1:
        print(f'{n2} maior que {n1}')
    else:
        print('Números iguais')


main()

