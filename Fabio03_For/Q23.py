def main():

    n = int(input('Digite a quantidade de funcionários: '))

    for i in range(n):
        codigo = int(input('Digite o codigo: '))
        horas = int(input('Digite a quantidade de horas trabalhadas: '))
        dependentes = int(input('Digite a quantidade de dependentes desse funcionário: '))

        dinheiro_hora = horas * 12.00
        dinheiro_dependentes = dependentes * 40.00
        salario_total = dinheiro_hora + dinheiro_dependentes
        desconto_inss = salario_total * 0.085
        desconto_ir = salario_total * 0.05
        salario_liquido = salario_total - (desconto_inss + desconto_ir)

        print('Desconto INSS: {}'.format(desconto_inss))
        print('Desconto IR: {}'.format(desconto_ir))
        print('Salário liquido: {}'.format(salario_liquido))




main()

