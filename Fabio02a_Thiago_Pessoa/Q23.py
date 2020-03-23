def main():
    dia_1, mes_1, ano_1 = input('Digite uma data: ').split('/')
    dia_1 = int(dia_1)
    mes_1 = int(mes_1)
    ano_1 = int(ano_1)
    dia_2, mes_2, ano_2 = input('Digite uma data: ').split('/')
    dia_2 = int(dia_2)
    mes_2 = int(mes_2)
    ano_2 = int(ano_2)


def maior_data(dia_1, dia_2, mes_1, mes_2, ano_1, ano_2):
    if mes_1 < 1 or mes_2 < 1 or dia_1 < 1 or dia_2 < 1:
        print('Data inválida')
    elif mes_1 > 12 or mes_2 > 12 or dia_1 > 31 or dia_2 > 31:
        print('Data inválida')
    elif ano_1 > ano_2:
        print(f'A data mais recente é {dia_1}/{mes_1}/{ano_1}')
    elif ano_2 > ano_1:
        print(f'A data mais recente é {dia_2}/{mes_2}/{ano_2}')
    elif ano_1 == ano_2:
        if mes_1 > mes_2:
            print(f'A data mais recente é {dia_1}/{mes_1}/{ano_1}')
        elif mes_2 > mes_1:
            print(f'A data mais recente é {dia_2}/{mes_2}/{ano_2}')
        elif mes_1 == mes_2:
            if dia_1 > dia_2:
                print(f'A data mais recente é {dia_1}/{mes_1}/{ano_1}')
            elif dia_2 > dia_1:
                print(f'A data mais recente é {dia_2}/{mes_2}/{ano_2}')
            elif dia_1 == dia_2:
                print('São as mesmas datas')


main()

