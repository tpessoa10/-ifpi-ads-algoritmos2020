def main():
    par = 0
    impar = 0 
    positivo = 0 
    negativo = 0

    quant_num = int(input('Quantos números deseja digitar: '))
    vetor = [-1] * quant_num
    numeros = input('Números que deseja adicionar ao vetor: ').split()
    resultado = []
    for num in numeros:
        resultado.append(int(num))
    pos = -1
    for item in vetor:
        pos = pos + 1
        vetor[pos] = resultado[pos]
    for i in vetor:
        if i % 2 == 0:
            par = par + 1
        elif i % 2 != 0:
            impar = impar + 1
        if i >= 0:
            positivo = positivo + 1
        elif i <= -1 :
            negativo = negativo + 1

    print('Quantidade de números pares {}'.format(par))
    print('Quantidade de números impares {}'.format(impar))
    print('Quantidade de números positivos {}.'.format(positivo))
    print('Quantidade de números negativos {}'.format(negativo))

    dobro_metade(vetor)
    par_impar_positivo_negativo_media(vetor)

def dobro_metade(vetor):
    for i in range(len(vetor)):
        if i >= 0:
            vetor[i] = vetor[i] * 2
        elif i <= 1:
            vetor[i] = vetor[i] // 2
    print('O novo vetor:{}'.format(vetor))

def par_impar_positivo_negativo_media(vetor):
    soma = 0
    par = 0
    impar = 0
    negativo = 0
    positivo = 0
    for i in vetor:
        if i % 2 == 0:
            par = par + 1
        elif i % 2 != 0:
            impar = impar + 1
        if i >= 0:
            positivo = positivo + 1
        elif i <= -1:
            negativo = negativo + 1
        
    print('Pares:{}'.format(par))
    print('Impares:{}'.format(impar))
    print('Positivos:{}'.format(positivo))
    print('Negativos:{}'.format(negativo))

    for i in vetor:
        soma += i
        media = soma // len(vetor)
    print('A media dos números é {}'.format(media))

    
    


main()

