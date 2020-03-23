def main():
    opcao = int(input('Escolha sua opção(1/2/3): '))
    num1 = int(input('Digite o número 1: '))
    num2 = int(input('Digite o número 2: '))
    num3 = int(input('Digite o número 3: '))

    qual_opcao(opcao, num1, num2, num3)


def qual_opcao(opcao, num1, num2, num3):
    if opcao == 1:
        print(f'O número na opção 1 é {num1}')
    elif opcao == 2:
        print(f'O número na opçao 2 é {num2}')
    elif opcao == 3:
        print(f'O número na opçao 3 é {num3}')
    else:
        print('Opção inválida')


main()

