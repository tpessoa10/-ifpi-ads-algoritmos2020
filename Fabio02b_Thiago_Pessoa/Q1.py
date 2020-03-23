def main():
    n = int(input('Digite um número: '))

    positivo_negativo(n)

def positivo_negativo(n):
    if n >= 1:
        print('Número positivo')
    elif n <= -1:
        print('Número negativo')
    elif n == 0:
        print('Número neutro')


main()

