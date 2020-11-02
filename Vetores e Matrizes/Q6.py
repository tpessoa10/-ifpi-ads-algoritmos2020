def main():

    lista = []
    print('Digite um número com 8 elementos')
    for i in range(0, 8):
        num = int(input('Digite os números binários: '))
        lista.append(num)

    def binario_para_decimal(lista):
        pos = -1
        soma = 0
        soma1 = 0
        lista.reverse()
        for n in lista:
            pos += 1
            decimal = n * (2**pos)
            soma = soma + decimal
        print('O número em decimal é {}'.format(soma))
    

    def binario_para_hexadecimal(lista):
        primeira_metade = lista[0:4]
        segunda_metade = lista[4:8]
        pos = -1
        pos1 = -1
        soma = 0
        soma1 = 0
        lista.reverse()
        for i in primeira_metade:
            pos += 1
            decimal = i * (2**pos)
            soma = soma + decimal
        if soma == 10:
            soma = 'A'
        elif soma == 11:
            soma = 'B'
        elif soma == 12:
            soma = 'C'
        elif soma == 13:
            soma = 'D'
        elif soma == 14:
            soma = 'E'
        elif soma == 15:
            soma = 'F'   
        for n in segunda_metade:
            pos1 += 1
            decimal1 = n * (2**pos1)
            soma1 = soma1 + decimal1
        if soma1 == 10:
            soma1 = 'A'
        elif soma1 == 11:
            soma1 = 'B'
        elif soma1 == 12:
            soma1 = 'C'
        elif soma1 == 13:
            soma1 = 'D'
        elif soma1 == 14:
            soma1 = 'E'
        elif soma1 == 15:
            soma1 = 'F'


        print('O número em hexadecimal fica {}{}'.format(soma1,soma))
        


    binario_para_decimal(lista)

    binario_para_hexadecimal(lista)



main()

