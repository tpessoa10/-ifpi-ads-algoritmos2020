def main():
    a = []
    elementos = int(input('Quantos elementos terá seu vetor: '))
    for i in range(elementos):
        num = int(input('Digite um número: '))
        a.append(num)

    repetidos = []
    for c in a:
        if c not in repetidos:
            repetidos.append(c)

    if len(a) == len(repetidos):
        print('Não existem números repetidos')
    else:
        print('Existe números repetidos')


main()