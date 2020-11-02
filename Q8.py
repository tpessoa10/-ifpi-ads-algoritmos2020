def main():

    vetor = []
    n = int(input('Quantos elementos terá seu vetor: '))
    for i in range(n):
        num = int(input('Digite um número: '))
        vetor.append(num)

    print(vetor)

    maior = menor = 0
    qnt = 0
    for i in vetor:
        qnt += 1
        if qnt == 1:
            maior = menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    print('O maior número é {} e o menor é {}'.format(maior, menor))


main()
