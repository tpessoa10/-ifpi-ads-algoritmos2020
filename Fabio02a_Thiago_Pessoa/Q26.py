def main():
    lado1 = int(input('Digite o tamanho do lado 1: '))
    lado2 = int(input('Digite o tamanho do lado 2: '))
    lado3 = int(input('Digite o tamanho do lado 3: '))

    lados(lado1, lado2, lado3)


def lados(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
        if lado1 > lado2 and lado3:
            print('O primeiro lado é a hipotenusa, o segundo e terceiro lado são catetos')
        elif lado2 > lado1 and lado3:
            print('O segundo lado é a hipotenusa, o primeiro e terceiro lado são catetos')
        elif lado3 > lado1 and lado2:
            print('O terceiro lado é a hipotenusa, o primeiro e segundo lado são catetos')
    else:
        print('Não forma triângulo')        


main()

