def main ():
    n1 = int(input('Digite o primeiro ângulo do triangulo: '))
    n2 = int(input('Digite o segundo ângulo do triangulo: '))
    n3 = int(input('Digite o terceiro ângulo do triangulo: '))

    qual_triangulo(n1, n2, n3)

def qual_triangulo(n1, n2, n3):
    if n1 + n2 + n3 == 180:
        if n1 < 90 and n2 < 90 and n3 < 90:
            print('Triângulo acutângulo')
        elif n1 == 90 or n2 == 90 or n3 == 90:
            print('Triângulo retângulo')
        elif n1 > 90 or n2 > 90 or n3 > 90:
            print('Triângulo obtusângulo')
        if n1 == 0 or n2 == 0 or n3 == 0:
            print('Não existe triângulo com grau zero')


main()

