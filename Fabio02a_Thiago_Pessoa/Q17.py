def main():
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))

    if n1 % n2 == 1:
        print(f'{n1} + {n2} + {1} = {n1 + n2 + 1}')
    elif n1 % n2 == 2:
        if n1 % 2 == 0:
            print(f'{n1} é par')
        elif n1 % 2 != 0:
            print(f'{n1} é impar')
        if n2 % 2 == 0:
            print(f'{n2} é par')
        elif n2 % 2 != 0:
            print(f'{n2} é impar')
    elif n1 % n2 == 3:
        multi = (n1 + n2) * n1 
        print(f'A multiplicação é {multi}')
    elif n1 % n2 == 4:
        div = (n1 + n2) / n2
        print(f'A divisao é {div}') 
    elif n1 % n2 >= 5:
        print(f'Quadrado de {n1} é {n1**2}')
        print(f'Quadrado de {n2} é {n2**2}')
        
    
main()

