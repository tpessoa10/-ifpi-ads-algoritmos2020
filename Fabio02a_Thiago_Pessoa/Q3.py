def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite mais um número: '))
    n3 = int(input('Digite mais um outro número: '))


    if n1 > n2 > n3:
        print(f'{n1} é o maior número')
    elif n1 > n3 > n2:
        print(f'{n1} é o maior número')
    elif n2 > n1 > n3:
        print(f'{n2} é o maior número')
    elif n2 > n3 > n1:
        print(f'{n2} é o maior número')
    elif n3 > n1 > n2:
        print(f'{n3} é o maior número')
    elif n3 > n2 > n1:
        print(f'{n3} é o maior número')
    elif n1 == n2 < n3:
        print(f'{n3} é o maior número')
    elif n1 > n2 == n3:
        print(f'{n1} é o maior número')
    elif n2 > n1 == n3:
        print(f'{n2} é o maior número')
    else:
        print('Todos iguais')


main()

