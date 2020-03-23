def main():
   dia_atual, mes_atual, ano_atual = input('Digite a data atual: ').split('/')
   dia_atual = int(dia_atual)
   mes_atual = int(mes_atual)
   ano_atual = int(ano_atual)

   dia_nasc, mes_nasc, ano_nasc =input('Digite a data de nascimento: ').split('/')
   dia_nasc = int(dia_nasc)
   mes_nasc = int(mes_nasc)
   ano_nasc = int(ano_nasc)

   saber_idade(dia_atual, dia_nasc, mes_atual, mes_nasc, ano_atual, ano_nasc)

def saber_idade(dia_atual, dia_nasc, mes_atual, mes_nasc, ano_atual, ano_nasc):
   idade_anos = ano_atual - ano_nasc
   if mes_atual < mes_nasc:
      if dia_atual < dia_nasc:
         idade_anos = idade_anos - 1

   print(f'A pessoa tem {idade_anos} anos de idade')


main()

