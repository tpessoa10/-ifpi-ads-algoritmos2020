def main():
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    operacao = int(input('Digite qual operação deseja realizar(1-Adição/2-Subtração/3-Multiplicação/4-Divisão): '))

    qual_operacao(n1, n2, operacao)


def qual_operacao(n1, n2, operacao):
    if operacao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif operacao == 2:
        sub = n1 - n2
        print(f'{n1} - {n2} = {sub}')
    elif operacao == 3:
        multi = n1 * n2
        print(f'{n1} x {n2} = {multi}')
    elif operacao == 4:
        div = n1 / n2 
        print(f'{n1} / {n2} = {div}')
    elif operacao < 1 or operacao >= 5:
        print('Escolha somente números de 1 a 4')


main()

