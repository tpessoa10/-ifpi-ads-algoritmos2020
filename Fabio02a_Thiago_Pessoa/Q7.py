def main():
    lado_1 = int(input('Digite o primeiro lado do triângulo: '))
    lado_2 = int(input('Digite o segundo lado do triângulo: '))
    lado_3 = int(input('Digite o terceiro lado do triângulo: '))

    triangulo(lado_1, lado_2, lado_3)


def triangulo(lado_1, lado_2, lado_3):
    if lado_1 + lado_2 < lado_3 or lado_1 + lado_3 < lado_2 or lado_2 + lado_3 < lado_1:
        print('Não forma triângulo')
    elif lado_1 + lado_2 > lado_3 or lado_1 + lado_3 > lado_2 or lado_2 + lado_3 > lado_1:
        if lado_1 == lado_2 == lado_3:
            print('Triângulo equilátero')
        elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            print('Triângulo isósceles')
        elif lado_1 != lado_3 and lado_1 != lado_2 and lado_2 != lado_3:
            print('Triângulo escaleno')
        elif lado_1 == 0 or lado_2 == 0 or lado_3 == 0:
            print('Não forma triângulo')
    

main()

