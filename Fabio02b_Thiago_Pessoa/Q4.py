def main():
    nota1 = float(input('Digite a nota da primeira prova: '))
    nota2 = float(input('Digite a nota da segunda prova: '))

    media = (nota1 + nota2) / 2

    aprovado_reprovado(media)

def aprovado_reprovado(media):
    if media == 10:
        print('Aprovado com distinção')
    elif media >= 7:
        print('Aprovado')
    elif media < 7:
        print('Reprovado')


main()

