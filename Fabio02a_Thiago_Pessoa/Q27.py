def main():
    dia_nasc, mes_nasc, ano_nasc = input('Digite a data do nascimento: ').split('/')
    dia_nasc = int(dia_nasc)
    mes_nasc = int(mes_nasc)
    ano_nasc = int(ano_nasc)

    dia_atual, mes_atual, ano_atual = input('Digite a data atual: ').split('/')
    dia_atual = int(dia_atual)
    mes_atual = int(mes_atual)
    ano_atual = int(ano_atual)


    idade_anos = ano_atual - ano_nasc
    if mes_atual > mes_nasc:
        idade_meses = mes_atual - mes_nasc
        print(f'A idade em meses é {idade_meses}')
    elif mes_nasc > mes_atual:
        idade_meses = (12 - mes_nasc) + mes_atual
        print(f'A idade em meses é {idade_meses}')
    if dia_atual > dia_nasc:
        idade_dias = dia_atual - dia_nasc
        print(f'A idade em dias é {idade_dias}')
    elif dia_nasc > dia_atual:
        idade_dias = (31 - dia_nasc) + dia_atual
        print(f'A idade em dias é {idade_dias}')
    if dia_atual < dia_nasc:
        idade_anos = idade_anos - 1
        idade_meses = idade_meses - 1


    print(f'A idade é {idade_anos} anos {idade_meses} meses e {idade_dias} dias')


main()


