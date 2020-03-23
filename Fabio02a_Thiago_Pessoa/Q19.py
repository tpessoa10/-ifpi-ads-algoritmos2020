def main():
    altura = float(input('Digite sua altura em metros: '))
    peso = float(input('Digite seu peso em KG: '))

    imc = peso / altura ** 2

    qual_imc(imc)

def qual_imc(imc):
    if imc < 25:
        print('Peso normal')
    elif imc >= 25 and imc <= 30:
        print('Obesidade')
    elif imc > 30:
        print('Obesidade mórbida')


main()


