def main():

    n = int(input('Quantos números terá na sua lista: '))
    maior = menor = 0

    for i in range(n):
        num = int(input('Quais números deseja adicionar: '))
        if i == 1:
            menor = maior = num
        elif i > 1:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

    print('O maior número é {}'.format(maior))
    print('O menor número é {}'.format(menor))


main()

