def main():
    n = int(input('Digite um número de 2 digitos: '))

    dezena = n // 10
    unidade = n % 10

    if dezena == unidade:
        print('Unidade e dezena são iguais')
    else:
        print('Unidade e dezena são diferentes')


main()

