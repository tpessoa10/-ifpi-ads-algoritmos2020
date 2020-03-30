def main():
    salario = float(input('Digite o salário do trabalhador: '))

    qual_salario(salario)

def qual_salario(salario):
    if salario <= 280:
        percentual = 0.20
        reajuste = salario * percentual
        novo_salario = salario + reajuste
    elif salario > 280 and salario <= 700:
        percentual = 0.15
        reajuste = salario * percentual
        novo_salario = salario + reajuste
    elif salario > 700 and salario <= 1500:
        percentual = 0.10
        reajuste = salario * percentual
        novo_salario = salario + reajuste
    elif salario > 1500:
        percentual = 0.05
        reajuste = salario * percentual
        novo_salario = salario + reajuste


    print(f'O salário do funcionário era {salario} R$')
    print(f'O reajuste foi de {percentual * 100} %')
    print(f'{reajuste} R$ acrescentados ao salário do funcionário')
    print(f'O seu salário passa a ser {novo_salario} R$')


main()

