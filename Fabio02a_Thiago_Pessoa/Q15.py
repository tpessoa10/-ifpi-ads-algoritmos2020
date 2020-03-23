def main():

    horas_prof1 = int(input('Digite a quantidade de horas aula dadas por um professor: '))
    horas_prof2 = int(input('Digite a quantidade de horas aulas dadas por outro professor: '))
    valor_hora1 = float(input('Digite o valor por hora que o primeiro professor recebe: '))
    valor_hora2 = float(input('Digite o valor por hora que o segundo professor recebe:  '))

    salario1 = horas_prof1 * valor_hora1
    salario2 = horas_prof2 * valor_hora2

    print(f'O primeiro professor ganha {salario1} e o segundo ganha {salario2}')

    ganha_mais(salario1, salario2)

def ganha_mais(salario1, salario2):
    if salario1 > salario2:
        print('O primeiro professor ganha mais')
    elif salario2 > salario1:
        print('O segundo professor ganha mais')
    else:
        print('Salario iguais')


main()

