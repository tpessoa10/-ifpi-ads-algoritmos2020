def main():
    sexo = input('Qual o seu sexo(M/F):').strip()

    qual_sexo(sexo)

def qual_sexo(sexo):
    if sexo in 'Mm':
        print('Masculino')
    elif sexo in 'Ff':
        print('Feminino')
    else:
        print('Inválido')


main()

