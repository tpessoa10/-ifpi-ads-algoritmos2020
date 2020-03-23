def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))


    if n1 > n2 > n3 > n4 > n5:
        print(f'Maior número é {n1} e o menor é {n5}')
    elif n2 > n1 > n3 > n4 > n5:
        print(f'Maior número é {n2} e o menor é {n5}')
    elif n3 > n1 > n2 > n4 > n5:
        print(f'Maior número é {n3} e o menor é {n5}')
    elif n4 > n1 > n2 > n3 > n5:
        print(f'Maior múmero é {n4} e o menor é {n5}')
    elif n5 > n1 > n2 > n3 > n4:
        print(f'Maior número é {n5} e o menor é {n4}')
    elif n3 > n1 > n2 > n5 > n4:
        print(f'Maior número é {n5} e o menor é {n4}')
    elif n2 > n1 > n3 > n5 > n4:
        print(f'Maior número é {n2} e o menor é {n4}')
    elif n1 > n2 > n3 > n5 > n4:
        print(f'Maior número é {n1} e o menor é {n4}')
    elif n1 > n2 > n4 > n5 > n3:
        print(f'Maior número é {n1} e o menor é {n3}')
    elif n2 > n1 > n4 > n5 > n3:
        print(f'Maior número é {n2} e o menor é {n3}')
    elif n4 > n1 > n2 > n5 > n3:
        print(f'Maior número é {n4} e o menor é {n3}')
    elif n5 > n1 > n2 > n4 > n3:
        print(f'Maior número é {n4} e o menor é {n3}')
    elif n1 > n3 > n4 > n5 > n2:
        print(f'Maior número é {n1} e o menor é {n2}')
    elif n3 > n1 > n4 > n5 > n2:
        print(f'Maior número é {n3} e o menor é {n2}')
    elif n4 > n1 > n3 > n5 > n2:
        print(f'Maior número é {n4} e o menor é {n2}')
    elif n5 > n1 > n3 > n4 > n2:
        print(f'Maior número é {n5} e o menor é {n2}')
    elif n2 > n3 > n4 > n5 > n1:
        print(f'Maior número é {n2} e o menor é {n1}')
    elif n3 > n2 > n4 > n5 > n1:
        print(f'Maior número é {n3} e o menor é {n1}')
    elif n4 > n2 > n3 > n5 > n1:
        print(f'Maior número é {n4} e o menor é {n1}')
    elif n5 > n2 > n3 > n4 > n1:
        print(f'Maior número é {n5} e o menor é {n1}')
    elif n5 > n4 > n3 > n2 > n1:
        print(f'Maior número é {n5} e o menor é {n1}')
    

main()

