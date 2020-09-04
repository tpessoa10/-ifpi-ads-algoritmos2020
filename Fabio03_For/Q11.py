def main():

    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior, limite_superior):
        cont = 0
        for x in range(1, i+1):
            if i % x == 0:
                cont = cont + 1
        if cont == 2:
            print(i)


main()

