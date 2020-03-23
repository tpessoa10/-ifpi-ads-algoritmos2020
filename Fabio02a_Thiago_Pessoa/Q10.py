def main():
    dia, mes, ano = input('Digite uma data: ').split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    data_valida(dia, mes, ano)

def data_valida(dia, mes, ano):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 31 and dia > 0:
            print('Data válida')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 30 and dia > 0:
            print('Data válida')
    elif mes == 2:
        if dia <= 28 and dia > 0:
            print('Data válida')
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia <= 29 and dia > 0:
                print('Data válida')
    else:
        print('Data inválida')


main()