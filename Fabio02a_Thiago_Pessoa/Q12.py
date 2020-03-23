def main():
    num = int(input('Digite um número: '))

    impar_par(num)


def impar_par(num):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')


main()

