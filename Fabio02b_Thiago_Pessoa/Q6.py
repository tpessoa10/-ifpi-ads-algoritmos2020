def main():
    turno = input('Digite o seu turno (Matutino(M)/Vespertino(V)/Noturno(N)): ').strip()

    qual_turno(turno)

def qual_turno(turno):
    if turno in 'Mm':
        print('Bom dia! Seja bem vindo')
    elif turno in 'Vv':
        print('Boa tarde! Seja bem vindo')
    elif turno in 'Nn':
        print('Boa noite! Seja bem vindo')
    else:
        print('Valor inválido')


main()

