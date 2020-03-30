def main():
    n = int(input('Digite um número da semana: '))

    dia_semana(n)

def dia_semana(n):
    if n == 1:
        print('Domingo')
    elif n == 2:
        print('Segunda')
    elif n == 3:
        print('Terça')
    elif n == 4:
        print('Quarta')
    elif n == 5:
        print('Quinta')
    elif n == 6:
        print('Sexta')
    elif n == 7:
        print('Sábado')
    else:
        print('Inválido')



main()

