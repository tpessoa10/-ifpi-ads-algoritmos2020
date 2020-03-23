def main():
    angulo = int(input('Digite a medida de um ângulo: '))

    qual_quadrante(angulo)

def qual_quadrante(angulo):
    if angulo > 0 and angulo <= 90:
        print('Primeiro quadrante')
    elif angulo > 90 and angulo <= 180:
        print('Segundo quadrante')
    elif angulo > 180 and angulo <= 270:
        print('Terceiro quadrante')
    elif angulo > 270 and angulo <= 360:
        print('Quarto quadrante')
    elif angulo > 360:
        resto = angulo % 360
        if resto > 0 and resto <= 90:
            print('Primeiro quadrante')
        elif resto > 90 and resto <= 180:
            print('Segundo quadrante')
        elif resto > 180 and resto <= 270:
            print('Terceiro quadrante')
        elif resto > 270 and resto <= 360:
            print('Quarto quadrante')

    
main()

