def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro um número: '))
    n3 = int(input('Digite mais um número: '))

    if n1 > n2 > n3:
        print(f'{n1} > {n2} > {n3}')
    elif n1 > n3 > n2:
        print(f'{n1} > {n3} > {n2}')
    elif n2 > n1 > n3:
        print(f'{n2} > {n1} > {n3}')
    elif n2 > n3 > n1:
        print(f'{n2} > {n3} > {n1}')
    elif n3 > n1 > n2:
        print(f'{n3} > {n1} > {n2}')
    elif n3 > n2 > n1:
        print(f'{n3} > {n2} > {n1}') 
    elif n1 == n2 < n3:
        print(f'{n3} > {n2} = {n1}')
    elif n1 > n2 == n3:
        print(f'{n1} > {n2} = {n3}')
    elif n2 > n1 == n3:
        print(f'{n2} > {n1} = {n3}')
    else:
        print('Todos iguais')


main()
