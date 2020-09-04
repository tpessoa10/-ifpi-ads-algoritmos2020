def main():

    n = int(input('Digite a quantidade de habitantes: '))
    ac_salario = 0
    ac_filhos = 0
    acum_menos_mil = 0
    
    for i in range(n):
        salario = float(input('Salario: '))
        filhos = int(input('Quantidade de filhos: '))

        ac_salario = ac_salario + salario
        media_salario = ac_salario // n

        ac_filhos = ac_filhos + filhos
        media_filhos = ac_filhos // n

        if salario <= 1000:
            acum_menos_mil = acum_menos_mil + 1

            percentual = (100 / n) * acum_menos_mil

    print('A media de salário da população é {}'.format(media_salario))
    print('A media de filhos da população é {}'.format(media_filhos))
    print('O percentual de pessoas que ganham até 1000R$ é de {}%'.format(percentual))





main()

