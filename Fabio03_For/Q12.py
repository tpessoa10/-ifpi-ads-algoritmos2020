def main():

    n = int(input('Digite a quantidade de números na sua lista: '))
    cont = 0

    for i in range(n):
        num = int(input('Quais números você deseja adicionar: '))
        cont = cont + num

    media = cont / n

    print('A soma dos números é {}'.format(cont))
    print('A media dos números é {}'.format(media))



main()

