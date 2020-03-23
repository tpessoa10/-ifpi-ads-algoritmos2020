def main():
    n = int(input('Digite um número entre 0 e 100: '))

    numero_primo(n)

def numero_primo(n):
    if  n >= 0 and n <= 100:
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
            print('Número primo')
        else:
            print('Não é número primo')
    else:
        print('Nescessário um número entre 0 e 100')


main()

