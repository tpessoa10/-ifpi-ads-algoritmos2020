def main():
    n = float(input('Digite um número: '))

    decimal_inteiro(n)


def decimal_inteiro(n):
    inteiro = n // 1 

    if n == inteiro:
        print(f'{n} é inteiro')
    else:
        print(f'{n} é decimal')
    


main()

