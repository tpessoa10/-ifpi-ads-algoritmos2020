def main():

    n = int(input('Digite a quantidade de habitantes: '))
    c = 1
    acum_salario = 0
    media_salario = 0
    acum_filhos = 0
    media_filhos = 0
    acum_menos_mil = 0
    percentual = 0

    while c <= n:
        salario = float(input('Digite seu salário: '))
        filhos = int(input('Digite a quantidade de filhos: '))
        c = c + 1
        
        acum_salario = acum_salario + salario
        media_salario = acum_salario // n 

        acum_filhos = acum_filhos + filhos
        media_filhos = acum_filhos / n

        if salario <= 1000:
            acum_menos_mil = acum_menos_mil + 1

            percentual = (100 / n) * acum_menos_mil

    print('A media de salário da população é {}'.format(media_salario))
    print('A media de filhos da população é {}'.format(media_filhos))
    print('O percentual de pessoas que ganham até 1000R$ é de {}%'.format(percentual))
    print(acum_menos_mil)


main()

