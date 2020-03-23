def main():
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segundo nota do aluno: '))

    media = (nota1 + nota2) / 2

    aprovado_reprovado(media)


def aprovado_reprovado(media):
    if media >= 7:
        print('Aluno aprovado')
    elif media <= 6.9:
        exame_final = float(input('Digite a nota do exame final: '))
        media_final = (media + exame_final) / 3
        if media_final >= 5:
            print('Aluno aprovado')
        elif media_final < 5:
            print('Aluno reprovado')



main()

