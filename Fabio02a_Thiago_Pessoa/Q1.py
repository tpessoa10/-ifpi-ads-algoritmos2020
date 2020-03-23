def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))


    if n1 == n2 == n3:
        print('Os três números sao iguais')
    elif n1 == n2 != n3:
        print('Dois números iguais')
    elif n1 == n3 != n2:
        print('Dois números iguais')
    elif n2 == n3 != n1:
        print('Dois números iguais')
    else:
        print('Todos os três números sao diferentes')


main()

